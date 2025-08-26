import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\Toshiba\\fraud-detection-cloud\\data\\creditcard.csv")

print("shape:", df.shape)
print("columns:", df.columns.tolist())
print("Missing values:\n", df.isnull().sum().sum())

print("class distribution: \n", df['Class'].value_counts())
print(df.describe())

df['Class'].value_counts().plot(kind='bar')
plt.title("Normal vs fraud Transaction")
plt.xlabel("Class (0=Normal, 1=Fraud)")
plt.ylabel("Count")
plt.show()
