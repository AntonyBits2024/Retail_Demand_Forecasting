# Feature Engineering & Baseline Model Building
**BITS WILP — AI/ML Capstone | Retail Demand Forecasting**  
*Mentor Presentation Document | 2026*

---

## 1. Task Objective

This week's task focuses on two core deliverables that bridge raw data to predictive insight:

| Deliverable | Description |
|---|---|
| **Feature Engineering** | Converting 58 raw columns into 24 new meaningful features across 5 engineering strategies |
| **Baseline Model Building** | Training and comparing 5 models from simple regression to ensemble methods |

---

## 2. Dataset Recap

| Dimension | Value | Implication |
|---|---|---|
| Total records | 2,000 rows | Sufficient for baseline modelling; limited for deep time-series |
| Original features | 58 columns | Rich multi-domain dataset (temporal, pricing, inventory, customer) |
| Target variable | Daily_Units_Sold | Range 17–204 · Mean 112 · Std 28.6 · Skew –0.15 (near-normal) |
| Time coverage | 2023 only (363 dates) | Single year — no multi-year trend; use month/quarter for seasonality |
| Data quality | 2 columns with nulls | Festival_Type (97% null), Promotion_Type (28% null) — both imputable |
| Leakage features | 5 high-correlation columns | In_Store_Sales, Online_Sales, Website_Visits, App_Traffic, Cust_Purchases |

> **Key Point:** Near-normal distribution of target (skew = –0.15) means no log transformation is needed. Regression models can be applied directly, reducing modelling complexity.

---

## 3. Critical Finding — Data Leakage Identification

Before engineering any features, it is essential to identify and remove **leakage features** — variables that are correlated with the target but cannot be known at the time of making a forecast.

| Leakage Feature | Correlation | Why It's Leakage |
|---|---|---|
| In_Store_Sales_Units | r = 0.907 | This IS part of daily demand — recorded simultaneously, not beforehand |
| Online_Sales_Units | r = 0.564 | A component of total units sold — consequence, not predictor |
| Website_Visits | r = 0.564 | Visits happen as customers buy — consequence of demand, not cause |
| App_Traffic_Index | r = 0.564 | Same pattern as website visits — concurrent with purchase event |
| No_of_Customer_Purchases | r = 0.526 | Count of transactions = realised demand, not forecast input |


---

## 4. Feature Engineering — 5 Strategies Applied

Starting from the 58 original columns (after removing leakage and metadata), **24 new features** were engineered across 5 domain-driven strategies. The final feature matrix is **2,000 × 61**.

---

### 4.1 Imputation Strategy

Two columns had meaningful nulls that required domain-aware imputation rather than dropping:

| Column | Null % | Strategy | Rationale |
|---|---|---|---|
| Festival_Type | 97.25% | Fill → `'No_Festival'` | Null means no festival active. Preserves 55 festival rows as signal |
| Festival_Name | 97.25% | Fill → `'None'` | Same logic — encodes absence of festival as a category |
| Promotion_Type | 27.65% | Fill → `'No_Promotion'` | 553 nulls = no active promotion. New category, not mean imputation |

---

### 4.2 Pricing & Competitive Features

Four price-derived features were created to capture competitive positioning and actual discount effectiveness:

```python
# Competitive pressure
df['price_gap']          = df['Current_Price'] - df['Competitor_Price']       # corr = +0.282
df['price_ratio']        = df['Current_Price'] / df['Competitor_Price']        # corr = -0.220

# Actual discount applied vs stated base
df['effective_discount'] = (df['Base_Price'] - df['Current_Price']) / df['Base_Price']  # corr = +0.234

# Profitability
df['margin_abs']         = df['Current_Price'] - df['Unit_Cost']              # corr = -0.364
```

> **Insight:** `price_gap` (r = 0.282) reveals that when our price is significantly above the competitor's price, demand decreases — a clean competitive pricing signal missing from the raw data.

---

### 4.3 Interaction Features

Interaction features capture joint effects that neither variable expresses alone — the hallmark of good feature engineering:

```python
# Promotion effectiveness (discount only matters when promo is active)
df['discount_x_promo']             = df['Discount_Percentage'] * df['Promo_Flag_num']        # corr = +0.225

# Customer engagement intensity (loyalty × sentiment)
df['loyalty_x_sentiment']          = df['Loyalty_Program_Usage_Count'] * df['Social_Media_Sentiment']
#                                                                                              corr = +0.415 ← strongest engineered feature

# Store traffic × basket size (revenue potential proxy)
df['basket_x_footfall']            = df['Avg_Basket_Size'] * df['Footfall_Index']            # corr = +0.242

# Competitor response to our pricing
df['competitor_promo_x_price_gap'] = df['Competitor_Promo_Flag'] * df['price_gap']           # corr = +0.154
```

---

