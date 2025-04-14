class Transport:
    def __init__(self, speed):
        self._speed = speed
    
    def move(self):
        return f"Транспорт  начал движение"
    
class Car(Transport):
    def __init__(self, speed):
        super().__init__(speed)
    
    def get_speed(self):
        return self._speed
    
    def move(self):
        return f"Автомобиль едет по дороге, со скоростью - {self._speed} км/ч"
    
    def set_speed(self,speed_new):
        self._speed=speed_new
        print(f"Автомобиль теперь едет по дороге, со скоростью - {self._speed} км/ч")

class Bicycle(Transport):
    def __init__(self, speed):
        super().__init__(speed)
    
    def get_speed(self):
        return self._speed
    
    def move(self):
        return f"Велосипед катится по велодорожке, со скоростью - {self._speed} км/ч" 
        
    def set_speed(self,speed_new):
        self._speed=speed_new
        print(f"Велосипед теперь едет по дороге, со скоростью - {self._speed} км/ч")
    
transport_list = [Car(90), Bicycle(30)]
for transport in transport_list:
    print(transport.move())
    print(f"Скорость: {transport.get_speed()} км/ч\n")


# transport_list[0].set_speed(80)
# transport_list[1].set_speed(20)