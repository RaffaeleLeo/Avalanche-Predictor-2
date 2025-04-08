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

## Training

All training was done in Colab:

- [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/17CC6RTRE8M_lyUVK5uHwXcGs3fxLnIbo?usp=sharing)
- Dataset and training parameters are configurable in the notebook

---

### Tech Stack

- Python (Pandas, NumPy, Scikit-learn, PySpark)
- OpenAI Embeddings API
- Dimensionality Reduction (PCA/UMAP)
- Jupyter for exploration and prototyping

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

### New: Backcountry Assistant
A natural-language interface for backcountry skiers.

This assistant takes a user’s trip description (e.g., “South-facing slope near Vail, slushy conditions”), finds the five most similar avalanche reports from the CAIC dataset, and then:

Predicts a danger level (D1–D5) based on historical severity data

Generates a safety advisory using an LLM (gpt-4o-mini) that summarizes what to look out for based on those past events

It leverages OpenAI embeddings for similarity search and combines it with LLM-powered summarization for a skier-facing output.

### Run the assistant

```bash
python3 assistant.py
```

Example interaction:

```vbnet
Hello! I will be your backcountry assistant for today, just tell me what your conditions are and I
      will give tips on what dangers to look for and avoid using avalanche data from the past.
Enter a description of the avalanche scenario: Hi! I am heading up a westfacing slope near vail where me and two friends will ski down a narrow shoot into a wide bowl, conditions are cold and sunny and it has not snowed for a few days.

Predicted Danger Rating for Your Scenario: D1.5

Based on the current conditions you're facing and the historical avalanche reports in similar situations, here’s some advice for your skiing day:

1. **Avalanche Danger Awareness**: You mentioned an average danger rating of 1.5, which falls between D1 and D2. While this rating suggests that conditions are relatively safe, it does indicate a slight risk of avalanches large enough to bury a person. Stay vigilant, especially in steep or wind-loaded areas.

2. **Slope Orientation and Aspect**: Since you're skiing on a west-facing slope, be aware that the stability can vary based on the specific aspect, especially since you have reports of avalanches on both easterly and westerly aspects. Avalanches can still be triggered by human activity, especially in steep terrain.

3. **Narrow Chutes and Bowls**: When skiing into a narrow chute leading into a wide bowl, be cautious of potential loading from wind and the possibility of slab formation. Watch for signs of instability such as cracking or whumpfing sounds, which can indicate a weak layer beneath the snow.

4. **Recent Weather**: The cold and sunny conditions following several days without snow may have led to some surface stabilization, but be alert for any signs of warming, especially if the sun hits the slope directly. This can create wet loose snow conditions, which could trigger small avalanches.

In summary, while the conditions may seem favorable, remain cautious, particularly in steep areas, and keep an eye on the snowpack behavior as you proceed. Stay safe and have fun!
```
---

### Interactive Classifier (Spark-based)

This script prompts users step-by-step and predicts the **danger level** based on conditions and location using a PySpark model pipeline.

#### **Run the script**
```bash
python3 classifier.py
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
