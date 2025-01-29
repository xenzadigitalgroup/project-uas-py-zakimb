CREATE DATABASE pbo_zaki;

USE db_zaki;

CREATE TABLE customers_zaki (
    cus_id INT PRIMARY KEY,
    cus_name VARCHAR(255)
);

CREATE TABLE product_zaki (
    id_product INT PRIMARY KEY,
    name VARCHAR(255),
    price INT
);

CREATE TABLE motorcycles_zaki (
    id_product INT PRIMARY KEY,
    name VARCHAR(255),
    price INT,
    cylinder INT,
    tank_capacity INT
);

CREATE TABLE electric_motorcycles_zaki (
    id_product INT PRIMARY KEY,
    name VARCHAR(255),
    price INT,
    battery INT,
    mileage INT
);

CREATE TABLE orders_zaki (
    id_order INT PRIMARY KEY,
    customer INT,
    product VARCHAR(255),
    date DATE
);

RENAME TABLE products_zaki TO product_zaki;

-- Insert data into product_zaki
INSERT INTO product_zaki (id_product, name, price) 
VALUES
(1, 'Helmet Zaki', 500000),
(2, 'Motor Oil Zaki', 150000);

-- Insert data into motorcycles_zaki
INSERT INTO motorcycles_zaki (id_product, name, price, cylinder, tank_capacity) 
VALUES
(1, 'Motorcycle Zaki 150cc', 20000000, 150, 12),
(2, 'Motorcycle Zaki 250cc', 30000000, 250, 15);

-- Insert data into electric_motorcycles_zaki
INSERT INTO electric_motorcycles_zaki (id_product, name, price, battery, mileage) 
VALUES
(1, 'E-Motor Zaki Lite', 25000000, 1500, 120),
(2, 'E-Motor Zaki Pro', 35000000, 2000, 180);

-- Insert data into orders_zaki
INSERT INTO orders_zaki (id_order, customer, product, date) 
VALUES
(1, 101, 'Helmet Zaki', '2025-01-14'),
(2, 102, 'E-Motor Zaki Lite', '2025-01-15');
