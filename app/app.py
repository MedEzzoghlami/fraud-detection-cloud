import logging
from fastapi import FastAPI, Request, Depends
from typing import List
import pandas as pd
from sqlalchemy.orm import Session

from app.schemas import Transaction, PredictionResponse
from app.model_utils import predict_fraud
from app.dependencies import get_db
from app import crud

# -------------------------------
# Logging Configuration
# -------------------------------
# General info log
info_logger = logging.getLogger("info_logger")
info_handler = logging.FileHandler("info.log")
info_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
info_handler.setFormatter(info_formatter)
info_logger.setLevel(logging.INFO)
info_logger.addHandler(info_handler)

# Fraud warnings log
fraud_logger = logging.getLogger("fraud_logger")
fraud_handler = logging.FileHandler("fraud.log")
fraud_handler.setFormatter(info_formatter)
fraud_logger.setLevel(logging.WARNING)
fraud_logger.addHandler(fraud_handler)

# -------------------------------
# FastAPI App
# -------------------------------
app = FastAPI(title="Fraud Detection")

@app.middleware("http")
async def log_requests(request: Request, call_next):
    info_logger.info(f"Incoming request: {request.method} {request.url}")
    response = await call_next(request)
    info_logger.info(f"Response status: {response.status_code}")
    return response

@app.get("/")
def root():
    return {"message": "Fraud Detection API is running!"}

@app.get("/health")
def health():
    return {"status": "running"}

@app.post("/predict", response_model=PredictionResponse)
def predict(transactions: List[Transaction], db: Session = Depends(get_db)):
    # Convert transactions into DataFrame
    data = pd.DataFrame([t.dict() for t in transactions])

    # Get prediction + probabilities
    pred, proba = predict_fraud(data)

    # Save each transaction and log
    for i, t in enumerate(transactions):
        crud.create_transaction(
            db=db,
            data=t.dict(),
            is_fraud=bool(pred[i]),
            probability=float(proba[i])
        )

        # Log every transaction using Time instead of id
        info_logger.info(
            f"Transaction at Time={t.Time} predicted: {pred[i]}, probability: {proba[i]:.4f}"
        )

        # Highlight high-probability frauds
        if proba[i] > 0.8:
            fraud_logger.warning(
                f"High-probability fraud detected! Transaction at Time={t.Time}, probability: {proba[i]:.4f}"
            )

    return PredictionResponse(prediction=list(pred), probability=list(proba))

@app.get("/transactions")
def list_transactions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_transactions(db, skip=skip, limit=limit)
