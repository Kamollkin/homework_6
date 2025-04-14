
class Animal():
  def __init__(self, name):
    self.name = name
  def eat(self):
    print(f"Животное  {self.name} ест")
  def sleep(self):
    print(f"Животное  {self.name} спит")

animal = Animal("Медведь")
animal.eat()
animal.sleep()
    
class Walker(Animal):
  def __init__(self, name):
    super().__init__(name)
  def walk(self):
    print(f"{self.name} ходит")

walker = Walker("Шимпанзе")
walker.walk()

class Swimmer(Animal):
  def __init__(self, name):
    super().__init__(name)
  def swim(self):
    print(f"{self.name} плавает")

swimmer = Swimmer("Кит")
swimmer.swim()


# class Flyer(Animal):
#   def __init__(self, name):
#     super().__init__(name)
#   def fly(self):
#     print(f"{self.name} летает")

# flyer = Flyer("Орел")
# flyer.fly()

# class Penguin(Walker,Swimmer):
#   def __init__(self, name):
#     super().__init__(name)
  
#   def swim(self):
#     return super().swim()
#   def walk(self):
#     return super().walk()
#   def describe(self):
#     print(f"{self.name} может ходить и плавать")


# penguin = Penguin("Пингвин")
# penguin.walk()
# penguin.swim()
# penguin.describe()


# class Duck(Walker,Swimmer,Flyer):
#   def __init__(self, name):
#     super().__init__(name)
#   def walk(self):
#     return super().walk()
#   def swim(self):
#     return super().swim()
#   def fly(self):
#     return super().fly()
#   def describe(self):
#     print(f"{self.name} может ходить, плавать и летать")

# duck = Duck("Утка")
# duck.walk()
# duck.swim()
# duck.fly()
# duck.describe()

# class Bat(Flyer):
#   def __init__(self, name):
#     super().__init__(name)
#   def fly(self):
#     return super().fly()
#   def describe(self):
#     print(f"{self.name} может летать")
  
# bat = Bat("Летучая мышь")
# bat.fly()
# bat.describe()

