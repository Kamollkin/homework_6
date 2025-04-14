# Number 1


class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    
    def introduce(self):
        print(f'Привет! Меня зовут {self.name}, мне {self.age} лет (год/а). Проживаю в городе {self.city}.')
    
person1 = Person("Хилола", 55, "Стамбул")
person1.introduce()

person2 = Person("Айсалкын", "31", "Стамбул")
person2.introduce()

person3 = Person("Камола", 32, "Ош")    
person3.introduce()  

# Number 2

class Car:
    def __init__(self, brand:str, model:str, year: int):
        self.brand = brand
        self.model = model
        self.year = year
        
        self.vozrast = 2025 - int(self.year)
       
    def info(self):
        print(f'Автомобиль {self.brand} {self.model}, {self.year} года выпуска')

    def is_old(self):
        if self.vozrast > 10:
            print(True)
        else:
            print(False)

car1 = Car("BMW", "X5 M", 2020)
car1.info()
car1.is_old()

car2 = Car("Mercedes Benz", "A class", 2000)
car2.info()
car2.is_old()


# Number 3
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = 0
        print(f"Hello {self.owner}! Welcome to your bank account!")

    def deposit(self):
        summa = float(input("Enter the amount to be deposited:"))
        self.balance += summa
        print("Amount Deposited:", summa)
    def withdraw(self):
        summa = float(input("Enter the amount to be withdrawn:"))
        if self.balance >= summa:
           self.balance -= summa
           print("Amount Withrdrawn:", summa)
        elif self.balance < summa:
            print("You do not have enough amount on your balance!")
           

    def show_balance(self):
        print(f"Dear {self.owner}, your balance is:", self.balance)
    

bank = BankAccount("Kamola", 0)
bank.deposit()
bank.withdraw()
bank.show_balance()
    
