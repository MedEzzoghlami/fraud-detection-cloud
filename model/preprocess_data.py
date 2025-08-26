import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
import os

df = pd.read_csv("C:\\Users\\Toshiba\\fraud-detection-cloud\\data\\creditcard.csv")

X = df.drop("Class", axis=1)
y = df["Class"]

scaler = StandardScaler()
X[["Time", "Amount"]] = scaler.fit_transform(X[["Time", "Amount"]])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

os.makedirs("processed", exist_ok=True)
X_train.to_csv("processed/X_train.csv", index=False)
X_test.to_csv("processed/X_test.csv", index=False)
y_train.to_csv("processed/y_train.csv", index=False)
y_test.to_csv("processed/y_test.csv", index=False)

joblib.dump(scaler, "processed/scaler.pkl")

print("processing complete")
print("Processed files are saved in 'processed' directory")
