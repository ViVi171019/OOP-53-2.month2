class Hero:

    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def introduce(self):
        print(f"Я герой {self.name}, мой уровень {self.lvl}, моё HP {self.hp}")

# 2 задание
#     Проверяем,готов ли герой к турниру
    def is_adult(self):
        return self.lvl > 10
hero2 = Hero("герой", 12, 120)
if hero2.is_adult():
     print(f"{hero2.name} достаточно опытен для участия в турнире!")
else:
     print(f"{hero2.name} ещё слишком слаб.")