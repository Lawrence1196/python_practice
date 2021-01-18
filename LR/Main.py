import random

from Warrior.Warrior import Warrior

if __name__ == "__main__":
    warrior1 = Warrior('Воин1')
    warrior2 = Warrior('Воин2')
    warrior3 = Warrior('Воин3')
    warriors = [warrior1, warrior2, warrior3]

    while True:
        if len(warriors) == 1:
            print(warriors[0].name + ' победил')
            break
        x = random.choice(warriors)
        y = random.choice(warriors)
        if x != y:
            print('%s атакует %s' % (x.name, y.name))
            y.health -= 20
            print('У %s осталось %s HP \n' % (y.name, y.health))
            if y.health <= 0:
                print('%s погиб от рук %s\n' % (x.name, y.name))
                warriors.remove(x)
