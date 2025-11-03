SELECT COUNT(DISTINCT makerName) AS MakerCount
FROM [dbo].[Vehicle_Data_Cleaned] WITH (NOLOCK);