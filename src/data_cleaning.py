import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/AirQualityUCI.csv", sep=";")

# Remove unwanted columns
df = df.drop(columns=["Unnamed: 15", "Unnamed: 16"])

# Replace invalid values (-200) with NaN


df.replace(-200, pd.NA, inplace=True)

print("Shape after cleaning:", df.shape)
print(df.shape)

print("\nMissing values:")
print(df.isnull().sum())