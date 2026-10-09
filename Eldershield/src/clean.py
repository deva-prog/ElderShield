import os
import pandas as pd

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(BASE, "data", "healthcare-dataset-stroke-data.csv")
OUT_PATH = os.path.join(BASE, "data", "clean_stroke.csv")

print("CSV yahan dhoondh raha hoon:", CSV_PATH)

df = pd.read_csv(CSV_PATH)

df = df.drop(columns=["id"])
df = df[df["gender"] != "Other"]
df["bmi"] = df["bmi"].fillna(df["bmi"].median())
df = pd.get_dummies(df, drop_first=True)

print("New shape:", df.shape)
print("Missing values left:", df.isnull().sum().sum())
print("Columns:", list(df.columns))

df.to_csv(OUT_PATH, index=False)
print("Saved:", OUT_PATH)