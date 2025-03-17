# Avalanche-Predictor-2
Second attempt at predicting future avalanches

A second attempt at predicting avalanches using a variety of neural network and machine learning techniques, both for my own curiosity as a backcountry skier and to learn new technologys.

# Main Differences From First Attempt

On my first attempt I used the Utah Avalanche Center as my database and a variety of simple decision tree and perceptron neworks. On this attempt I used:

* The Colorado Avalance Information Center database, which has 25,000 avalanches and their data on record
* A larger variety of techniques including random forest, logistic regression, and similarity algorithms through embeddings
* I decided to change the focus from predicting if an avalanche would occur to predicting the severity of an avalanche under certain conditions.

# Embedding Experiments

* Using the Open-AI text-embedding-ada-002 model I was able to embedd the avalaces to try and sort through them by similarity to see if avalanches of similar severity has similar data associated with them

* The embeddings looked like this:


* After running the embedding ada model, mapping the high-dimentional embeddings to the 2d plane, I ran a random forest algorithm to see if avalanches of similar seveity were saved under similar conditions, the results are below.

# Cosign similarity

* Lastly I tried cosine-similarity to get the description that matched the user inputs the most, then get the danger rating of that datapoint.

* Below is an example of the top 5 most similar data points to the description “heading up a large north facing slope in the vail area, snow is dry with an icy underlayer”

