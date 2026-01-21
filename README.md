# Agriculture Inventory Management System

## Overview
This project is a Python and MySQL based Agriculture Inventory Management System designed to manage soil samples, crop records, and fertilizer inventory. The system supports CSV-based bulk data ingestion, database storage, analytical reporting, and data visualization.

## 📂 Folder Structure (Updated)
Agriculture-Inventory-Management-System/
│
├── data/                  # CSV files
├── sql/                   # Database scripts
├── screenshots/           # Output charts & graphs
│   ├── daily_testing_trend.png
│   ├── low_stock_fertilizers.png
│   └── soil_ph_distribution.png
├── main.py
├── visualization.py
└── README.md

## 📊 Visualizations & Outputs
📈 Daily Soil Testing Trend
<img width="761" height="602" alt="daily_testing_trend png" src="https://github.com/user-attachments/assets/0cad34f5-45ea-4c3f-bb7c-36c2a1d07c2d" />

Shows the number of soil samples tested each day to monitor testing frequency and trends.

🚨 Low Stock Fertilizers
<img width="1736" height="788" alt="low_stock_fertilizers png" src="https://github.com/user-attachments/assets/f4577a6d-aa1a-4616-bbf6-99bf476f6579" />

Identifies fertilizers with low inventory levels to support timely restocking decisions.

🧪 Soil pH Distribution
<img width="787" height="636" alt="soil_ph_distribution png" src="https://github.com/user-attachments/assets/1168df2a-3b55-46c5-8de9-f40f61724d73" />

Displays the distribution of soil pH values to analyze soil health and suitability for crops.
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
