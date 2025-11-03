# Exploratory Data Analysis (EDA)

This document outlines my process and findings from the exploratory data analysis (EDA) of the Telangana RTO vehicle registration dataset.

---

## What I Explore

- Top vehicle makes and models
- Registrations by RTO office
- Registrations over time (monthly trends)
- Distribution of engine capacity (CC)
- Outliers and anomalies in the data
- Distinct vehicle makers
- Most powerful vehicles

---

## My EDA Workflow

1. **Load the Cleaned Data**
   - I use `Vehicle_Data_Cleaned.csv` from the `Dataset/` folder.
   - Load into pandas DataFrame for analysis.

2. **Summary Statistics & Data Types**
   - Check column types, missing values, and basic stats.

3. **Top Makes and Models**
   - Group by make/model, count registrations.
   - Visualize top 10 makes/models.

4. **Registrations by Office**
   - Group by RTO office, count registrations.
   - Plot office-wise distribution.

5. **Monthly Registration Trends**
   - Parse registration dates.
   - Aggregate by month/year, plot time series.

6. **Engine Capacity (CC) Distribution**
   - Plot histogram of CC values.
   - Identify outliers using boxplot or IQR.

7. **Distinct Makers Count**
   - Count unique vehicle makers.

8. **Most Powerful Vehicles**
   - Sort by CC, list top 5 vehicles.

9. **Outlier Detection**
   - Use statistical methods to find anomalies in CC or registration counts.

---

## Example Code Snippets

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Dataset/Vehicle_Data_Cleaned.csv')

# Top 10 vehicle makes
print(df['Make'].value_counts().head(10))

# Registrations by office
print(df['RTO_Office'].value_counts())

# Monthly registration trend
monthly = df.groupby(df['Registration_Date'].str[:7]).size()
monthly.plot(kind='line')
plt.title('Monthly Registration Trend')
plt.show()
```

---

## Key Findings

- [Summarize your main insights here after running the analysis.]
- Example: "Most registrations are for Maruti Suzuki, with Hyderabad RTO leading in volume. Registration trends show a peak in early 2022. Several outliers in CC suggest data entry errors or rare high-performance vehicles."

---

## Next Steps

- Use SQL scripts for deeper aggregations and reporting.
- Visualize more features if needed.
- Document all findings in the final report.

---

*See `Data_Cleaning.ipynb` for the full notebook and `Reports/` for generated CSV outputs.*
