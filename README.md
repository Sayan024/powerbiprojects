# Power BI Analytics Portfolio

Welcome to my Power BI repository showcasing data modeling (Star & Galaxy schemas), DAX engineering, and ETL data transformation pipelines.

This repository leverages Git branching to keep each dashboard project completely isolated with its own local dataset, reports metadata, screenshots, and documentation.

---

## 📂 Dashboard Portfolio Directory

Select a branch from the list below (or use the branch dropdown selector in the top-left on GitHub) to explore the individual project code, previews, and documentation:

### 1. 🍽️ Dine360 Restaurant Sales Analysis
* **Branch:** [Dine360RestuarantAnalysis](https://github.com/Sayan024/powerbiprojects/tree/Dine360RestuarantAnalysis)
* **Highlights:** Star schema mapping restaurant sales transactions, Average Order Value (AOV) metrics, menu mix Category Share, and location analysis.

### 2. 🛍️ Shoperkart Retail performance vs Targets
* **Branch:** [Shoperkart](https://github.com/Sayan024/powerbiprojects/tree/Shoperkart)
* **Highlights:** Galaxy schema with shared dimensions comparing actual daily transactions against monthly regional sales quotas, dynamic products/customers ranking, and margin preservation.

### 3. ⚡ Volt Electronic Sales, Cohorts & Logistics
* **Branch:** [VoltSalesDashboard](https://github.com/Sayan024/powerbiprojects/tree/VoltSalesDashboard)
* **Highlights:** Product return metrics tracking refund volumes, new vs returning customer cohorts, and logistics delays audits.

---

## 🛠️ Global Repository Optimizations
All dashboard branches in this repository have been optimized:
1. **Relative Local Data Sources:** Cleaned and remapped all semantic models to read from relative project folders (using extracted dataset caches).
2. **VertiPaq Engine Cleanup:** Scanned and removed 31 unused DAX measures across all models to optimize query caching and performance.
3. **Master Gitignore:** Configured to exclude user settings, session files, and temp caches (`cache.abf`).
