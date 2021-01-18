from Weapon.Weapon import Weapon
import random


class Sword(Weapon):

    def __init__(self, name, damage, stamina=1):
        Weapon.__init__(self, name, damage)
        self.stamina = stamina

    def attack(self):
        if random.choice([True, False]) == True:
            self.stamina -= 0.1
        return self.damage * self.stamina

    def __str__(self):
        return f"{Weapon.__str__(self)},уровень целости - {self.stamina}"