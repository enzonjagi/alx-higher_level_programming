-- list number of records with same score
-- this is stored under number
SELECT score, COUNT(score) AS number FROM second_table
       GROUP BY score
       ORDER BY score DESC;
