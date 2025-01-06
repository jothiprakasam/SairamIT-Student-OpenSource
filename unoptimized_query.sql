-- Task: Optimize this SQL query to fetch data efficiently.

SELECT * 
FROM users 
WHERE id IN (
    SELECT id 
    FROM orders 
    WHERE order_date > '2024-01-01'
);

-- Contributors: Rewrite this query to improve performance, avoid subqueries, and use indexes effectively.
