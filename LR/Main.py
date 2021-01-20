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
        if random.choice([True, False]) == True:
            weapons[i].freeze()
        if random.choice([True, False]) == True:
            weapons[i].burn()
        if (weapons[thebest].__le__(weapons[i])):
            thebest = i

    number_of_weapons = random.randint(1, 2)
    for i in range(len(warriors)):
        random.shuffle(weapons)
        warriors[i].setWeapon(weapons[:number_of_weapons])

    while True:
        while True:
            x = random.choice(warriors)
            if x.weapon[0].stopfight_count == 0:
                break
            print('На %s действует заморозка %s ход(а)' % (
            x.name, x.weapon[0].stopfight_count))
        y = random.choice(warriors)
        if x != y and x.weapon[0].stopfight_count == 0:
            print('%s атакует %s' % (x.name, y.name))
            if not x.weapon:
                print('У %s нет оружия' % x.name)
                y.health -= x.strength
                print('%s нанес %s урона' % (x.name, x.strength))
            else:
                print('Оружие, которое наносит урон: %s' % x.weapon[0].name)
                y.health -= x.weapon[0].burn_attack(y)
                x.weapon[0].freeze_attack(y)
                if type(x.weapon[0]) == Sword and x.weapon[0].stamina == 0:
                    print('У %s сточился меч' % x.name)
                    x.weapon.pop(0)
            print('У %s осталось %s HP \n' % (y.name, y.health))

            copy_unit_list = copy.copy(warriors)
            for i in range(len(copy_unit_list)):
                if (copy_unit_list[i].health <= 0):
                    weapon_of_dead = warriors[i].weapon
                    print('%s получает все оружие %s:' % (x.name, y.name))
                    for j in range(len(weapon_of_dead)):
                        x.weapon.append(weapon_of_dead[j])
                        print('%s' % weapon_of_dead[j].__str__())
                    warriors[i].__del__()
                    warriors.pop(i)

            if len(warriors) == 1:
                print('\nПобедил %s' % str(warriors[0]))
                break