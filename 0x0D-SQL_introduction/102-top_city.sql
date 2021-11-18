-- displays top 3 cities tempratures for July and august
-- order this by descending temperature
SELECT city, AVG(value) AS avg_temp FROM temperatures
       WHERE month IN (7, 8)
       GROUP BY city
       ORDER BY avg_temp DESC LIMIT 3;
