SELECT TOP 5 registrationNo, makerName, modelDesc, hp, bodyType
FROM [dbo].[Vehicle_Data_Cleaned] WITH (NOLOCK)
WHERE hp IS NOT NULL
ORDER BY hp DESC;