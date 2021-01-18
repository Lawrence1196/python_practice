class Warrior:
    def __init__(self, name, strength=20, health=100):
        self.name = name
        self.strength = strength
        self.health = health


    def __str__(self):
        return f"{self.name}, сила - {self.strength}, осталось здоровья - {self.health} HP"

    def __del__(self):
        print('Valhalla... %s is coming' % self.name)