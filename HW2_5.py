import sqlite3

connect = sqlite3.connect("orders.db")
cursor = connect.cursor()


cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            product TEXT,
            quantity INTEGER

            
        )
""")

# def register():
#     name = input("Enter your name:")
#     product = input("Enter the name of the product:")
#     quantity = int(input("Enter the quantity of the product:"))

#     cursor.execute("""INSERT INTO orders 
#                    (name, product, quantity)
#                   VALUES (?, ?, ?)""", (name, product, quantity))
#     connect.commit()

# register()

# def all_orders():
#     cursor.execute("SELECT * FROM orders")
#     orders = cursor.fetchall()
#     print(orders)

# all_orders()

def over_1():
    cursor.execute("SELECT * FROM orders WHERE quantity > 1")
    order = cursor.fetchall()
    print(order)

# over_1()

def update_quantity(id, new_q):
    cursor.execute("UPDATE orders SET quantity = ? WHERE id = ?", (new_q, id))
    print("New information is successfully updated!")
    connect.commit()

# update_quantity(1, 7)

def delete_order(id):
    cursor.execute("DELETE FROM orders WHERE id = ?", (id,))
    connect.commit()
    print(f"User {id} is successfully deleted.")

delete_order(4)