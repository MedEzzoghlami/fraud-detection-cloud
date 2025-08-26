import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import (
    classification_report, confusion_matrix,
    roc_curve, auc, precision_recall_curve, accuracy_score, f1_score, precision_score, recall_score
)
import seaborn as sns
import os
from datetime import datetime

# ===========================
# 0. Create timestamped results folder
# ===========================
base_dir = "results"
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
results_dir = os.path.join(base_dir, timestamp)
os.makedirs(results_dir, exist_ok=True)

# ===========================
# 1. Load dataset & model
# ===========================
print("🔄 Loading dataset and model...")

df = pd.read_csv("data/creditcard.csv")

X = df.drop("Class", axis=1)
y = df["Class"]

with open("model/xgb_fraud_model.pkl", "rb") as f:
    model, best_threshold = pickle.load(f)

print("✅ Model loaded successfully!")

# ===========================
# 2. Predictions
# ===========================
y_proba = model.predict_proba(X)[:, 1]
threshold = 0.799   # from training day
y_pred = (y_proba >= threshold).astype(int)

# ===========================
# 3. Reports
# ===========================
report = classification_report(y, y_pred, digits=4)
print("\n📊 Classification Report (with threshold):\n")
print(report)

cm = confusion_matrix(y, y_pred)
print("\nConfusion Matrix:")
print(cm)

# ROC AUC
fpr, tpr, _ = roc_curve(y, y_proba)
roc_auc = auc(fpr, tpr)

# PR AUC
precision_curve, recall_curve, _ = precision_recall_curve(y, y_proba)
pr_auc = auc(recall_curve, precision_curve)

# ===========================
# 4. Save metrics (CSV + TXT)
# ===========================
metrics = {
    "Accuracy": accuracy_score(y, y_pred),
    "Precision": precision_score(y, y_pred),
    "Recall": recall_score(y, y_pred),
    "F1": f1_score(y, y_pred),
    "ROC_AUC": roc_auc,
    "PR_AUC": pr_auc
}
metrics_df = pd.DataFrame([metrics])
metrics_df.to_csv(os.path.join(results_dir, "metrics.csv"), index=False)

# Save text report
with open(os.path.join(results_dir, "classification_report.txt"), "w") as f:
    f.write("Classification Report:\n")
    f.write(report + "\n\n")
    f.write("Confusion Matrix:\n")
    f.write(str(cm) + "\n\n")
    f.write(f"ROC AUC: {roc_auc:.4f}\n")
    f.write(f"PR AUC : {pr_auc:.4f}\n")

# ===========================
# 5. Confusion Matrix Plot
# ===========================
plt.figure(figsize=(5,4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["Not Fraud", "Fraud"], yticklabels=["Not Fraud", "Fraud"])
plt.title("Confusion Matrix")
plt.ylabel("True label")
plt.xlabel("Predicted label")
plt.tight_layout()
plt.savefig(os.path.join(results_dir, "confusion_matrix.png"))
plt.close()

# ===========================
# 6. ROC Curve
# ===========================
plt.figure(figsize=(6,5))
plt.plot(fpr, tpr, color="darkorange", lw=2, label=f"ROC curve (AUC = {roc_auc:.4f})")
plt.plot([0, 1], [0, 1], color="navy", lw=2, linestyle="--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("Receiver Operating Characteristic (ROC)")
plt.legend(loc="lower right")
plt.tight_layout()
plt.savefig(os.path.join(results_dir, "roc_curve.png"))
plt.close()

# ===========================
# 7. Precision-Recall Curve
# ===========================
plt.figure(figsize=(6,5))
plt.plot(recall_curve, precision_curve, color="purple", lw=2, label=f"PR AUC = {pr_auc:.4f}")
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.title("Precision-Recall Curve")
plt.legend(loc="lower left")
plt.tight_layout()
plt.savefig(os.path.join(results_dir, "precision_recall_curve.png"))
plt.close()

# ===========================
# 8. Feature Importance
# ===========================
try:
    import xgboost as xgb
    model_booster = model.get_booster()
    importance = model_booster.get_score(importance_type="weight")
    importance_df = pd.DataFrame({"Feature": list(importance.keys()), "Importance": list(importance.values())})
    importance_df = importance_df.sort_values(by="Importance", ascending=False)

    plt.figure(figsize=(8,6))
    sns.barplot(x="Importance", y="Feature", data=importance_df.head(15), palette="viridis")
    plt.title("Top 15 Important Features (XGBoost)")
    plt.tight_layout()
    plt.savefig(os.path.join(results_dir, "feature_importance.png"))
    plt.close()
except Exception as e:
    print("⚠️ Feature importance not available:", e)

print(f"\n✅ Evaluation complete! Results saved in '{results_dir}/'")
