-- Find all customers who made orders in 2024 with their total order amounts
-- Optimized version with performance improvements

-- Recommended indexes:
-- CREATE INDEX idx_orders_date_customer ON orders(order_date, customer_id);
-- CREATE INDEX idx_order_items_order_id ON order_items(order_id);
-- CREATE INDEX idx_customers_id ON customers(customer_id);

WITH customer_orders_2024 AS (
    -- Pre-filter orders to reduce join size
    SELECT 
        o.customer_id,
        o.order_id
    FROM orders o
    WHERE o.order_date >= '2024-01-01' 
      AND o.order_date < '2025-01-01'
),
order_totals AS (
    -- Calculate order totals before joining with customer data
    SELECT 
        co.customer_id,
        SUM(oi.quantity * oi.price) as total_spent
    FROM customer_orders_2024 co
    JOIN order_items oi ON co.order_id = oi.order_id
    GROUP BY co.customer_id
)
SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    c.email,
    ot.total_spent
FROM customers c
JOIN order_totals ot ON c.customer_id = ot.customer_id
ORDER BY ot.total_spent DESC;