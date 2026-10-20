import pandas as pd

df = pd.read_csv("data/healthcare-dataset-stroke-data.csv")

print("Shape:", df.shape)
print("\nColumns:", list(df.columns))
print("\nFirst 5 rows:")
print(df.head())
print("\nMissing values:")
print(df.isnull().sum())
print("\nStroke count (0 = no stroke, 1 = stroke):")
print(df["stroke"].value_counts())