# Restaurant Sales Analytics - Dashboard Portfolio

An operational performance dashboard designed for multi-unit restaurant operators to track gross revenue, transaction volumes, dining check sizes, and category menu mixes across locations.

> [!NOTE]
> **Disclaimer:** None of the data used in this report is sourced from private or active customers. All files, tables, and records correspond to dummy datasets that are generally and publicly available on the internet for training and development purposes.

---

## 📸 Dashboard Preview

![Restaurant Sales Analytics Dashboard](Resturant%20Analystics.png)

---

## 💼 Business Impact & Insights

The **Restaurant Sales Analytics** dashboard provides restaurant managers and corporate executives with the financial intelligence needed to improve store-level performance:

* **Upselling and Average Ticket Optimization (AOV):** Monitoring the **Average Order Value (AOV)** helps evaluate store staff's upselling effectiveness. A low AOV triggers targeted staff training on promoting high-margin add-ons (beverages, desserts).
* **Menu Engineering & Selection Share:** By mapping the **Category Share %** of sales, the kitchen and purchasing departments can identify popular, high-volume categories vs. slow-moving, low-margin products. This helps optimize menu pricing, reduce food waste, and streamline inventory.
* **Geographical Resource Allocation:** The **Location Share %** metric highlights underperforming branches. Executive management can use these insights to optimize marketing spend or reallocate operational budgets from high-performing locations to branches that need support.
* **Seasonal Sales Adjustments:** Time-intelligence KPIs (MTD, YTD, and YoY %) reveal seasonal transaction peaks, allowing managers to plan staffing levels and inventory orders in advance to avoid food spoilage or stockouts.

---

## 🔮 Future Scope & Enhancements

To take this hospitality analytics solution further, the following extensions are planned:

* **Predictive Inventory Forecasting:** Integrate POS data with local weather and public event calendars using machine learning models to forecast daily customer foot traffic, helping kitchens prepare the exact amount of ingredients needed and reduce organic waste.
* **Labor Cost Integration:** Import employee shift logs and hourly wages to calculate labor cost percentages against sales curves. This helps store managers schedule staff dynamically during peak hours and cut back on idle hours.
* **Feedback Sentiment Correlation:** Link POS transaction IDs with customer satisfaction scores from Google Reviews, Yelp, or receipt-based surveys to check if menu category sales volumes correlate directly with customer happiness.
* **Smart Purchase Ordering:** Automate replenishment emails to suppliers via Power Automate when food category quantities drop below dynamic safety thresholds.

---

## 📊 Overview & Data Model

The **Restaurant Sales Analytics** report translates raw daily transaction logs into dynamic business intelligence.

### Data Sources & Schema
* **Source Datasets:** Local CSV files:
  * [Food_Beverage_Sales_2023_2024.csv](Food_Beverage_Sales_2023_2024.csv) (Contains core transactions)
  * [food_categories.csv](food_categories.csv) (Maintains categories metadata)
* **Schema Design:** Optimized **Star Schema**
  * **Fact Table:** `FactSales` (Houses transactional fields: date, category, location, quantity, unit price, and total sales amount).
  * **Dimension Tables:** `DimCategories` (Maps category names to descriptions and image URLs), `DimDate` (Dynamically generated calendar table).
* **Granularity:** Daily transaction level, aggregated by product category and restaurant location.

---

## 📑 Dashboard Pages & Visuals

The report features a unified **Home** interface designed for high-level operations monitoring:
* **Objective:** Track store revenue health, ticket averages, and seasonal sales shifts.
* **Core Metrics Managed:** Total Sales, Transactions count, Average Order Value (AOV), Sales MTD/QTD/YTD, YoY Growth rate %, Category Share %, and Location Share %.
* **Key Visuals:** Clustered columns comparing current year sales to previous year, multi-row KPI summaries, location/category filter slicers, and trend matrices.

---

## ⚡ ETL Transformations & Power Query

The data ingestion pipeline, defined in M Script, executes the following data engineering operations:
1. **Source Loading:** Imports raw sales transaction records and menu category logs using `Csv.Document()`.
2. **Promoting Headers:** Promoting structural headers to database columns.
3. **Data Type Conversions:** Standardizing transactional fields (e.g., date formats, integer numbers for quantities, and decimals for sales values).
4. **Dynamic Calendar Generator (`DimDate`):** 
   A custom M function scans `FactSales` to find the exact start and end dates of sales records, generates a continuous, gap-free list of dates, and derives columns for Year, Month, Month Number (for sorting), Quarter, Day, and Day Name. This ensures that time-intelligence functions like `SAMEPERIODLASTYEAR` compute correctly.
