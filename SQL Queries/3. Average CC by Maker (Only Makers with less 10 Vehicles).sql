SELECT makerName, AVG(cc) AS AvgCC, COUNT_BIG(*) AS VehicleCount
FROM [dbo].[Vehicle_Data_Cleaned] WITH (NOLOCK)
WHERE cc IS NOT NULL
GROUP BY makerName
HAVING COUNT_BIG(*) > 10
ORDER BY AvgCC DESC;