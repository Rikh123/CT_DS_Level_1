#  Level 1 Task 2: Descriptive Analysis

##  Overview
This task involves performing **descriptive analysis** on a cleaned restaurant dataset. The goal is to calculate basic statistical measures, explore categorical variables, and identify top cuisines and cities.

---

## 📂 Dataset Information
The dataset contains **restaurant-related data**, including:
- **Numerical columns**: Restaurant ID, Average Cost, Ratings, Votes, etc.
- **Categorical columns**: Country Code, City, Cuisines, etc.

---

## 📈 Analysis Performed
### 1️⃣ **Basic Statistics for Numerical Columns**
- Computed **mean, median, standard deviation, min, max, quartiles** for:
  - **Average Cost for Two**
  - **Aggregate Rating**
  - **Votes**
  - **Price Range**
- Identified outliers (e.g., some restaurants have **extremely high costs**).

### 2️⃣ **Exploring Categorical Variables**
- Counted **unique values** for:
  - **Country Code**: 15 unique countries.
  - **City**: 141 different cities.
  - **Cuisines**: 1,825 unique cuisine types.

### 3️⃣ **Identified Popular Cuisines and Cities**
- **Top 10 cuisines** with the highest number of restaurants.
- **Top 10 cities** with the most restaurants (New Delhi ranks highest).

---

##  Key Findings
- **New Delhi has the most restaurants** (5,473).
- **North Indian cuisine is the most popular**, followed by Chinese & Fast Food.
- **Average rating is ~3.43**, indicating most restaurants have a mid-range rating.
- **Average meal cost is ₹1199**, but some high-end restaurants have extreme prices.

---

## 📊 Visualizations (Optional)
To better understand the data, we can use:
- **Histograms** for rating distribution.
- **Bar charts** for top cuisines & cities.
- **Box plots** to identify cost outliers.

---

##  Next Steps
- Perform **correlation analysis** (e.g., does higher cost mean better ratings?).
- Visualize the findings using **Seaborn & Matplotlib**.

---

##  Technologies Used
- **Python (Pandas, NumPy, Seaborn, Matplotlib)** for data analysis and visualization.


