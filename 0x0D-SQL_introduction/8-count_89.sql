-- count items with id as 89
SELECT
    COUNT(IF(id = '89', id,
            NULL)) AS countID
FROM
    first_table;
