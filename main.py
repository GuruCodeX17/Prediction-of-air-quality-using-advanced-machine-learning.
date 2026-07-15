import pandas as pd

# Load the dataset
df = pd.read_csv("data/raw/AirQualityUCI.csv", sep=";")

print("========== AIR QUALITY PREDICTION PROJECT ==========\n")

# First 5 rows
print("First 5 Rows:")
print(df.head())

# Shape
print("\nDataset Shape:")
print(df.shape)

# Column names
print("\nColumns:")
print(df.columns)

# Information
print("\nDataset Information:")
df.info()

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Statistical Summary
print("\nStatistical Summary:")
print(df.describe())