# ООП - Объектно-ориентированное программирование
"Наследование"

class Game: # parent class
    def __init__(self, game_name, game_year, company, graphics):
        self.game_name = game_name
        self.game_year = game_year
        self.company = company
        self.graphics = graphics
    def info(self):
        print(f"Game - {self.game_name} - {self.game_year} - {self.company} - {self.graphics} - {self.multiplayer}")

# game = Game("Mortal Combat", 2014, "Midway Games", "4K")
# game.info()

class Roblox(Game):
    def __init__(self, game_name, game_year, company, graphics, multiplayer):
        super().__init__(game_name, game_year, company, graphics)
        # Game().__init__(game_name, game_year, company, graphics)
        self.multiplayer = multiplayer

        self.name ="Player"
        self.gender = "None"
        self.skin = "None"
        self.hp = 100

    def info(self):
        return super().info()
    
    def info_player(self):
        print(f"Игрок - {self.name}\nПол - {self.gender}\nОблик - {self.skin}\nЗдоровье - {self.hp}")
    
    def edit_player(self):
        name = input("Введите свое имя:")
        gender = input("Введите свой пол:")
        skin = input("Введите свой облик:")
        self.name = name
        self.gender = gender
        self.skin = skin
    
# roblox = Roblox("Roblox", 2006, "Roblox Corp.", "FULL HD", 8)
# roblox.info()
# roblox.edit_player()
# roblox.info_player()

class Strike(Roblox):
    def __init__(self, game_name, game_year, company, graphics, multiplayer):
        super().__init__(game_name, game_year, company, graphics, multiplayer)
    
    def info(self):
        return super().info()
    
    def info_player(self):
        return super().info_player()
    
    def edit_player(self):
        return super().edit_player()
    

strike = Strike("Strike", 2007, "Roblox Corp", "FULL HD", 9)
strike.info()
strike.edit_player()
strike.info_player()

