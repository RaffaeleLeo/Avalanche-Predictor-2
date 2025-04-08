import pandas as pd
from pyspark.sql import SparkSession
from pyspark.ml import PipelineModel
import os
import logging
from config import input_config, danger_levels

os.environ["PYSPARK_SUBMIT_ARGS"] = "--conf spark.ui.showConsoleProgress=false pyspark-shell"
logging.getLogger("py4j").setLevel(logging.ERROR)

# --- Initialize Spark Session ---
spark = SparkSession.builder.appName("AvalanchePredictor").config("spark.driver.extraJavaOptions", "-Djava.security.manager=allow").config("spark.executor.extraJavaOptions", "-Djava.security.manager=allow").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

# --- Load Trained Pipeline Model ---
cvModel = PipelineModel.load("data/cvModel")

# --- Run Prediction ---
def predict():
    print("\n  Welcome to the Avalanche Danger Estimator ")

    # Get input from user
    input_data = {}
    for key, cfg in input_config.items():
        while True:
            val = input(cfg["prompt"]).strip().upper()
            if val in cfg["map"]:
                input_data[key] = cfg["map"][val]
                break
            else:
                print("Invalid input. Please try again.")

    # Convert to DataFrame
    df = pd.DataFrame([{
        'Elev_imputed': input_data['elevation'],
        'Asp_imputed': input_data['aspect'],
        'Type_imputed': input_data['snow_type'],
        'Trig_imputed': input_data['transportation'],
        'sizeR_imputed': input_data['slope_size'],
        'Area_imputed': input_data['area']
    }])

    # Predict with Spark pipeline
    spark_df = spark.createDataFrame(df)
    pred = cvModel.transform(spark_df).collect()[0][9]

    # Print danger level
    print("\n Predicted Avalanche Danger Level:")
    print(danger_levels.get(pred, f"D? - Unknown danger level ({pred})"))

if __name__ == "__main__":
    predict()
