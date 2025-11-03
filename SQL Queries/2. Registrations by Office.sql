SELECT OfficeCd, COUNT_BIG(*) AS RegistrationCount
FROM [dbo].[Vehicle_Data_Cleaned] WITH (NOLOCK)
GROUP BY OfficeCd
ORDER BY RegistrationCount DESC;