import pandas as pd

# Load the dataset
df = pd.read_csv("data/raw/AirQualityUCI.csv", sep=";")

print("========== DATA PREPROCESSING ==========\n")

# Dataset shape
print("Dataset Shape:")
print(df.shape)

# Column names
print("\nColumn Names:")
print(df.columns)

# Data information
print("\nDataset Information:")
df.info()

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())