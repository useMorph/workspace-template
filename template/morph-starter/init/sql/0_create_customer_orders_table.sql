-- Check if the example table exists in the public schema
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT FROM pg_tables
        WHERE schemaname = 'public'
        AND tablename = 'customer_orders'
    ) THEN
        -- Create the table if it does not exist
        CREATE TABLE customer_orders (
            order_id INT,
            customer_id INT,
            product_name VARCHAR(255),
            quantity INT,
            unit_price NUMERIC(10, 2),
            order_date DATE
        );

        -- Insert data into the table
        INSERT INTO customer_orders (order_id, customer_id, product_name, quantity, unit_price, order_date)
        VALUES
            (200, 2, 'Laptop', 5, 484.27, '2024-01-10'),
            (142, 5, 'Wireless Mouse', 2, 976.13, '2024-06-16'),
            (136, 10, 'Laptop', 4, 1115.96, '2024-08-01'),
            (111, 7, 'Laptop', 5, 1452.09, '2024-06-23'),
            (168, 2, 'Monitor', 5, 291.11, '2024-04-05'),
            (130, 7, 'Wireless Mouse', 5, 183.02, '2024-05-19'),
            (169, 4, 'USB Cable', 1, 255.89, '2024-09-22'),
            (131, 3, 'Laptop', 4, 1229.9, '2024-05-06'),
            (199, 2, 'Mechanical Keyboard', 4, 936.13, '2024-10-12'),
            (126, 5, 'USB Cable', 2, 1069.24, '2024-07-26'),
            (141, 5, 'Laptop', 4, 955.23, '2024-06-29'),
            (166, 4, 'Wireless Mouse', 1, 417.97, '2024-07-14'),
            (153, 9, 'Wireless Mouse', 3, 1201.15, '2024-04-17'),
            (106, 6, 'USB Cable', 1, 1479.23, '2024-10-08'),
            (142, 5, 'Mechanical Keyboard', 4, 419.21, '2024-01-26'),
            (171, 4, 'USB Cable', 4, 1260.35, '2024-06-22'),
            (190, 5, 'Laptop', 5, 1405.93, '2024-09-06'),
            (119, 8, 'Monitor', 3, 1317.15, '2024-09-01'),
            (178, 5, 'Monitor', 4, 754.4, '2024-05-12'),
            (161, 8, 'USB Cable', 1, 1425.77, '2024-05-17'),
            (166, 2, 'Laptop', 3, 581.52, '2024-09-16'),
            (159, 8, 'USB Cable', 5, 1101.48, '2024-09-25'),
            (115, 1, 'USB Cable', 3, 474.21, '2024-04-27'),
            (172, 4, 'Wireless Mouse', 5, 132.29, '2024-10-04'),
            (144, 5, 'Wireless Mouse', 5, 146.92, '2024-04-05'),
            (143, 10, 'USB Cable', 2, 1396.23, '2024-07-27'),
            (183, 5, 'Mechanical Keyboard', 5, 647.64, '2024-09-15'),
            (148, 9, 'USB Cable', 4, 490.2, '2024-08-02'),
            (119, 10, 'Monitor', 2, 1467.44, '2024-03-01'),
            (172, 6, 'Wireless Mouse', 5, 53.55, '2024-09-14');
    END IF;
END $$;