### 4.4 Temporal Features

| Feature | Logic | Correlation | Business Meaning |
|---|---|---|---|
| Quarter | Date → Q1/Q2/Q3/Q4 | +0.004 | Broad seasonal marker for annual planning |
| Is_Summer | Month ∈ {6, 7, 8} | +0.029 | Summer buying behaviour flag |
| Is_MonthEnd | Day ≥ 25 | +0.028 | Payday/salary-driven end-of-month surge |
| WeekOfYear | ISO week number | +0.007 | Granular seasonality for weekly forecasts |

---

### 4.5 Inventory & Supply Chain Features

```python
# How full are shelves relative to capacity?
df['stock_utilisation']   = df['Stock_On_Hand'] / df['Shelf_Capacity']             # corr = -0.008

# How many days of average demand do we have in stock?
df['stock_vs_safety']     = df['Stock_On_Hand'] / df['Safety_Stock_Level']         # corr = -0.001

# Google Trends momentum (week-over-week change)
df['google_trend_change'] = df['Google_Trends_Current_Wk'] - df['Google_Trends_Lag_1w']  # corr = +0.027
```

> **Note:** Inventory features show low individual correlation. This is expected — low stock constrains sales (not demand), so it suppresses measured units sold. In a production system, these features would be critical for supply-constrained forecasting.

---

## 5. Categorical Encoding

10 categorical columns were encoded. Strategy was chosen based on cardinality and model type:

| Column | Unique Values | Encoding | Reason |
|---|---|---|---|
| Store_Type | 2 (Urban/Rural) | Label Encoding | Binary — 0/1 is sufficient |
| Brand_Tier | 3 (Budget/Mid/Premium) | Label Encoding | Ordinal relationship exists |
| Category | 5 | Label Encoding | Low cardinality; tree models handle well |
| Festival_Type | 4 (incl. No_Festival) | Label Encoding | Low cardinality |
| Promotion_Type | 5 (incl. No_Promotion) | Label Encoding | Low cardinality |
| Seasonal_Product_Flag | 2 (Y/N) | Label Encoding | Binary flag |
| Backorder_Flag | 2 (Y/N) | Label Encoding | Binary flag |
| Promotional_Campaign_Flag | 2 (Y/N) | Numeric (0/1) | Used in interaction features |
| Competitor_Promotion_Flag | 2 (Y/N) | Numeric (0/1) | Used in interaction features |
| Festival_Name | 9 | Label Encoding | For tree models; use OHE for linear |

---

## 6. Baseline Model Building — Results

Five models were trained on the engineered feature matrix (2,000 × 61 after removing leakage and metadata). **80/20 train/test split** with `random_state=42`. **5-fold cross-validation** was used for generalisation assessment.

---

### 6.1 Model Comparison Table

| Model | RMSE ↓ | MAE ↓ | MAPE ↓ | WAPE ↓ | R² ↑ | CV-RMSE |
|---|---|---|---|---|---|---|
| Linear Regression *(baseline)* | 10.65 | 8.57 | 8.10% | 7.54% | 0.856 | 10.05 |
| **Ridge Regression (α=10) ⭐** | **10.57** | **8.48** | **8.01%** | **7.46%** | **0.858** | 10.06 |
| Lasso Regression (α=1) | 10.60 | 8.55 | 8.06% | 7.52% | 0.857 | 10.48 |
| Random Forest (100 trees) | 11.16 | 9.05 | 8.58% | 7.96% | 0.841 | 11.09 |
| Gradient Boosting (200/lr=0.05) | 10.69 | 8.61 | 8.14% | 7.58% | 0.855 | 10.49 |

> **Key Result:** Ridge Regression achieves the best RMSE (10.57) and R² (0.858) — a strong baseline. All models exceed R² = 0.84, confirming the feature set is highly predictive. Industry benchmark for good demand forecasting MAPE is 10–15%; our baseline already achieves **8.01%**.

---

### 6.2 Before vs After Feature Engineering

| Model | RMSE Before FE | RMSE After FE | Improvement |
|---|---|---|---|
| Linear Regression | 10.66 | 10.63 | 0.3% |
| Ridge Regression | 10.63 | 10.56 | **0.7% ← best gain** |
| Random Forest | 11.27 | 11.20 | 0.6% |


---

### 6.3 Lasso Feature Selection Result

Lasso (L1 regularisation) with α=1 performs automatic feature selection by shrinking irrelevant coefficients to zero:

| Result | Count |
|---|---|
| Total features in matrix | 61 |
| Features selected by Lasso (non-zero) | **9** |
| Features eliminated (zeroed out) | 52 |

The 9 features Lasso retained, ranked by standardised coefficient magnitude:

