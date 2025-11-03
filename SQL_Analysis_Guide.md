# SQL Analysis Guide: My Workflow for Vehicle Registration Data

This guide documents the exact steps I use to analyze my vehicle registration data in SQL Server Management Studio (SSMS).

---

## Importing My Data

1.  I open SSMS and connect to my database.
2.  I use **Tasks > Import Data** to load my cleaned CSV (`Vehicle_Data_Cleaned.csv`) into a table named `[dbo].[Vehicle_Data_Cleaned]`.
3.  I make sure the column types match my data (see below for recommended types).

---

## Checking Column Types

To confirm my table columns are correct, I run:

```sql
SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTHFROM INFORMATION_SCHEMA.COLUMNSWHERE TABLE_NAME = 'Vehicle_Data_Cleaned' AND TABLE_SCHEMA = 'dbo';
```

---

## Indexing for Fast Analysis

Before running heavy queries, I create indexes to speed up grouping and sorting:

```sql
CREATE INDEX idx_bodyType ON [dbo].[Vehicle_Data_Cleaned](bodyType);CREATE INDEX idx_OfficeCd ON [dbo].[Vehicle_Data_Cleaned](OfficeCd);CREATE INDEX idx_makerName ON [dbo].[Vehicle_Data_Cleaned](makerName);CREATE INDEX idx_regvalidfrom ON [dbo].[Vehicle_Data_Cleaned](regvalidfrom);CREATE INDEX idx_hp ON [dbo].[Vehicle_Data_Cleaned](hp);
```

---

## My Go-To Analysis Queries (Optimized for 500k+ Rows)

### 1. Count of Vehicles by Type

```sql
SELECT bodyType, COUNT_BIG(*) AS VehicleCountFROM [dbo].[Vehicle_Data_Cleaned] WITH (NOLOCK)GROUP BY bodyTypeORDER BY VehicleCount DESC;
```

### 2. Registrations by Office (with OfficeCd Cleaning)

Before running this query, I clean up the OfficeCd column to remove unwanted prefixes (like '5,' or 'DIESEL,50.0,5,') and keep only the actual office name:

```sql
-- Clean OfficeCd by keeping only the last part after the last commaUPDATE [dbo].[Vehicle_Data_Cleaned]SET OfficeCd = LTRIM(RTRIM(	CASE		WHEN OfficeCd LIKE '%,%' THEN RIGHT(OfficeCd, CHARINDEX(',', REVERSE(OfficeCd)) - 1)		ELSE OfficeCd	END));
```

Now I run the optimized registrations by office query:

```sql
SELECT OfficeCd, COUNT_BIG(*) AS RegistrationCountFROM [dbo].[Vehicle_Data_Cleaned] WITH (NOLOCK)GROUP BY OfficeCdORDER BY RegistrationCount DESC;
```

### 3. Average CC by Maker (Only Makers with >10 Vehicles)

```sql
SELECT makerName, AVG(cc) AS AvgCC, COUNT_BIG(*) AS VehicleCountFROM [dbo].[Vehicle_Data_Cleaned] WITH (NOLOCK)WHERE cc IS NOT NULLGROUP BY makerNameHAVING COUNT_BIG(*) > 10ORDER BY AvgCC DESC;
```

### 4. Monthly Registration Trend

```sql
SELECT DATEFROMPARTS(YEAR(regvalidfrom), MONTH(regvalidfrom), 1) AS MonthStart,       COUNT_BIG(*) AS RegistrationsFROM [dbo].[Vehicle_Data_Cleaned] WITH (NOLOCK)WHERE regvalidfrom IS NOT NULLGROUP BY DATEFROMPARTS(YEAR(regvalidfrom), MONTH(regvalidfrom), 1)ORDER BY MonthStart;
```

### 5. Top 5 Most Powerful Vehicles

```sql
SELECT TOP 5 registrationNo, makerName, modelDesc, hp, bodyTypeFROM [dbo].[Vehicle_Data_Cleaned] WITH (NOLOCK)WHERE hp IS NOT NULLORDER BY hp DESC;
```

### 6. Distinct Makers Count

```sql
SELECT COUNT(DISTINCT makerName) AS MakerCountFROM [dbo].[Vehicle_Data_Cleaned] WITH (NOLOCK);
```

### 7. Find Outliers in CC

```sql
SELECT registrationNo, makerName, ccFROM [dbo].[Vehicle_Data_Cleaned] WITH (NOLOCK)WHERE cc > (	SELECT AVG(cc) + 3*STDEV(cc)	FROM [dbo].[Vehicle_Data_Cleaned]	WHERE cc IS NOT NULL);
```

---

## Exporting My Results

After running my queries, I export results from SSMS to CSV for reporting and further analysis.