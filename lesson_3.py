# Инкапсуляция

# class BankAccount:
#     def __init__(self, balance=0):
#         self.__balance = balance # __ privatnaya

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#            self.__balance -= amount

#     def get_balance(self):
#         return self.__balance
    
# account = BankAccount(1000)
# account.deposit(500)
# account.withdraw(200)

# # print(account.__balance)
# print(account.get_balance())


# class Person:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self._age = age
#         self.__salary = salary
    
#     # Геттер для защищенного атрибута

#     def get_age(self):
#         return self._age
#     #  Сеттер  для защищенного атрибута
#     def set_age(self,age):
#         if age > 0:
#             self._age = age
#         else:
#             print("Возраст должен быть положительным числом")
#     def get_salary(self):
#         return self.__salary
#     def set_salary(self, salary):
#         if salary >= 0:
#             self.__salary = salary
#         else:
#             print("Зарплата не может быть отрицательной!")

# person = Person ( "Kamola Nimatulaeva", 32, 50000)
# print("Имя:", person.name)
# print("Возраст до изменения:", person.get_age())
# person.set_age(33)
# print("Возраст после изменения:", person.get_age())

# print("Зп до изменения:", person.get_salary())
# person.set_salary(70000)
# print("Зп после изменения:", person.get_salary())

# print(person.)



class Person:
    def __init__(self, name, age, salary):
        self.name = name # Публичный
        self._age = age  # Защищенный
        self.__salary = salary # Приватный

    @property
    def age(self):
        return self._age
        
    @age.setter
    def age(self,value):
        if value > 0:
            self._age = value
        else:
            raise ValueError("Возраст должен быть положительным числом")
    

    @property 
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self,value):
        if value >= 0:
            self.__salary = value
        else:
            raise ValueError("Зарплата не может быть отрицательной!")
        

person = Person("Kamola Nimatulaeva", 32, 50000)
print("Имя:", person.name)
print("Возраст до изменения:", person.age)
person.age = 65
print("Возраст после изменения:", person.age)

print("Зп до изменения:", person.salary)
person.salary = 65000
print("Зп после изменения:", person.salary)


class Animal:
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        return "Мяу"
    
class Dog(Animal):
    def speak(self):
        return "Гав"
    
class Cow(Animal):
    def speak(self):
        return "Му"
    
animals = [Cat(), Dog(), Cow()]
for animal in animals:
    print(animal.speak())


class Vehicle:
    def move(self):
        raise NotImplementedError("Этот метод должен быть переопределен в дочерних классах!")
    
class Car(Vehicle):
    def move(self):
        return "Автомобиль едет по дороге"
    
class Plane(Vehicle):
    def move(self):
        return "Самолет летит в небе"
    
vehicles = [Car(), Plane()]
for i in vehicles:
    print (i.move())
