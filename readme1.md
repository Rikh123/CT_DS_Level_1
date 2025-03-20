#  Restaurant Rating Data Exploration & Preprocessing

##  Project Overview
This project focuses on exploring and preprocessing a restaurant dataset to ensure data quality and prepare it for further analysis. The dataset includes restaurant details, locations, ratings, and other relevant attributes.

## 📂 Dataset Information
- **Total Rows:** 9,551  
- **Total Columns:** 21  
- **Key Features:**
  - `Restaurant ID`, `Restaurant Name`, `City`, `Cuisines`, `Aggregate rating`, etc.
  - Boolean attributes: `Has Table booking`, `Has Online delivery`, `Is delivering now`, `Switch to order menu`.
  - Numeric attributes: `Average Cost for two`, `Votes`, `Price range`, etc.

##  Steps Performed

### 1️⃣ Data Loading & Exploration
- Loaded the dataset (`Dataset.csv`).
- Identified the number of rows and columns.
- Checked for missing values in each column.

### 2️⃣ Handling Missing Values
- **Replaced missing categorical values** with **mode** (most frequent value).
- **Replaced missing numerical values** with **mean**, except for `Aggregate rating`, which was filled with the **median** for robustness.
- **Converted "0.0" ratings** to NaN (assuming they mean "Not Rated").

### 3️⃣ Data Type Conversion
- Converted `Yes/No` categorical columns (`Has Table booking`, `Has Online delivery`, etc.) into **boolean** values (`True/False`).
- Ensured numerical columns were of appropriate **integer** or **float** types.

### 4️⃣ Distribution Analysis of `Aggregate rating`
- Plotted a **histogram** to understand the distribution of ratings.
- Identified potential **class imbalance** in restaurant ratings.

### 5️⃣ Data Export
- Saved the cleaned dataset as **`Cleaned_Dataset.csv`**.

## Insights from Analysis
- Some restaurants had an **"Aggregate rating" of 0**, which was treated as **NaN** (Not Rated).
- The majority of restaurants had ratings between **2.5 and 4.5**, with relatively fewer in the extreme ranges.
- A large number of restaurants had **ratings concentrated around 3.4**.

##  How to Run the Script
1. Ensure you have **Python 3.x** installed.
2. Install the required libraries:  
3. To run it 
   ```bash
    Task2.py
