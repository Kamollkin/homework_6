
class BankAccount:
    def __init__(self, owner, balance):
         self._owner = owner
         self._balance = 0

    def get_owner(self):
        return self._owner
    
    
    
    def deposit(self,amount):
        self._balance += amount
    
    def withdraw(self,amount):
        if self._balance >= amount:
            self._balance -= amount

    def get_balance(self):
        return self._balance

    def set_owner(self,name):
        self._owner = name 
       


    def set_balance(self, amount):
        self._balance = amount
        if amount < 0:
            print("Невозможно установить отрицательный баланс!")

    

bankaccount = BankAccount("Kamola", 0)
# bankaccount.deposit(60)
# bankaccount.withdraw(50)
# print(bankaccount.get_owner())
# bankaccount.set_owner("Hilola")
# print(bankaccount.get_owner())
# print(bankaccount.get_balance())
bankaccount.set_balance(100)
bankaccount.deposit(60)
bankaccount.withdraw(50)
print(bankaccount.get_balance())
