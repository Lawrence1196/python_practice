from Warrior.Warrior import Warrior
import random
import copy

if __name__ == "__main__":
    warrior1 = Warrior('Воин1',10)
    warrior2 = Warrior('Воин2')
    warrior3 = Warrior('Воин3',30)
    warriors = [warrior1, warrior2, warrior3]
    copy_warriors = []

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