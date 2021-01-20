from Warrior.Warrior import Warrior
from Weapon.Bow import Bow
from Weapon.Sword import Sword
import random
import copy

if __name__ == "__main__":
    warrior1 = Warrior('Воин1',10)
    warrior2 = Warrior('Воин2')
    warrior3 = Warrior('Воин3',30)
    warriors = [warrior1, warrior2, warrior3]
    copy_warriors = []

    bow1 = Bow("Лук1", 30, 50)
    bow2 = Bow("Лук2", 10, 90)
    bow3 = Bow("Лук3", 5, 100)
    sword1 = Sword("Меч1", 40, 1)
    sword2 = Sword("Меч2", 20, 1)
    sword3 = Sword("Меч3", 10, 1)
    weapons = [bow1, bow2, bow3, sword1, sword2, sword3]

    thebest = 0
    for i in range(len(weapons)):
        if (weapons[thebest].__le__(weapons[i])):
            thebest = i

    number_of_weapons = random.randint(1, 2)
    for i in range(len(warriors)):
        random.shuffle(weapons)
        warriors[i].setWeapon(weapons[:number_of_weapons])

    while True:
        if len(warriors) == 1:
            print('Победил %s' % str(warriors[0]))
            break
        x = random.choice(warriors)
        y = random.choice(warriors)
        if x != y:
            print('%s атакует %s' % (x.name, y.name))
            y.health -= x.strength
            print('У %s осталось %s HP \n' % (y.name, y.health))
            copy_warriors = copy.copy(warriors)
            for i in range(len(copy_warriors)):
                if (copy_warriors[i].health <= 0):
                    warriors[i].__del__()
                    warriors.pop(i)
            if y.health <= 0:
                print('%s погиб от рук %s\n' % (x.name, y.name))
                warriors.remove(x)