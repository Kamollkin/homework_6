from main import User, UserService

user = UserService()

user_services = User(name= "Adelina", email='asa@gmail.com', age = 16)

# user.add_user(user_services)

find = user.find_user_by_email('asa@gmail.com')
if find:
    print(f"User is found: {find.name}, {find.email}, {find.age}")

delete = user.delete_user_by_email('asa@gmail.com')

