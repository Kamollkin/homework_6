class Transport:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    
    def info(self):
        print(f"Транспорт марки - {self.brand}, скорость: {self.speed}") 
    
    def move(self):
        return f"Транспорт движется"
    
    
class Car(Transport):
    def __init__(self, brand, speed):
        super().__init__(brand, speed)
        
    
    def info(self):
        print(f"Машина  марки {self.brand} имеет скорость {self.speed} km/h")
    
    def move(self):
        return f"Машина едет по дороге"
    
    def honk(self):
       print(f"Машина сигналит")
    

class Bicycle(Transport):
    def __init__(self, brand, speed):
        super().__init__(brand, speed)
        

    def info(self):
        print(f" Велосипед марки {self.brand} имеет скорость {self.speed} km/h")
    
    def move(self):
        return f"Велосипед едет по тропинке"
    
    def ring_bell(self):
        print(f"Велосипед звенит звонком")
    

class Airplane(Transport):
    def __init__(self, brand, speed):
        super().__init__(brand, speed)
        

    def info(self):
        print(f"Cамолет марки {self.brand} имеет скорость {self.speed} km/h")

    def move(self):
        return f"Самолет летит в небе"
    
    def take_off(self):
        print(f"Самолет взлетает")
    
transport = [Car("BMW", 90), Bicycle("Red",10), Airplane("Boing", 200)]
for i in transport:
    print(i.move())
    print(i.info())

transport1 = Car("BMW", 90)
transport1.honk()

transport2 = Bicycle("Red", 10)
transport2.ring_bell()

transport3 = Airplane("Boing", 200)
transport3.take_off()

        
    

