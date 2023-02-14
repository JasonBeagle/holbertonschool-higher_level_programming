-- lists all records of second_table of hbtn_0c_0 in your MySQL server
-- lists all records in a table except rows without a name value
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;