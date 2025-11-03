SELECT DATEFROMPARTS(YEAR(regvalidfrom), MONTH(regvalidfrom), 1) AS MonthStart,
       COUNT_BIG(*) AS Registrations
FROM [dbo].[Vehicle_Data_Cleaned] WITH (NOLOCK)
WHERE regvalidfrom IS NOT NULL
GROUP BY DATEFROMPARTS(YEAR(regvalidfrom), MONTH(regvalidfrom), 1)
ORDER BY MonthStart;