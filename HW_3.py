
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def info(self):
        print(f"Транспортное средство {self.brand} модели {self.model} {self.year} года выпуска")

# vehicle = Vehicle("BMW", "X5", 1999)
# vehicle.info()


class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors
        

    def info(self):
        print(f"Автомобиль {self.brand} модели {self.model} {self.year} года выпуска.Количество дверей: {self.doors}.")
    
       
        self.bak = 10
        self.engine = True
    def start_engine(self):
        if self.bak > 0:
           self.engine = True
           print("Двигатель заведен")
        else:
            print("Двигатель не заведен")

        
    
# car = Car("Mercedez Benz", "S - class", 1972, 4)
# car.info()
# car.start_engine()


class Bike(Vehicle):
    def __init__(self, brand, model, year, type):
        super().__init__(brand, model, year)
        self.type = type
    def info(self):
        print(f"Мотоцикл {self.brand} {self.model} модели,{self.year} года выпуска, тип: {self.type}")

        self.bak = 10
        self.engine = True
    def start_engine(self):
        if self.bak > 0:
           self.engine == True
           print("Двигатель заведен")
        else:
            print("Двигатель не заведен")
        
    
bike = Bike( "Yamaha", "YZF r1", 1988, "спорт" )
bike.info()
bike.start_engine()


        