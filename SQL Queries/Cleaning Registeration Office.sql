UPDATE [dbo].[Vehicle_Data_Cleaned]
SET OfficeCd = LTRIM(RTRIM(
    -- If OfficeCd contains a comma, get the last part after the last comma
    CASE
        WHEN OfficeCd LIKE '%,%' THEN
            RIGHT(OfficeCd, CHARINDEX(',', REVERSE(OfficeCd)) - 1)
        ELSE OfficeCd
    END
));