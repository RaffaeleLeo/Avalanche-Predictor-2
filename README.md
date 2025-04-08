## Avalanche Predictor 2

A machine learning project focused on predicting **avalanche severity** based on real-world reports and environmental data.

This second iteration builds on earlier work, expanding the dataset and ML techniques to better understand avalanche conditions — driven by curiosity as a backcountry skier and a passion for applied machine learning.

---

### Project Highlights

- Uses a rich dataset from the **Colorado Avalanche Information Center (CAIC)** with over 25,000 avalanche incidents.
- Predicts **severity** of avalanches (not just occurrence) based on weather, snowpack, location, and more.
- Explores traditional and modern ML techniques:
  - **Random Forests**, **Logistic Regression**, and **Neural Networks**
  - **OpenAI's text-embedding-ada-002** model for NLP-based similarity analysis
  - **Cosine similarity** for semantic matching of avalanche descriptions

---

### Key Experiments

#### 1. **Embedding-Based Severity Clustering**
- Avalanche reports were embedded using OpenAI's `text-embedding-ada-002` model.
- Embeddings were projected to 2D using dimensionality reduction.
- A Random Forest model was used to check if similar reports led to similar severity.

<p align="center">
  <img width="433" src="https://github.com/user-attachments/assets/bf360cfc-426f-4063-81f4-0943371475c5" alt="Embeddings visualization">
</p>

#### 2. **Cosine Similarity Matching**
- A basic input description is matched to the most semantically similar avalanche reports using cosine similarity on the embedding space.
- The matched reports give a quick insight into likely severity based on historical similarity.

Example:
> Input: *"Heading up a large north-facing slope in the Vail area, snow is dry with an icy underlayer."*

Top 5 most similar matches:
<p align="center">
  <img width="684" src="https://github.com/user-attachments/assets/50ffd9ba-cacf-4142-8f80-83494590a10e" alt="Cosine similarity output">
</p>

---

### Tech Stack

- Python (Pandas, NumPy, Scikit-learn, PySpark)
- OpenAI Embeddings API
- Dimensionality Reduction (PCA/UMAP)
- Jupyter for exploration and prototyping

---

### Interactive Classifier (Spark-based)

This script prompts users step-by-step and predicts the **danger level** based on conditions and location using a PySpark model pipeline.

#### **Run the script**
```bash
python classifier.py
```
You'll be asked to enter:
- Elevation
- Slope aspect
- Snow type
- Travel method
- Slope size
- Colorado region

The model will respond with a message like:
> "Your danger level is D3: danger levels are high, avalanches have the possibility of moving vehicles."
