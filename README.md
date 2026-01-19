# Agriculture Inventory Management System

## Overview
This project is a Python and MySQL based Agriculture Inventory Management System designed to manage soil samples, crop records, and fertilizer inventory. The system supports CSV-based bulk data ingestion, database storage, analytical reporting, and data visualization.

## Features
- Soil sample inventory management
- Fertilizer stock management with low-stock alerts
- CSV-based bulk data import
- Data validation and cleaning
- Analytical reports and visualizations
- Modular Python code structure

## Tech Stack
- Python
- MySQL
- Pandas
- Matplotlib
- CSV

## Project Structure
- main.py – Handles data insertion, inventory operations, and reports
- visualization.py – Handles analytical visualizations
- data/ – Contains CSV files used for bulk data ingestion
- sql/ – Database table creation scripts
- screenshots/ – Output charts and graphs

## Database Tables
- soil_samples
- crops
- fertilizers

## How to Run
1. Create the database and tables using SQL scripts.
2. Update MySQL credentials in Python files.
3. Run main.py for data operations.
4. Run visualization.py for charts and analysis.

## Data Cleaning & Validation
- Removed missing and null values from CSV files.
- Validated soil pH values to ensure they fall within the range 0–14.
- Converted numeric fields to correct data types.
- Ensured date fields follow YYYY-MM-DD format.
- Prevented duplicate and inconsistent inventory records.
- Maintained realistic value ranges to simulate real-world agricultural data.

## Use Case
This system simulates real-life agricultural data collection and inventory management, supporting soil health analysis, fertilizer stock monitoring, and data-driven decision-making.
