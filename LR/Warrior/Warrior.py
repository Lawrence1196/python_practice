class Warrior:
    count = 3

    def __init__(self, name, strength=20, health=100):
        self.name = name
        self.strength = strength
        self.health = health

    def setWeapon(self, weapon):
        self.weapon = weapon

    def __str__(self):
        return f"{self.name}, сила - {self.strength}, осталось здоровья - {self.health} HP"

    def __del__(self):
        print('Valhalla... %s is coming' % self.name)