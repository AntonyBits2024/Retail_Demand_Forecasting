# Week 2 – Data Analysis Plan and Findings

## Dataset Overview

The dataset used for this analysis contains **2,000 rows and 22 columns**, with **no missing values**.

The target variable for the forecasting task is:

**Daily_Units_Sold**

Since the dataset is complete and contains multiple feature categories (pricing, store attributes, external factors, and inventory variables), it provides a good foundation for performing exploratory data analysis (EDA) and preparing features for demand forecasting.


# Objectives of Week-2 Analysis

The main objectives of the second week of the project were:

- Perform exploratory data analysis to understand the dataset.
- Analyze the behavior of the target variable.
- Determine whether additional features may be needed.
- Examine relationships between variables using correlation and feature importance analysis.
- Investigate multicollinearity between predictors.
- Apply normalization and standardization where appropriate.
- Use Principal Component Analysis (PCA) to derive new high-variance features without removing the original variables.

Importantly, the project requirement specifies that **no existing features should be removed**, so all original variables are retained throughout the analysis.


# Structure of the Analysis

The notebook analysis is organized into the following sections.


# 1. Target Variable Analysis

The first step is to analyze the distribution of the target variable **Daily_Units_Sold**.

### Analyses Performed

- Summary statistics (mean, median, standard deviation)
- Histogram visualization
- Boxplot for outlier detection
- Demand variation across categories and stores
- Time-based demand patterns

### Observations

The distribution of **Daily_Units_Sold** appears reasonably balanced.

- Mean demand ≈ **112 units**
- Median demand ≈ **113 units**
- Standard deviation ≈ **28 units**

The histogram shows that most demand values fall between **90 and 140 units**, suggesting a stable demand distribution.

The boxplot indicates a few extreme values, but these likely represent valid demand fluctuations rather than data errors, since retail sales naturally vary due to promotions, weather, and customer traffic.

Therefore, the target variable **does not require outlier removal** at this stage.


# 2. Exploratory Data Analysis of Predictor Variables

To better understand the dataset, predictor variables were grouped into logical categories.

## Time Features

- Date
- DayOfWeek
- Month
- Year
- Is_Weekend
- Is_Holiday

## Pricing Features

- Base_Price
- Discount_Percentage
- Current_Price
- Competitor_Price

## Store and Product Features

- Store_ID
- Store_Type
- Product_ID
- Category

## External Factors

- Footfall_Index
- Avg_Temperature
- Rainfall_mm
- Social_Media_Sentiment

## Inventory and Supply Variables

- Lead_Time_Days
- Safety_Stock_Level
- Stock_On_Hand

This grouping allowed the analysis to examine how different operational and environmental factors influence product demand.


# 3. Standardization and Normalization

Both **standardization** and **normalization** techniques were considered during the analysis.

## Standardization

Standardization using **StandardScaler** was applied to numerical variables before performing PCA.

This transformation converts variables to:
mean = 0
standard deviation = 1

Standardization is important because many machine learning algorithms assume features are centered and scaled similarly.

## Normalization

Normalization (such as **MinMax scaling**) converts variables to a **0–1 range**.

This technique is useful when comparing variables with very different scales, but for **PCA analysis**, standardization is generally preferred because PCA relies on variance.


# 4. Correlation Analysis

A correlation matrix was generated to understand relationships between predictors and the target variable.

## Key Observations

Several variables show meaningful relationships with **Daily_Units_Sold**:

- **Current_Price** shows a strong negative relationship with demand.
- **Base_Price** and **Competitor_Price** also exhibit negative relationships.
- **Footfall_Index** shows a positive relationship, indicating that higher store traffic increases sales.
- **Discount_Percentage** positively influences demand.
- **Social_Media_Sentiment** shows a mild positive relationship with sales.

These findings are consistent with expected retail behavior:

- Higher prices reduce demand
- Discounts increase demand
- Higher store traffic leads to more purchases


# 5. Multicollinearity Analysis

Variance Inflation Factor (**VIF**) was used to detect multicollinearity among predictors.

## Observations

Several pricing variables exhibit high VIF values:

- **Base_Price**
- **Current_Price**
- **Competitor_Price**

This is expected because **Current_Price is derived from Base_Price and Discount_Percentage**, which creates natural dependence between these variables.

Additionally, the **Year variable shows extremely high VIF** because the dataset contains only a single year (2023), making it effectively constant.

Although multicollinearity exists, the project requirement specifies that **features should not be dropped**, so all variables are retained.


# 6. Feature Importance Analysis

Feature importance was evaluated using multiple approaches.

## Methods Used

- Correlation analysis
- Random Forest feature importance
- Permutation importance

Using multiple techniques helps avoid bias from relying on a single metric.

### Random Forest Feature Importance

The Random Forest model identified the most influential features:

- **Current_Price**
- **Footfall_Index**
- **Social_Media_Sentiment**

These features contribute the most to predicting daily sales.

### Permutation Feature Importance

Permutation importance confirmed the Random Forest findings.

When key features such as **Current_Price** or **Footfall_Index** were shuffled, the model performance dropped significantly.

This indicates that these variables contain strong predictive information.


# 7. Principal Component Analysis (PCA)

Principal Component Analysis was applied to identify latent structures in the data and generate new derived features.

PCA decomposes the dataset into orthogonal components that capture the maximum variance.

The first few principal components appear to represent combinations of:

- pricing variables
- temporal patterns
- operational variables

Because the project requires that **existing features should not be removed**, PCA components were **added as additional derived features** rather than replacing original variables.

These new features may improve predictive performance in later modeling stages.


