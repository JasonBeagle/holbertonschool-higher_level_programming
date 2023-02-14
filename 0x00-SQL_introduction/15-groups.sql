-- lists number of records with the same score in second_table of the database hbtn_0c_0 in your MySQL server
-- groups rows together when they have the same scores and displays the number of occurrences
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;