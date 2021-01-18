from Weapon.Weapon import Weapon
import random


class Bow(Weapon):

    def __init__(self, name, damage, chance):
        Weapon.__init__(self, name, damage)
        self.__chance = chance

    def bowdamage(self):
        return self.damage * (self.__chance * 0.01)

    def attack(self):
        chance_attack = self.__chance * 0.01
        rn = random.uniform(0, 1)
        if rn <= chance_attack:
            return self.bowdamage()
        else:
            return 0

    def __str__(self):
        return f"{Weapon.__str__(self)}, шанс попадания - {self.__chance}"