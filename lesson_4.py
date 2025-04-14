# ООП - Объектно-ориентированное программирование "Абстракция"

# class Programmer:
#     def direction(self):
#         pass

#     def language(self):
#         pass

#     def laptop(self):
#         pass


# class WebDeveloper(Programmer):
#     def direction(self):
#         return f"Backend"
    
#     def language(self):
#         return f"python"
    
#     def laptop(self):
#         return f"True"
    
    
# class Vercel(Programmer):
#     def direction(self):
#         return f"Frontend"
    
#     def language(self):
#         return f"JavaScript"
    
#     def laptop(self):
#         return f"False"
    
    
# class Server(Programmer):
#     def direction(self):
#         return f"Devops"
    
#     def language(self):
#         return f"Linux/Ubuntu/Kali"
    
#     def laptop(self):
#         return f"True"
    

# programmer = [WebDeveloper(), Vercel(), Server()]

# for i in programmer:
#         print(i.direction())
#         print(i.language())
#         print(i.laptop())


       
import sqlite3

connect = sqlite3.connect("geeks.db")
cursor = connect.cursor()


cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name VARCHAR (50) NOT NULL,
            age INT DEFAULT NULL,
            direction TEXT,
            is_have BOOLEAN NOT NULL DEFAULT FALSE,
            birth_date DATE,
            rating DOUBLE (4,2) DEFAULT (0.0)
        )
""")


# def register():
#     full_name = input("Enter your full name:")
#     age = int(input("Enter your age:"))
#     direction = input("Enter your direction:")
#     is_have = bool(input("Laptop availability:"))
#     birth_date = input("Enter your birthdate:")
#     rating = float(input("Enter your rating:"))

    # cursor.execute(f""" INSERT INTO users
    #                (full_name, age, direction, is_have, birth_date, rating)
    #                VALUES ('{full_name}',{age}, '{direction}', {is_have}, '{birth_date}', {rating})""")
    # connect.commit() # Sohranenie v BD

    # Использование форматированных строк (f"") для вставки значений в SQL-запрос может привести к уязвимости типа SQL-инъекция, 
     # если пользователь вводит cпециальные символы в текстовые поля.
    # cursor.execute(""" INSERT INTO users
    #                (full_name, age, direction, is_have, birth_date, rating)
    #                VALUES (?, ?, ?, ?, ?, ?)""", (full_name, age, direction, is_have, birth_date, rating))
    # connect.commit() # Sohranenie v BD
    # '''Плейсхолдер (англ. placeholder) — это специальный символ или текстовый маркер, который используется в SQL-запросах
    #   и других контекстах программирования для обозначения места, куда позже будет вставлено значение'''
    
def all_students():
    cursor.execute("SELECT * FROM users")
    students = cursor.fetchall()
    print(students)

def one_student(id):
    cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
    student = cursor.fetchone()
    print(student)


def delete_student(id):
    cursor.execute("DELETE FROM users WHERE id = ?", (id,))
    connect.commit()
    print(f"User {id} is successfully deleted.")

# register()
# all_students()
# one_student(1)
delete_student(1)