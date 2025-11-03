SELECT bodyType, COUNT_BIG(*) AS VehicleCount
FROM [dbo].[Vehicle_Data_Cleaned] WITH (NOLOCK)
GROUP BY bodyType
ORDER BY VehicleCount DESC;