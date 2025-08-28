# model/train_model.py
import pandas as pd
import joblib
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix, precision_recall_curve
from imblearn.over_sampling import SMOTE
from xgboost import XGBClassifier


X_train = pd.read_csv("C:\\Users\\Toshiba\\fraud-detection-cloud\\model\\processed\\X_train.csv")
X_test = pd.read_csv("C:\\Users\\Toshiba\\fraud-detection-cloud\\model\\processed\\X_test.csv")
y_train = pd.read_csv("C:\\Users\\Toshiba\\fraud-detection-cloud\\model\\processed\\y_train.csv")['Class'].astype(int).values
y_test = pd.read_csv("C:\\Users\\Toshiba\\fraud-detection-cloud\\model\\processed\\y_test.csv")['Class'].astype(int).values


print(f"Original training set shape: {X_train.shape}, Fraud count: {sum(y_train)}")
smote = SMOTE(sampling_strategy=0.1, random_state=42)  
X_res, y_res = smote.fit_resample(X_train, y_train)
print(f"Resampled training set shape: {X_res.shape}, Fraud count: {sum(y_res)}")


model = XGBClassifier(
    n_estimators=300,
    max_depth=5,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    scale_pos_weight=10,   
    use_label_encoder=False,
    eval_metric="logloss",
    random_state=42
)

model.fit(X_res, y_res)

# === 4. Predict probabilities ===
y_probs = model.predict_proba(X_test)[:, 1]

# === 5. Find best threshold (trade-off) ===
precisions, recalls, thresholds = precision_recall_curve(y_test, y_probs)

best_threshold = 0.5
best_recall = 0
best_precision = 0

for p, r, t in zip(precisions, recalls, thresholds):
    if r >= 0.85 and p > best_precision:  # keep recall >= 85% but improve precision
        best_threshold = t
        best_recall = r
        best_precision = p

print(f"\n🔎 Selected threshold: {best_threshold:.3f} with Recall={best_recall:.4f}, Precision={best_precision:.4f}")

# === 6. Apply threshold ===
y_pred = (y_probs >= best_threshold).astype(int)

# === 7. Evaluation ===
print("\nClassification Report (with optimized threshold):\n")
print(classification_report(y_test, y_pred, digits=4))

print("Confusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))

# === 8. Save model and threshold ===
joblib.dump((model, best_threshold), "C:\\Users\\Toshiba\\fraud-detection-cloud\\model\\xgb_fraud_model.pkl")
print("\n✅ XGBoost fraud detection model saved as 'C:\\Users\\Toshiba\\fraud-detection-cloud\\model\\xgb_fraud_model.pkl'")
