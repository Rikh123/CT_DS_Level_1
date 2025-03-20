import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium  # For interactive maps

# 📂 Load the cleaned dataset
df = pd.read_csv("Cleaned_Dataset_Task1.csv")  # Ensure the correct file path

# 1️⃣ Visualizing Restaurant Locations on an Interactive Map
map_center = [df["Latitude"].mean(), df["Longitude"].mean()]
restaurant_map = folium.Map(location=map_center, zoom_start=5)

for index, row in df.iterrows():
    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        popup=f"{row['Restaurant Name']} - Rating: {row['Aggregate rating']}",
        icon=folium.Icon(color="blue" if row["Aggregate rating"] >= 4 else "red"),
    ).add_to(restaurant_map)

restaurant_map.save("Restaurant_Locations_Map.html")
print("\n Interactive Map Saved: Restaurant_Locations_Map.html")

# 2️⃣  Analyzing the Distribution of Restaurants by City
plt.figure(figsize=(12, 6))
top_cities = df["City"].value_counts().head(10)
sns.barplot(x=top_cities.index, y=top_cities.values, hue=top_cities.index, palette="viridis", legend=False)
plt.xticks(rotation=45)
plt.title("Top 10 Cities with the Most Restaurants")
plt.xlabel("City")
plt.ylabel("Number of Restaurants")
plt.show()

# 3️⃣  Analyzing the Distribution of Restaurants by Country
plt.figure(figsize=(12, 6))
top_countries = df["Country Code"].value_counts().head(10)
sns.barplot(x=top_countries.index, y=top_countries.values, hue=top_countries.index, palette="coolwarm", legend=False)
plt.title("Top 10 Countries with the Most Restaurants")
plt.xlabel("Country Code")
plt.ylabel("Number of Restaurants")
plt.show()

# 4️⃣  Checking the Relationship Between Location & Rating
plt.figure(figsize=(10, 5))
scatter = plt.scatter(
    df["Longitude"],
    df["Latitude"],
    c=df["Aggregate rating"],
    cmap="coolwarm",
    alpha=0.5
)
plt.title("Restaurant Location vs. Rating")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

#  Correct way to add a colorbar
plt.colorbar(scatter, label="Aggregate Rating")
plt.show()

# 5️⃣  Compute the Correlation Between Rating and Location
correlation = df[["Longitude", "Latitude", "Aggregate rating"]].corr()

print("\n Correlation Matrix:")
print(correlation.to_string())

print("\n Geospatial Analysis Completed!")