# Are Additional Features Needed?

The current dataset already contains strong predictors of retail demand, including:

- pricing variables
- store traffic indicators
- external factors such as weather and sentiment
- inventory levels

However, real-world retail forecasting systems typically incorporate additional features.


# Additional Data That Could Improve Forecasting

## Promotion Campaign Data

- Promotion_Flag
- Promotion_Type
- Marketing_Spend

Discount percentage alone does not capture the full effect of marketing campaigns.

## Extended Calendar Data

- festival indicators
- payday effects
- school vacation periods
- local events

Retail demand often shifts due to calendar behavior beyond simple holidays.

## Product Lifecycle Data

- Launch_Date
- Product_Age
- Seasonal_Product_Flag

Demand patterns differ for new products compared to mature ones.

## Sales Channel Data

- online vs in-store sales
- app traffic
- website visits

Modern retail is increasingly **omnichannel**.

## Supply Chain Reliability

- Backorder_Flag
- Supplier_Delay_Days
- Fill_Rate

Inventory optimization depends on supplier reliability as well as demand.

## Customer Behavior Data

- loyalty program usage
- repeat purchase rate
- basket size

Retail stakeholders often want insights into **who is purchasing**, not just **how much is sold**.


# What Stakeholders Typically Ask

In real retail environments, stakeholders rarely ask directly about **feature importance**.

Instead, they ask operational questions such as:

- Which variables drive product demand the most?
- Are discounts increasing sales enough to justify promotions?
- Which stores are at risk of stockouts?
- Which products require higher safety stock?
- Which additional data should we start collecting?

Therefore, the purpose of Week-2 analysis is not only to explore data but also to **connect analytical findings with real business decisions**.


# Python Libraries Used in the Analysis

## Core Data Analysis

- pandas
- numpy
- matplotlib
- seaborn

These libraries were used for **data inspection and visualization**.

## Statistical Analysis

- scipy
- statsmodels

Statsmodels was used particularly for:

- regression-style diagnostics
- variance inflation factor (VIF)

## Machine Learning and Feature Analysis

- scikit-learn

Used for:

- preprocessing
- scaling
- train/test split
- Random Forest models
- permutation importance
- PCA

## Explainability

- SHAP

SHAP helps interpret model predictions by explaining how each feature contributes to predictions.


# Why These Libraries Were Used and Justification

| Category | Library Used | Purpose in the Project | Common Alternatives | Why This Library Was Chosen |
|--------|--------|--------|--------|--------|
| Data Handling | pandas | Loading, cleaning, filtering, and analyzing tabular data | Polars, Dask | Pandas is the most widely used library for structured datasets and is easier for exploratory analysis |
| Numerical Computation | NumPy | Mathematical operations and efficient array processing | CuPy, JAX | NumPy is the foundational numerical library used by most scientific Python tools |
| Visualization | Matplotlib | Creating graphs such as histograms and distribution plots | Plotly, Bokeh | Produces stable static charts suitable for analysis reports |
| Statistical Visualization | Seaborn | Boxplots, correlation heatmaps, statistical plots | Altair, Plotly | Built on top of Matplotlib and simplifies statistical visualizations |
| Scientific Computation | SciPy | Mathematical and statistical routines | SymPy | Provides optimized scientific computing functions used in data analysis |
| Statistical Diagnostics | Statsmodels | Regression diagnostics and Variance Inflation Factor (VIF) for multicollinearity | scikit-learn regression tools | Offers deeper statistical interpretation and diagnostic tools |
| Machine Learning | Scikit-learn | Preprocessing, scaling, train/test split, Random Forest, permutation importance, PCA | XGBoost, LightGBM, CatBoost | Provides a complete and consistent machine learning toolkit suitable for beginners |
| Explainability | SHAP | Explains how each feature contributes to predictions | LIME, ELI5 | Provides consistent and theoretically grounded feature contribution explanations |


# Explanation

The selected libraries represent the **standard Python data science ecosystem**.

- Pandas and NumPy handle **data manipulation and numerical computation**.
- Matplotlib and Seaborn provide **visualization capabilities for exploratory analysis**.
- SciPy and Statsmodels support **statistical diagnostics such as multicollinearity detection through VIF**.
- Scikit-learn provides a **unified machine learning framework for preprocessing, modeling, feature importance, and PCA**.
- SHAP is used for **model explainability by showing how individual features influence predictions**.

Although alternative libraries exist, the chosen libraries were preferred because they are **widely used, beginner-friendly, well-documented, and sufficient for exploratory analysis and feature evaluation tasks**.


# The Notebook Structure

The completed notebook is organized into the following sections:

- Load and inspect dataset
- Target variable analysis
- Exploratory analysis of predictors
- Standardization and normalization
- Correlation analysis
- Multicollinearity analysis
- Feature importance analysis
- PCA-based feature generation
- Time-based demand analysis
- Category-level demand analysis
- Store-level demand analysis
- Final insights and findings


# Final Conclusion

The dataset provides a strong foundation for building a **retail demand forecasting model**.

Pricing variables, customer traffic indicators, and external factors all show meaningful relationships with sales.

Feature importance analysis indicates that **Current_Price, Footfall_Index, and Social_Media_Sentiment** are among the strongest predictors of demand.

Although multicollinearity exists among pricing variables, **all features are retained in accordance with the project requirement**.

Principal Component Analysis was used to **generate additional derived features without removing original variables**.

Overall, the dataset is suitable for further modeling work. However, incorporating additional real-world variables such as **promotion campaigns, product lifecycle indicators, customer behavior metrics, and supply chain reliability data** could further improve forecasting accuracy.
