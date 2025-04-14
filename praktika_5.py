import sqlite3

connect = sqlite3.connect("users.db")
cursor = connect.cursor()


# cursor.execute("""
#         CREATE TABLE IF NOT EXISTS people(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT
            
#         )
# """)

# def register():
#     name = input("Enter your name:")

#     cursor.execute("""INSERT INTO people (name)
#                   VALUES (?)""", (name,))
#     connect.commit()

# register()

# def delete_student(id):
#     cursor.execute("DELETE FROM people WHERE id = ?", (id,))
#     connect.commit()
#     print(f"User {id} is successfully deleted.")

# delete_student(7)
# # delete_student(4)


def all_users():
    cursor.execute("SELECT * FROM people")
    users = cursor.fetchall()
    print(users)

all_users()