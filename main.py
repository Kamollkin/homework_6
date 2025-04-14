from lesson_7 import DataBase

class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

class UserService:
    def __init__(self):
        self.db = DataBase()

    def add_user(self,user):
        if self.find_user_by_email(user.email):
            print("User with this email is already exists!")
            return
        self.db.add_user(user)
        print("User is successfully added!")

    
    def find_user_by_email(self,email):
        user_data = self.db.get_user(email)
        if user_data:
            return User(name=user_data[1], email=user_data[2], age=user_data[3])
        else:
            print("User is not found!")
        
    def delete_user_by_email(self,email):
        delete_user = self.find_user_by_email(email)
        if delete_user:
            self.db.delete_user_by_email(email)
        else:
            None

        