# Internship Project: Data Analysis Report

## Project Context
**System:** Employee Time Sheet System (Analysis of `dataset1.csv`)
**Objective:** Evaluate feature importance, perform Exploratory Data Analysis (EDA), execute Principal Component Analysis (PCA), and identify potential feature engineering needs.

---

## 1. Target Variable Identification
The primary **Target Variable** for this dataset is **`Daily_Units_Sold`**. 
All subsequent analyses focus on identifying how store, product, and external environmental features influence this outcome.

---

## 2. Exploratory Data Analysis (EDA)

### Correlation & Causation Analysis
Based on the correlation matrix, several key relationships were identified:
* **Price Sensitivity:** A strong negative correlation (-0.80) exists between **`Current_Price`** and **`Daily_Units_Sold`**, indicating that price changes are a dominant driver of sales volume.
* **Competitive Impact:** **`Competitor_Price`** (-0.75) similarly impacts sales, suggesting that the system's performance is highly sensitive to market pricing.
* **Footfall Impact:** The **`Footfall_Index`** (0.44) shows a strong positive relationship, proving that store traffic directly translates to higher units sold.
* **Brand Sentiment:** **`Social_Media_Sentiment`** (0.22) has a notable positive impact, suggesting that online brand perception influences purchasing behavior.

### Data Scaling
* **Standardization (`StandardScaler`):** Applied to remove the mean and scale to unit variance. This was essential for the PCA and Random Forest analysis to ensure that high-magnitude features (like `Base_Price`) did not overshadow low-magnitude features (like `Social_Media_Sentiment`).
* **Normalization (`MinMaxScaler`):** Performed to provide a bounded range (0 to 1) for features, which is useful for algorithms sensitive to input scale.

---

## 3. Recommended Python Libraries
For further feature importance and predictive modeling, the following stack is recommended:
* **`scikit-learn`**: Use for `RandomForestRegressor` and `Lasso` (L1) regularization to identify the most significant features.
* **`XGBoost` / `LightGBM`**: These libraries offer superior performance on tabular data and provide built-in `plot_importance` functions.
* **`SHAP` (SHapley Additive exPlanations)**: Best for explaining the impact of specific features on individual predictions.
* **`Seaborn`**: Essential for visualizing multi-collinearity and distribution overlaps.

---

## 4. Principal Component Analysis (PCA)
PCA was executed to derive new features that maximize variance.
* **Component Results:**
    * **PCA1**: Explains ~16.3% of variance.
    * **PCA2**: Explains ~10.0% of variance.
    * **PCA3**: Explains ~6.3% of variance.
* **Integration:** These three components have been added to the dataset as `PCA1`, `PCA2`, and `PCA3`. 
* **Constraint Check:** No original features were dropped; PCA components serve as supplemental high-variance indicators.

---

## 5. Feature Engineering Recommendations
To enhance the predictive power of the model, the following features should be considered:
1.  **Price Gap:** `Current_Price - Competitor_Price` (measures relative market competitiveness).
2.  **Inventory Velocity:** `Stock_On_Hand / Safety_Stock_Level` (identifies stock health).
3.  **Temporal Trends:** 7-day and 30-day rolling averages of `Daily_Units_Sold` to capture seasonality beyond the simple day-of-week.
4.  **Discount Efficiency:** A feature interacting `Discount_Percentage` with `Footfall_Index` to see how effectively promotions drive conversion.

---
