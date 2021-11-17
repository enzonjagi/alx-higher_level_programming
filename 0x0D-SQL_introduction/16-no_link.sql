-- list all records in second_table
-- where name is not null
-- select score and name
-- ORDER BY descending score
SELECT score, name FROM second_table
       WHERE name IS NOT NULL
       ORDER BY score DESC;
