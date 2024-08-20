import mysql.connector
from mysql.connector import Error

def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='SalesManagement',
                                       user='root',
                                       password='mango')
        if conn.is_connected():
            print('Connected to MySQL database')
            return conn
    except Error as e:
        print(e)

def add_customer(conn):
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    phone = input("Enter customer phone: ")
    address = input("Enter customer address: ")
    loyalty_program = input("Enter customer loyalty program: ")
    cursor = conn.cursor()
    query = "INSERT INTO Customers(name, email, phone, address, loyalty_program) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (name, email, phone, address, loyalty_program))
    conn.commit()
    print("Customer added successfully!")

def view_customers(conn):
    cursor = conn.cursor()
    query = "SELECT * FROM Customers"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def add_product(conn):
    name = input("Enter product name: ")
    description = input("Enter product description: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))
    category = input("Enter product category: ")
    cursor = conn.cursor()
    query = "INSERT INTO Products(name, description, price, quantity, category) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (name, description, price, quantity, category))
    conn.commit()
    print("Product added successfully!")

def view_products(conn):
    cursor = conn.cursor()
    query = "SELECT * FROM Products"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def add_supplier(conn):
    name = input("Enter supplier name: ")
    email = input("Enter supplier email: ")
    phone = input("Enter supplier phone: ")
    address = input("Enter supplier address: ")
    product_offerings = input("Enter product offerings: ")
    cursor = conn.cursor()
    query = "INSERT INTO Suppliers(name, email, phone, address, product_offerings) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (name, email, phone, address, product_offerings))
    conn.commit()
    print("Supplier added successfully!")

def view_suppliers(conn):
    cursor = conn.cursor()
    query = "SELECT * FROM Suppliers"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def record_sale(conn):
    customer_id = int(input("Enter customer ID: "))
    product_id = int(input("Enter product ID: "))
    quantity = int(input("Enter quantity sold: "))
    date = input("Enter sale date (YYYY-MM-DD): ")
    total = float(input("Enter total sale amount: "))
    cursor = conn.cursor()
    query = "INSERT INTO Sales(customer_id, product_id, quantity, date, total) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (customer_id, product_id, quantity, date, total))
    conn.commit()
    print("Sale recorded successfully!")

def view_sales(conn):
    cursor = conn.cursor()
    query = "SELECT * FROM Sales"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def main():
    conn = connect()  # Connect to the database
    if conn is None:
        return

    while True:
        print("\nMenu:")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Add Product")
        print("4. View Products")
        print("5. Add Supplier")
        print("6. View Suppliers")
        print("7. Record Sale")
        print("8. View Sales")
        print("9. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            add_customer(conn)
        elif choice == '2':
            view_customers(conn)
        elif choice == '3':
            add_product(conn)
        elif choice == '4':
            view_products(conn)
        elif choice == '5':
            add_supplier(conn)
        elif choice == '6':
            view_suppliers(conn)
        elif choice == '7':
            record_sale(conn)
        elif choice == '8':
            view_sales(conn)
        elif choice == '9':
            conn.close()
            print("Connection closed.")
            break
        else:
            print("Invalid Choice. Please choose a valid option.")

if __name__ == '__main__':
    main()
