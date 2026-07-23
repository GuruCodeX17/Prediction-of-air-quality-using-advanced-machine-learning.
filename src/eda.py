import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/AirQualityUCI.csv", sep=";")

# Remove empty columns
df = df.drop(columns=["Unnamed: 15", "Unnamed: 16"])

print("========== EXPLORATORY DATA ANALYSIS ==========\n")

# Dataset Shape
print("Dataset Shape:")
print(df.shape)

# Column Names
print("\nColumn Names:")
print(df.columns)

# Data Types
print("\nData Types:")
print(df.dtypes)

# Dataset Information
print("\nDataset Information:")
df.info()

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Statistical Summary
print("\nStatistical Summary:")
print(df.describe())