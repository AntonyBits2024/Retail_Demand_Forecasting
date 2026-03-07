## First Week Task

Main Task : Demand forecasting for Retail Inventory Optimization  
This week we are to explore the stakeholders and what kind of data will align with the stakeholders. What we need to find and figure out.

### **1. Objective of Retail Demand Forecasting**

Retail demand forecasting predicts **future product sales** so companies can optimize inventory levels and avoid:

- **Stockouts** (lost sales)
- **Overstocking** (inventory holding cost)

Inventory optimization aims to determine:

`Optimal\ Inventory = Forecasted\ Demand + Safety\ Stock`

Stakeholders use forecasts to make **procurement, pricing, and logistics decisions**.

### **2. Key Stakeholders in Retail Inventory Forecasting**

- Inventory Managers
- Supply Chain / Procurement Team
- Store Operations Team
- Pricing & Marketing Teams
- Finance Teams

### **3. Types of Data Used in Real Retail Systems**

Retail demand forecasting requires **multiple categories of data**.

#### **1. Historical Sales Data (Most Important)**

Examples:

- Units sold
- sales transactions
- sales by store

This is the **target variable**.

**Example column in the dataset: `Daily_Units_Sold`**

#### **2. Product Information**

Helps identify product behavior.

Typical fields:

- Product ID
- Product category
- brand
- size/packaging
- product lifecycle stage

**This dataset includes:**

- **`Product_ID`**
- **`Category`**

This is **good but minimal**.

#### **3. Pricing and Promotion Data**

Demand is highly sensitive to price.

Typical features:

- Base price
- Discount
- Promotion campaign
- coupons

This dataset includes:

- `Base_Price`
- `Discount_Percentage`
- `Current_Price`
- `Competitor_Price`

This is **very useful for modeling price elasticity**.

#### **4. Store Information**

Demand varies across locations.

Typical store attributes:

- store location
- store size
- store format (urban / mall / suburban)

This dataset includes:

- `Store_ID`
- `Store_Type`

This is **sufficient for basic modeling**.

#### **5. Customer Traffic Data**

Retailers track store visits.

Example:

- foot traffic
- website visits
- mobile app activity

This dataset includes: `Footfall_Index`

This is **excellent for demand prediction**.

#### **6. External Factors**

External conditions influence demand.

Examples:

- weather
- holidays
- events
- economic indicators

This dataset includes:

- `Avg_Temperature`
- `Rainfall_mm`
- `Is_Holiday`
- `Is_Weekend`

This is **very good contextual data**.

#### **7. Inventory Data**

Used for optimization decisions.

Examples:

- stock available
- reorder point
- supplier lead time

This dataset includes:

- `Lead_Time_Days`
- `Safety_Stock_Level`
- `Stock_On_Hand`

This allows **inventory policy modeling**.

### **4. Is the Provided Dataset Sufficient?**

This dataset has **22 columns and 2000 records**.

It contains:

- Time variables
- Product data
- Pricing data
- Store data
- Weather data
- Social sentiment
- Inventory data

This is **quite comprehensive for an academic dataset**.

However, **real retail datasets contain more information**.

### **5. Important Data Missing From the Dataset**

Several **important real-world factors are missing**.

#### **1. Promotion Campaign Information**

This dataset has **discount percentage**, but it lacks:

- marketing campaign indicator
- advertising spend
- promotion type

Example:

- `Promotion_Type` (BOGO, coupon, clearance)
- `Campaign_Active`
- `Ad_Spend`

Why important:

Promotions can **increase demand by 3–5x**.

#### **2. Customer Segmentation Data**

Retailers track customer demographics.

Examples:

- loyalty program usage
- customer age group
- purchase frequency

Why important:

Customer behavior influences demand patterns.

#### **3. Economic Indicators**

Macroeconomic factors affect retail demand.

Examples:

- inflation rate
- unemployment rate
- consumer confidence index

These are often used in long-term demand forecasting.

#### **4. Product Lifecycle Data**

Products move through stages:

- introduction
- growth
- maturity
- decline

Example data:

- `Product_Age`
- `Launch_Date`
- `Discontinued_Flag`

This is critical for electronics and fashion retail.

#### **5. Supply Chain Disruptions**

Real supply chains experience disruptions.

Examples:

- supplier delays
- shipment disruptions
- logistics constraints

Additional fields could include:

- `Supplier_Reliability`
- `Shipment_Delay_Days`
- `Backorder_Level`

#### **6. Online vs Offline Sales Channels**

Modern retailers have multiple channels.

Examples:

- in-store sales
- online sales
- mobile app orders

Example column:

- `Sales_Channel`

Demand patterns differ by channel.

#### **6. Additional Data We Can Have**

To improve forecasting accuracy, we could request:

| Data Type | Example Fields | Why Needed |
|---|---|---|
| Promotion campaigns | `Promo_Type`, `Campaign_Flag` | promotions strongly affect demand |
| Product lifecycle | `Launch_Date` | demand varies across lifecycle |
| Customer behavior | `Loyalty_Memberships` | predict repeat purchases |
| Economic indicators | `CPI`, inflation | macro demand shifts |
| Supply chain reliability | `Supplier_delay_rate` | affects stock availability |
| Sales channel | Online vs Store | omnichannel retail analysis |

- #### **Demand Forecasting**
- #### **Inventory Management**
- **Target Variable, Start doing EDA analyse (normalized, standardized, causation analysis)**
- **Python Libraries: which will do these**
- **Try to do PDA**

