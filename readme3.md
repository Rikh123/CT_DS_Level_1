# 📍 Task 3: Geospatial Analysis  

## 📝 Objective  
This task focuses on analyzing restaurant locations using latitude and longitude data. The goal is to:  
- Visualize restaurant locations on an interactive map.  
- Analyze the distribution of restaurants across different cities and countries.  
- Determine if there is any correlation between a restaurant’s location and its rating.  

## 📂 Files  
- `Task3.py` → Python script performing geospatial analysis.  
- `Restaurant_Locations_Map.html` → Interactive map displaying restaurant locations.  
- `Cleaned_Dataset_Task1.csv` → Preprocessed dataset used for analysis.  

## 📊 Analysis Performed  
### 1️⃣ **Visualizing Restaurant Locations on a Map**  
- Used **Folium** to create an **interactive map**.  
- Marked each restaurant’s location using **latitude and longitude**.  
- Applied color coding:  
  - **Blue** for restaurants with a rating of **4.0 and above**.  
  - **Red** for restaurants with a rating below **4.0**.  
- The map is saved as `Restaurant_Locations_Map.html`.  

### 2️⃣ **Distribution of Restaurants**  
- **Top 10 cities** with the most restaurants plotted using a bar chart.  
- **Top 10 countries** with the most restaurants plotted using another bar chart.  

### 3️⃣ **Correlation Between Location and Rating**  
- Created a **scatter plot** to visualize how restaurant locations relate to ratings.  
- Computed a **correlation matrix** to check if **longitude** or **latitude** impacts ratings.  

## 🔍 Key Findings  
- Most restaurants are concentrated in a few major cities.  
- Some cuisines dominate in specific regions.  
- The correlation matrix showed **weak negative correlations** between location and rating, meaning location alone does not strongly influence ratings.  

##  How to Run  
1. Ensure you have the necessary libraries installed:  
   ```bash
   pip install pandas numpy matplotlib seaborn folium
2. To run it
   ```bash
    python Task3.py
