-- Find all customers who made orders in 2024 with their total order amounts
-- Optimized version with index-friendly date filtering and reduced data processing
SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    c.email,
    SUM(oi.quantity * oi.price) as total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
WHERE o.order_date >= '2024-01-01' 
  AND o.order_date < '2025-01-01'
GROUP BY c.customer_id, c.first_name, c.last_name, c.email
ORDER BY total_spent DESC;