| Rank | Feature | Std. Coefficient | Category |
|---|---|---|---|
| 1 | Current_Price | 20.74 | Pricing |
| 2 | Footfall_Index | 10.71 | Customer |
| 3 | Social_Media_Sentiment | 3.65 | External Signal |
| 4 | **loyalty_x_sentiment** | **1.64** | **Engineered Interaction ★** |
| 5 | Is_Weekend | 1.33 | Temporal |
| 6 | **basket_x_footfall** | **1.08** | **Engineered Interaction ★** |
| 7 | Loyalty_Program_Usage_Count | 0.57 | Customer |
| 8 | Competitor_Price | 0.18 | Pricing |
| 9 | Unit_Cost | 0.14 | Pricing |

> **Insight:** 2 of the top 6 Lasso-selected features (`loyalty_x_sentiment`, `basket_x_footfall`) are engineered interaction features — confirming that feature engineering added genuine predictive signal beyond the raw data.

---

## 7. Feature Importance Analysis (Random Forest)

| Rank | Feature | Importance % | Type |
|---|---|---|---|
| 1 | Current_Price | 60.9% | Raw — pricing |
| 2 | Footfall_Index | 19.4% | Raw — customer traffic |
| 3 | **loyalty_x_sentiment** | **2.9%** | **Engineered ★** |
| 4 | Social_Media_Sentiment | 2.4% | Raw — external |
| 5 | Competitor_Price | 2.1% | Raw — pricing |
| 6 | Base_Price | 1.5% | Raw — pricing |
| 7 | **basket_x_footfall** | **0.5%** | **Engineered ★** |
| 8–20 | Remaining 48 features | ~10.3% | Mixed |


---

## 8. Key Talking Points for Mentor

### 8.1 What Worked Well

1. **Leakage identification:** Proactively identified and removed 5 high-correlation leakage features before any modelling — prevents production failure.
2. **Interaction feature discovery:** `loyalty_x_sentiment` (r = 0.415) outperforms both raw features individually and is confirmed important by both RF and Lasso.
3. **Strong baseline performance:** 8.01% MAPE on first pass beats the industry benchmark of 10–15%. All models R² > 0.84.
4. **Lasso as feature selector:** Used Lasso not just as a model but as a principled feature selection tool — 52 of 61 features zeroed out, identifying the 9 core predictors.
5. **Domain-aware imputation:** Festival nulls imputed as `'No_Festival'` (not dropped, not mean-filled) — a business logic decision, not a mechanical one.

---

### 8.2 Challenges & How They Were Addressed

1. **Challenge — Current_Price dominance (61% importance):** Will investigate using Partial Dependence Plots (PDP) next week to confirm causal direction and rule out proxy effects.
2. **Challenge — Single-year data limits time-series modelling:** Mitigated by engineering temporal signals (Quarter, Is_Summer, Is_MonthEnd) from calendar attributes within the available year.
3. **Challenge — Tree models underperforming linear:** With 2,000 rows and two dominant linear predictors, this is expected. Will test XGBoost with hyperparameter tuning and early stopping in the next iteration.

---

### 8.3 Next Steps Proposed

1. **XGBoost / LightGBM with hyperparameter tuning** — expected to outperform current baseline with proper tuning (`learning_rate`, `max_depth`, early stopping).
2. **SHAP explainability** — apply `shap.TreeExplainer` to Random Forest for individual-level prediction explanations; critical for business trust.
3. **Target encoding for Category & Festival_Name** — replace label encoding with cross-validated target encoding for linear models to better capture the demand mean per group.
4. **Partial Dependence Plots for Current_Price** — confirm monotonic price-demand relationship and investigate whether dominance is genuine or proxy for product tier.
5. **Category-stratified models** — separate models per product category may outperform the single global baseline.

---

## 9. Evaluation Metrics — Reference

| Metric | Formula | Best Value | Interpretation |
|---|---|---|---|
| RMSE | √(Σ(y−ŷ)²/n) | 10.57 units | Penalises large errors. Good for inventory planning |
| MAE | mean(\|y−ŷ\|) | 8.48 units | Avg absolute error. Easy for ops teams to understand |
| MAPE | mean(\|y−ŷ\|/y) × 100 | 8.01% | Business-friendly. "We forecast within 8% on average" |
| WAPE | Σ\|y−ŷ\|/Σy × 100 | 7.46% | Weighted MAPE — preferred in retail; down-weights low-volume SKUs |
| R² | 1 − SS_res/SS_tot | 0.858 | 85.8% of demand variance explained by our features |
| CV-RMSE | 5-fold mean RMSE | 10.06 | Generalisation check. Close to test RMSE → no overfitting |

### Industry Benchmarks for Retail Demand Forecasting

| Rating | MAPE Range | Our Result |
|---|---|---|
| Excellent | < 10% | **8.01% ✓** |
| Good | 10–15% | Industry average |
| Needs improvement | > 20% | Requires major rework |

---

