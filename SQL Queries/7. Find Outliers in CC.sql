SELECT registrationNo, makerName, cc
FROM [dbo].[Vehicle_Data_Cleaned] WITH (NOLOCK)
WHERE cc > (
	SELECT AVG(cc) + 3*STDEV(cc)
	FROM [dbo].[Vehicle_Data_Cleaned]
	WHERE cc IS NOT NULL
);