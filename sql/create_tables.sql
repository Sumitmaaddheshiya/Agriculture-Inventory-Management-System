-- Create Database
CREATE DATABASE agriculture_inventory;
USE agriculture_inventory;


-- table name soil_samples

CREATE TABLE soil_samples (
    sample_id INT AUTO_INCREMENT PRIMARY KEY,
    location VARCHAR(100),
    soil_type VARCHAR(50),
    ph_value DECIMAL(3,1),
    moisture INT,
    nitrogen INT,
    phosphorus INT,
    potassium INT,
    test_date DATE
);

-- Crop Records
CREATE TABLE crops (
    crop_id INT AUTO_INCREMENT PRIMARY KEY,
    crop_name VARCHAR(50),
    season VARCHAR(30),
    soil_type VARCHAR(50),
    expected_yield INT
);

-- Fertilizer Inverntory
CREATE TABLE fertilizers (
    fertilizer_id INT AUTO_INCREMENT PRIMARY KEY,
    fertilizer_name VARCHAR(50),
    quantity INT,
    last_updated DATE
);

