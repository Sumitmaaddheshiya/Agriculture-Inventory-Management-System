import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="agriculture_inventory",
    auth_plugin="mysql_native_password"
)

cursor = conn.cursor()
print("Connected successfully")

### Add These FUNCTIONS

### Add Soil Sample
def add_soil_sample():
    location = input("Location: ")
    soil_type = input("Soil Type: ")
    ph = float(input("pH (0–14): "))

    if ph < 0 or ph > 14:
        print("Invalid pH value")
        return

    moisture = int(input("Moisture: "))
    nitrogen = int(input("Nitrogen: "))
    phosphorus = int(input("Phosphorus: "))
    potassium = int(input("Potassium: "))
    test_date = input("Date (YYYY-MM-DD): ")

    query = """
    INSERT INTO soil_samples
    (location, soil_type, ph_value, moisture, nitrogen, phosphorus, potassium, test_date)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """

    values = (location, soil_type, ph, moisture,
              nitrogen, phosphorus, potassium, test_date)

    cursor.execute(query, values)
    conn.commit()

    print("Soil sample added successfully")

### View Soil Samples
def view_soil_samples():
    cursor.execute("SELECT * FROM soil_samples")
    for row in cursor.fetchall():
        print(row)

### Add Fertilizer
def add_fertilizer():
    name = input("Fertilizer name: ")
    qty = int(input("Quantity: "))

    cursor.execute("""
    INSERT INTO fertilizers (fertilizer_name, quantity, last_updated)
    VALUES (%s,%s,CURDATE())
    """, (name, qty))

    conn.commit()
    print("Fertilizer added successfully")


### Low Stock Report

def low_stock_report():
    cursor.execute("""
    SELECT fertilizer_name, quantity
    FROM fertilizers
    WHERE quantity < 100
    """)

    print("Low Stock Fertilizers:")
    for row in cursor.fetchall():
        print(row)
# Add the MENU

while True:
    print("\n--- Agriculture Inventory Management ---")
    print("1. Add Soil Sample")
    print("2. View Soil Samples")
    print("3. Add Fertilizer")
    print("4. Low Stock Report")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_soil_sample()
    elif choice == "2":
        view_soil_samples()
    elif choice == "3":
        add_fertilizer()
    elif choice == "4":
        low_stock_report()
    elif choice == "5":
        print("Exiting system")
        break
    else:
        print("Invalid choice")
