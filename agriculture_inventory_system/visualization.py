# Database Connection in visualization.py

import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="agriculture_inventory",
    auth_plugin="mysql_native_password"
)

print("Connected for visualization")

# Visualization 1 – Soil pH Distribution
def soil_ph_distribution():
    query = "SELECT ph_value FROM soil_samples"
    df = pd.read_sql(query, conn)

    plt.figure()
    plt.hist(df['ph_value'], bins=10)
    plt.title("Soil pH Distribution")
    plt.xlabel("pH Value")
    plt.ylabel("Number of Samples")
    plt.show()

# Visualization 2 – Daily Soil Testing Trend

def daily_soil_testing():
    query = """
    SELECT test_date, COUNT(*) AS samples
    FROM soil_samples
    GROUP BY test_date
    ORDER BY test_date
    """
    df = pd.read_sql(query, conn)

    plt.figure()
    plt.plot(df['test_date'], df['samples'])
    plt.title("Daily Soil Testing Trend")
    plt.xlabel("Date")
    plt.ylabel("Samples Tested")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Visualization 3 – Low Stock Fertilizers

def fertilizer_low_stock_chart():
    query = """
    SELECT fertilizer_name, quantity
    FROM fertilizers
    WHERE quantity < 100
    """
    df = pd.read_sql(query, conn)

    if df.empty:
        print("No low stock fertilizers")
        return

    plt.figure(figsize=(14, 6))   # 👈 increase width
    plt.bar(df['fertilizer_name'], df['quantity'])
    plt.title("Low Stock Fertilizers")
    plt.xlabel("Fertilizer")
    plt.ylabel("Quantity")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

soil_ph_distribution()
daily_soil_testing()
fertilizer_low_stock_chart()
