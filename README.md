# Vehicle-Registration-Analysis

Data analysis of the latest Telangana Regional Transport Office (RTO) vehicle registration dataset.

This repository contains the analysis pipeline I use to explore, clean, and report insights from the Telangana vehicle registration data.

🔗 Dataset (source): [https://www.kaggle.com/datasets/chandansy/telangana-vehicle-registration-data](https://www.kaggle.com/datasets/chandansy/telangana-vehicle-registration-data)

## What I'm doing here

-   Verify and ingest the raw dataset
-   Clean and preprocess the data (dates, categorical normalization, missing value handling)
-   Perform exploratory data analysis (top makes/models, registrations by RTO and time, distributions)
-   Run advanced analyses (trend analysis, growth rates, anomaly detection, optional geospatial mapping)
-   Optionally build a short time-series forecast and/or a small interactive dashboard
-   Produce a written report with figures and reproducible steps

## Analysis Workflow Steps

1. **Data Ingestion**
   - Download the raw dataset from Kaggle.
   - Place the CSV file in the `Dataset/` folder.

2. **Data Verification & Initial Exploration**
   - Load the CSV into a pandas DataFrame.
   - Inspect column names, data types, and sample rows.
   - Check for missing values and obvious data issues.

3. **Data Cleaning & Preprocessing**
   - Normalize categorical fields (e.g., vehicle make/model, RTO codes).
   - Parse and standardize date fields.
   - Handle missing or inconsistent values.
   - Save cleaned data to `data/` as CSV or Parquet.

4. **SQL-Based Analysis (with SSMS)**
   - Import the cleaned dataset into a SQL Server database.
   - Use SQL Server Management Studio (SSMS) for:
     - Data exploration with SELECT queries
     - Aggregations (GROUP BY, COUNT, SUM, etc.)
     - Advanced analysis (window functions, joins, subqueries)
     - Data cleaning and transformation using SQL
     - Exporting query results for reporting and visualization

5. **Exploratory Data Analysis (EDA)**
   - Analyze top vehicle makes and models.
   - Visualize registrations by RTO, time, and other categories.
   - Plot distributions and identify patterns.

6. **Advanced Analysis**
   - Perform trend analysis and calculate growth rates.
   - Detect anomalies or outliers in registration data.
   - (Optional) Map registrations geospatially if location data is available.

7. **Forecasting & Dashboard (Optional)**
   - Build a simple time-series forecast for future registrations.
   - Create an interactive dashboard for data exploration.

8. **Reporting**
   - Generate figures and summary tables.
   - Write a report documenting methods, findings, and insights.
   - Save outputs in the `reports/` folder.

9. **Reproducibility**
   - Document all steps in notebooks and scripts.
   - List required Python packages in `requirements.txt`.

## SQL Server Management Studio (SSMS) Usage

- SSMS is recommended for SQL-based exploration, cleaning, and reporting.
- Example workflow:
  1. Create a database and import the vehicle registration data.
  2. Use T-SQL queries for analysis and transformation.
  3. Save and share query scripts for reproducibility.
  4. Export results for further analysis or visualization.

## Project structure

```
.├─ Dataset/                  # place the raw CSV(s) here (do NOT commit large files)
├─ data/                     # processed data outputs (cleaned parquet/csv)
├─ notebooks/                # Jupyter notebooks for ingestion, EDA, modeling
├─ reports/                  # generated figures and final analysis report
├─ requirements.txt          # Python packages used for the analysis
└─ README.md                 # this file
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.