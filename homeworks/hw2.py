class Hero:
    def __init__(self, name="John Doe", hp=100):
        self.name = name
        self.hp = hp

    def rest(self):
        self.hp += 10
        return f"{self.name} восстанавливает 10 очков здоровья"

    def attack(self):
        return f"{self.name} атакует мечом"

    def status(self):
        return (f'Name: {self.name}\n'
                f'HP: {self.hp}\n')


class Warrior(Hero):

    def __init__(self, name, hp, st):
        super().__init__(name, hp)
        self.st = st

    def attack(self):
        if self.st >= 10:
            self.st -= 10
            return f"{self.name} бросается на противника"
        else:
            return f"Нехватает стамины. Необходимо 10"

    def rest(self):
        self.st += 10
        return f'{self.name} восстанавливает 10 очков стамины'

    def status(self):
        return (f'Name: {self.name}\n'
                f'HP: {self.hp}\n'
                f'Stamina: {self.st}\n')

    def charge(self):
        if self.st >= 20:
            self.st -= 20
            self.hp += 50
            return f'{self.name} повышает здоровье на 50'
        else:
            return f'Нехватает стамины. Необходимо 20'


class Archer(Hero):

    def __init__(self, name, hp, arrows = 30, precision = 10):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        self.arrows -= 1
        if self.arrows != 0:
            if self.precision > 3:
                return f"{self.name} попадает в цель из лука"
            else:
                return f"{self.name} промахивается по цели"
        else:
            return f'Колчан пуст'

    def rest(self):
        self.arrows += 5
        return f'{self.name} восстанавливает 5 стрел'

    def status(self):
        return (f'Name: {self.name}\n'
                f'HP: {self.hp}\n'
                f'Arrows: {self.arrows}\n'
                f'Precision: {self.precision}\n')


class Mage(Hero):

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self.mp = mp

    def attack(self):
        if self.mp >= 10:
            self.mp -= 10
            return f"{self.name} колдует в огненый шар"
        else:
            return f"Нехватает маны. Необходимо: 30"

    def rest(self):
        self.mp += 10
        return f"{self.name} восстанавливает 10 очков маны"

    def status(self):
        return (f'Name: {self.name}\n'
                f'HP: {self.hp}\n'
                f'Mana: {self.mp}\n')

    def teleport(self):
        if self.mp >= 30:
            self.mp -= 30
            return f'{self.name} использовал заклинание телепортации'
        else:
            return f'Нехватает маны. Необходимо: 30'


def hero_actions(obj):
    print(obj.attack())
    print(obj.rest())

hero_persival = Hero('Persival', 10000)
# print(hero_persival.attack())
# print(hero_persival.rest())
print(hero_persival.status())

warrior_rudeus = Warrior('Rudeus', 5000, 400)
# print(warrior_rudeus.attack())
# print(warrior_rudeus.rest())
print(warrior_rudeus.status())

mage_pharsa = Mage('Pharsa', 1000, 4000)
# print(mage_pharsa.attack())
# print(mage_pharsa.rest())
print(mage_pharsa.status())

archer_jett = Archer('Jett', 2000, 60, 10 )
# print(archer_jett.attack())
# print(archer_jett.rest())
print(archer_jett.status())

hero_actions(hero_persival)
hero_actions(warrior_rudeus)
hero_actions(mage_pharsa)
hero_actions(archer_jett)

print(mage_pharsa.teleport())
print(warrior_rudeus.charge())

print(isinstance(mage_pharsa, Hero))



