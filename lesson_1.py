# ООП - Объектно-ориентированное программирование

# class Car: #шаблон или чертеж
#     def __init__(self, motor, wheel, body): # __init__ - конструктор
#         self.motor = motor # self - ссылка на текущий объект
#         self.wheel = wheel
#         self.body = body # атрибут класса

#         self.bak = 10 
#         self.is_start = False # Флажок

#     def info(self): # функция внутри класса превращается в метод
#         print(f"Мотор - {self.motor} Колесо - {self.wheel} Кузов - {self.body}")
#     def start(self):
#         if self.bak > 0:
#             self.is_start = True
#             print("Машина заведена ")
#         else:
#             print("У машины нет топлива")
#     def stop(self):
#         self.is_start = False
#         print("Машина заглушена")
    
#     def drive(self,city):
#         if self.is_start == True:
#             print(f"Машина едет в {city}")
#         else:
#             print("Машина не заведена")


# car = Car("V6", "R20", "Sky") # экземпляр класса
# car.info()
# car.start()
# car.stop()
# car.drive("Dubai")

class Book:
    def __init__(self, avtor, book_name, year):
        self.avtor = avtor
        self.book_name = book_name
        self.year = year
    def info(self):
        print(f"Автор - {self.avtor} Название - {self.book_name} Год выпуска - {self.year}")

book = Book("Агата Кристи", "Десять негритят", "1939")
book.info()
