import pandas as pd

# Load dataset
df = pd.read_csv("data/students.csv")

print("Original Shape:", df.shape)

# Remove duplicate rows
df = df.drop_duplicates()

# Handle missing values
for col in df.select_dtypes(include="number").columns:
    df[col] = df[col].fillna(df[col].mean())

# Encode categorical columns
df = pd.get_dummies(df, drop_first=True)

print("After Preprocessing:", df.shape)

print("\nFirst 5 rows:")
print(df.head())