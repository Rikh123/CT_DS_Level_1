#  Import necessary libraries
import pandas as pd

# Load the dataset
df = pd.read_csv("Cleaned_Dataset_Task1.csv")  # Ensure the correct file path

# 1️⃣ Basic Statistical Measures for Numerical Columns
print("\n Basic Statistics for Numerical Columns:")
print(df.describe())  # Provides mean, median, std deviation, min, max, etc.

# 2️⃣ Exploring Categorical Variables
print("\n Unique values in categorical columns:")

# Count the number of unique values in categorical columns
categorical_columns = ["Country Code", "City", "Cuisines"]
for col in categorical_columns:
    print(f"{col}: {df[col].nunique()} unique values")

# 3️⃣ Identifying Top Cuisines and Cities with the Most Restaurants
print("\n Top 10 Cuisines with the Highest Number of Restaurants:")
print(df["Cuisines"].value_counts().head(10))  # Top 10 cuisines

print("\n Top 10 Cities with the Most Restaurants:")
print(df["City"].value_counts().head(10))  # Top 10 cities

print("\n Descriptive Analysis Completed!")
