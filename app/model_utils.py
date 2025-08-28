import pickle
import pandas as pd
import os
import requests

MODEL_PATH = "model/xgb_fraud_model.pkl"
GITHUB_RAW_URL = "https://github.com/MedEzzoghlami/fraud-detection-cloud/raw/refs/heads/main/xgb_fraud_model.pkl"

# Ensure the model folder exists
os.makedirs("model", exist_ok=True)

# Download the model if it doesn't exist
if not os.path.exists(MODEL_PATH):
    print("Model not found locally. Downloading from GitHub...")
    response = requests.get(GITHUB_RAW_URL)
    if response.status_code == 200:
        with open(MODEL_PATH, "wb") as f:
            f.write(response.content)
        print("Model downloaded successfully.")
    else:
        raise Exception(f"Failed to download model: {response.status_code}")

# Load model + threshold
with open(MODEL_PATH, "rb") as f:
    model, best_threshold = pickle.load(f)

def predict_fraud(input_data: pd.DataFrame):
    """
    input_data: pd.DataFrame with same columns as training data
    returns: predictions (0=not fraud, 1=fraud) and probabilities
    """
    proba = model.predict_proba(input_data)[:, 1]
    pred = (proba >= best_threshold).astype(int)
    return pred.tolist(), proba.tolist()
