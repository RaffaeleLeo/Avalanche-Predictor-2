import pandas as pd
import numpy as np
from openai import OpenAI
import ast
from sklearn.metrics.pairwise import cosine_similarity

import os
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("Loading data...")
embeddings_df = pd.read_csv("data/embeddings.csv")
metadata = pd.read_csv("data/avalanche_record_CAIC.csv")

# Parse embeddings
embeddings = embeddings_df['embedding'].apply(ast.literal_eval).tolist()
embeddings = np.array(embeddings)

print("""\nHello! I will be your backcountry assistant for today, just tell me what your conditions are and I
      will give tips on what dangers to look for and avoid using avalanche data from the past.""")
user_description = input("Enter a description of the avalanche scenario: ")

# embed input with open ai
response = client.embeddings.create(
    input=user_description,
    model="text-embedding-ada-002"
)

user_embedding = np.array(response.data[0].embedding).reshape(1, -1)

# Cosign Similarities
similarities = cosine_similarity(user_embedding, embeddings)[0]
top_indices = similarities.argsort()[::-1][:5]  # Top 5


# Normalize Danger Ratings
valid_reports = []

for idx in top_indices:
    row = metadata.iloc[idx]
    size = row.get('sizeD', '').strip().upper()
    desc = row.get('Description', '').strip()
    
    # Only include reports with both a valid danger level and a description
    if size.startswith("D") and desc:
        try:
            danger_val = float(size[1:])
            valid_reports.append((danger_val, desc))
        except ValueError:
            continue 

# Compute average danger rating
danger_levels = [r[0] for r in valid_reports]
descriptions = [r[1] for r in valid_reports]

if danger_levels:
    avg_danger = round(np.mean(danger_levels), 2)
else:
    avg_danger = "Unknown"

print(f"\nPredicted Danger Rating for Your Scenario: D{avg_danger}")

# Generate summary using open ai
if descriptions:
    combined_text = "\n".join(descriptions)
    prompt = f"""You are an avalanche safety expert. The user input the conditions that they are skiing in and we found 5 avalanches that happend during similar conditions.
                Given the average danger rating and the descriptions of the avalanches below, give the user advice on what to look out for when going skiing that day.

                User Input:
                {user_description}

                Average Danger Rating:
                {avg_danger}
                Danger Rating Descriptions:
                D1 - Safe to go out, avalanches will not be large enough to cause harm to humans
                D2 - Slightly dangerous, avalanches could get large enough to bury a person
                D3+ - Danger high, avalanches could be large enough to move vehicles

                Reports of avalances that occured in similar conditions:
                {combined_text}

                Summary:"""

    # Generate safety summary
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an avalanche safety expert."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=600
    )

    print(completion.choices[0].message.content)
else:
    print("\nNo descriptions available to generate summary.")

