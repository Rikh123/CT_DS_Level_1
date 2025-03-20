#  Import necessary libraries
import pandas as pd  # For data manipulation and analysis
import numpy as np  # For numerical operations
import matplotlib.pyplot as plt  # For visualization
import seaborn as sns  # For advanced data visualization

#  Load the dataset
df = pd.read_csv("Dataset .csv")  

# 1️⃣ Check the number of rows and columns in the dataset
print(f"Dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")

# 2️⃣ Check for missing values in each column
missing_values = df.isnull().sum()  # Count missing (NaN) values for each column
print("\nMissing Values in Each Column:\n", missing_values)

#  Replace "0.0" ratings with NaN (assuming "0.0" means "Not Rated")
df["Aggregate rating"] = df["Aggregate rating"].replace(0.0, np.nan)

#  Handle missing values:
# - Categorical columns (text data) → Fill with mode (most frequent value)
# - "Aggregate rating" (numerical) → Fill with median (better for outliers)
# - Other numerical columns → Fill with mean
for column in df.columns:
    if df[column].dtype == 'object':  # If the column contains text data (categorical)
        df[column] = df[column].fillna(df[column].mode()[0])  # Fill with mode (most common value)
    elif column == "Aggregate rating":
        df[column] = df[column].fillna(df[column].median())  # Fill with median (to handle skewed data)
    else:
        df[column] = df[column].fillna(df[column].mean())  # Fill numerical columns with mean

# 3️⃣ Print data types before conversion
print("\nData Types Before Conversion:\n", df.dtypes)

#  Convert categorical columns with 'Yes/No' values to Boolean (True/False)
bool_cols = ["Has Table booking", "Has Online delivery", "Is delivering now", "Switch to order menu"]
df[bool_cols] = df[bool_cols].apply(lambda x: x.map({"Yes": True, "No": False}))  # Convert Yes → True, No → False

#  Ensure "Aggregate rating" is treated as a numerical (float) column
df["Aggregate rating"] = pd.to_numeric(df["Aggregate rating"], errors="coerce")

# Print data types after conversion
print("\nData Types After Conversion:\n", df.dtypes)

# 4️⃣ Visualize the distribution of "Aggregate rating"
plt.figure(figsize=(8, 5))  # Set figure size
sns.histplot(df["Aggregate rating"].dropna(), bins=10, kde=True, color="blue")  # Plot histogram, remove NaN values
plt.title("Distribution of Aggregate Rating")  # Set title
plt.xlabel("Aggregate Rating")  # Set x-axis label
plt.ylabel("Count")  # Set y-axis label
plt.grid(True)  # Show grid for better readability
plt.show()

# 5️⃣ Check if ratings are balanced (or if some ratings appear much more frequently)
rating_counts = df["Aggregate rating"].value_counts().sort_index()  # Count occurrences of each rating
print("\nRating Value Counts:\n", rating_counts)

#  Plot class distribution of ratings
plt.figure(figsize=(12, 6))  # Set figure size
sns.countplot(x=df["Aggregate rating"], order=sorted(df["Aggregate rating"].unique()), 
              hue=df["Aggregate rating"], palette="viridis", legend=False)  # Count plot

plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.title("Class Distribution of Aggregate Ratings")  # Set title
plt.xlabel("Aggregate Rating")  # Set x-axis label
plt.ylabel("Count")  # Set y-axis label
plt.show()

#  Save the cleaned dataset to a new CSV file (optional)
df.to_csv("Cleaned_Dataset_Task1.csv", index=False)  # Save without index column

print("\n✅ Data cleaning and exploration completed successfully!")  # Success message
