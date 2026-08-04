# Volt Electronic Sales Report - Dashboard Portfolio

An enterprise-grade Power BI dashboard analyzing sales performance, logistics efficiency, customer cohorts, and product return metrics for a regional electronics retail business.

> [!NOTE]
> **Disclaimer:** None of the data used in this report is sourced from private or active customers. All files, tables, and records correspond to dummy datasets that are generally and publicly available on the internet for training and development purposes.

---

## 📸 Dashboard Previews

### 1. Sales Overview Page
![Sales Overview](voltdashboard%20(1).png)

---

### 2. Details by Product Page
![Details by Product](voltdashboard%20(2).png)

---

### 3. Customer Insights Page
![Customer Insights](voltdashboard%20(3).png)

---

### 4. Return Analysis Page
![Return Analysis](voltdashboard%20(4).png)

---

## 💼 Business Impact & Insights

The **Volt Electronic Sales Report** serves as an operational decision-making tool, helping the business optimize inventory, improve customer satisfaction, and protect profit margins:

* **Product Quality & Logistics Control (Return Analysis):** By monitoring **% Orders Returned** and **Total Returns**, supply chain managers can instantly detect surges in defective SKU batches or damage caused by specific courier partners. Minimizing returns saves direct shipping overhead and prevents negative brand reviews.
* **Customer Acquisition Efficiency:** Tracking the **Percent New Customers** allows marketing teams to evaluate customer lifetime value (LTV). If acquisition rates fall below target, it triggers adjustments in digital ad campaigns or promotional offers.
* **Fulfillment Optimization:** Cross-analyzing delivery status with regions helps operations managers identify regional transit delays, allowing them to shift inventory to local hubs to meet customer delivery promises.
* **Basket Size Expansion (Average Purchase Value):** Helps determine if cross-selling and bundling campaigns (e.g. laptop accessories with core laptop purchases) are successfully increasing the overall order size.

---

## 🔮 Future Scope & Enhancements

To expand the business value of this electronics dashboard, the following strategic upgrades are planned:

* **Predictive Churn Modeling:** Integrate Azure Machine Learning to build a churn propensity score for customers based on purchase intervals, support ticket counts, and past return histories, enabling sales teams to run proactive retention campaigns.
* **Logistics API Integration:** Connect real-time GPS coordinates of courier vehicles via REST APIs to dynamically calculate actual shipping delays and show predictive delivery estimates.
* **RLS & Multi-Tenant Security:** Apply dynamic Row-Level Security (RLS) so that Region Managers can only see transaction records, courier performance, and returns related to their specific territories.
* **Automated Refund Integration:** Connect return status approvals to the corporate ERP via Power Automate, allowing low-value returns (e.g., under $50) to process automatic refunds instantly upon a package scan.

---

## 📊 Overview & Data Model

The **Volt Electronic Sales Report** transforms transactional sales records into operational insights. 

### Data Source & Schema
* **Source Dataset:** Excel Workbook (`Final_Sample_Sales_Data_With_2345_Customers.xlsx`)
* **Schema Design:** Optimized Single Flat Table Model (`Sales` table) mapping transactional grains with geographical and product descriptors, combined with a separate DAX `Calculations` table housing core business metrics.
* **Granularity:** Line-item transaction grain, recording unique details per sale date, item quantity, customer demographics, and delivery status.

---

## 📑 Dashboard Pages & Visuals

The report is divided into four distinct focus areas:

### 1. Sales Overview
* **Objective:** Monitor primary sales channels, regional revenue distributions, and payment methods.
* **Core Metrics:** Revenue, Units Sold, Average Revenue per Sale.
* **Key Visuals:** Donut charts for Payment Method splits, card headers for KPIs, and trend line charts showing sales velocity over time.

### 2. Details by Product
* **Objective:** Audit individual electronic catalog items and inventory velocity.
* **Core Metrics:** Total Products, Units Sold by category.
* **Key Visuals:** Treemaps showing category share and stacked bar charts highlighting top-performing electronics.

### 3. Customer Insights
* **Objective:** Assess customer acquisition trends and purchase values.
* **Core Metrics:** Total Customers, Percent New Customers, Average Purchase Value.
* **Key Visuals:** Clustered columns comparing customer segments (New vs. Returning) and scatter plots relating purchase values to frequencies.

### 4. Return Analysis
* **Objective:** Track refunds, return rates, and product satisfaction rates.
* **Core Metrics:** Total Returns, Total Returned checks, % Orders Returned, Percent Orders Returned.
* **Key Visuals:** Bar charts indicating high-return product categories and KPI cards flagging return metrics to operations.

---

## ⚡ ETL Transformations & Power Query

Initial processing of raw spreadsheet data includes standard cleaning transformations in M Script:
1. **Source Loading:** excel sheet data read via `Excel.Workbook()`.
2. **Promoting Headers:** Promoting structural sheet headers to database fields.
3. **Data Type Conversions:** Coercing transactional columns (e.g. `Date` to type date, `Revenue` to type number, and `Quantity` to Int64) to ensure data model validation.
