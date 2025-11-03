# Vehicle-Registration-Analysis

This is my personal project for analyzing the Telangana Regional Transport Office (RTO) vehicle registration dataset. Here, I document my workflow, code, and insights as I explore, clean, and report on this data.

---

## My Approach

I use a mix of Python (pandas, Jupyter notebooks) and SQL (SQL Server Management Studio) to work through the data. My goal is to make the process reproducible and the results easy to share.

**Dataset Source:**  
[Kaggle: Telangana Vehicle Registration Data](https://www.kaggle.com/datasets/chandansy/telangana-vehicle-registration-data)

---

## What I Do in This Project

-   Download and verify the raw dataset
-   Clean and preprocess the data (dates, categories, missing values)
-   Explore the data: top makes/models, registrations by RTO and time, distributions
-   Run advanced analyses: trends, growth rates, anomaly detection, (sometimes) geospatial mapping
-   Optionally build a time-series forecast or a small dashboard
-   Write up my findings and save all outputs for reproducibility

---

## My Analysis Workflow

1.  **Data Ingestion**: I download the raw CSV from Kaggle and put it in the `Dataset/` folder.
2.  **Initial Exploration**: I use pandas to inspect columns, data types, and missing values.
3.  **Data Cleaning**: I normalize categories, parse dates, and handle missing/inconsistent values. The cleaned data goes into `Dataset/Vehicle_Data_Cleaned.csv`.
4.  **SQL Analysis**: I import the cleaned data into SQL Server and use my `.sql` scripts for deeper analysis and reporting.
5.  **Exploratory Data Analysis (EDA)**: I look at top makes/models, registrations by office and time, distributions, and trends.
6.  **Advanced Analysis**: I run trend analysis, calculate growth rates, and detect anomalies or outliers.
7.  **Forecasting & Dashboard (Optional)**: If I have time, I build a simple forecast or dashboard.
8.  **Reporting**: I export results to CSV in `Reports/` and document my findings in markdown files.
9.  **Reproducibility**: I keep all steps in notebooks/scripts and list required Python packages in `requirements.txt`.

---

## How I Use SQL Server Management Studio (SSMS)

-   I use SSMS for SQL-based exploration, cleaning, and reporting.
-   My typical workflow:
    1.  Create a database and import the cleaned vehicle registration data.
    2.  Run T-SQL queries for analysis and transformation (see `SQL Queries/`).
    3.  Save and share query scripts for reproducibility.
    4.  Export results for further analysis or visualization.

---

## My Project Structure

```text
├─ Dataset/                  # raw and cleaned CSV files│   ├─ Vehicle_Data.csv│   └─ Vehicle_Data_Cleaned.csv├─ Notebook/                 # Jupyter notebooks for data cleaning and analysis│   └─ Data_Cleaning.ipynb├─ Reports/                  # generated CSV reports from analysis│   ├─ 1. Count of Vehicles by Type.csv│   ├─ 2. Registrations by Office.csv│   ├─ 3. Average CC by Maker (Only Makers with less 10 Vehicles).csv│   ├─ 4. Monthly Registration Trend.csv│   ├─ 5. Top 5 Most Powerful Vehicles.csv│   ├─ 6. Distinct Makers Count.csv│   ├─ 7. Find Outliers in CC.csv├─ SQL Queries/              # SQL scripts for analysis and cleaning│   ├─ 1. Count of Vehicles by Type.sql│   ├─ 2. Registrations by Office.sql│   ├─ 3. Average CC by Maker (Only Makers with less 10 Vehicles).sql│   ├─ 4. Monthly Registration Trend.sql│   ├─ 5. Top 5 Most Powerful Vehicles.sql│   ├─ 6. Distinct Makers Count.sql│   ├─ 7. Find Outliers in CC.sql│   ├─ Cleaning Registeration Office.sql│   └─ Creating Indexes.sql├─ Detailed_Walk_Through.md  # step-by-step analysis guide├─ SQL_Analysis_Guide.md     # SQL workflow and queries documentation├─ README.md                 # this file
```

---

## How You Can Reproduce My Steps

1.  Download the dataset from Kaggle and place it in `Dataset/Vehicle_Data.csv`.
2.  Run my Jupyter notebook in `Notebook/Data_Cleaning.ipynb` to clean and preprocess the data.
3.  Import the cleaned CSV into SQL Server and run the scripts in `SQL Queries/` for analysis.
4.  Export results to CSV files in `Reports/`.
5.  Check out `Detailed_Walk_Through.md` and `SQL_Analysis_Guide.md` for my step-by-step instructions.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.