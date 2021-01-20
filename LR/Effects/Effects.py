import random

class Effects():
    __burn = 0
    __freeze = 0
    stopfight_count = 0

    def burn(self):
        self.__burn = 1

    def freeze(self):
        self.__freeze = 1

    def burn_attack(self, warrior):
        if not warrior.armor:
            return self.attack()
        else:
            rn = random.uniform(0, 1)
            if warrior.armor.__burn == 1 and rn <= warrior.armor.chance * 0.01:
                print('%s обладает защитой против огня!' % warrior.armor.name)
                warrior.armor.check_stamina(1)
                return 0
            else:
                if self.__burn == 1:
                    warrior.armor.check_stamina(0)
                    print('%s-й воин только что был подожжен!' % warrior.name)
                    return self.attack() + warrior.health * 0.05
                else:
                    return self.attack()

    def freeze_attack(self, warrior):
        if warrior.armor:
            rn = random.uniform(0, 1)
            if warrior.count <= 0:
                warrior.count = 3
            if warrior.armor.__freeze == 1 and rn <= warrior.armor.chance * 0.01:
                print('%s обладает защитой против заморозки!' % warrior.armor.name)
                warrior.armor.check_stamina(1)
            else:
                if self.__freeze == 1:
                    warrior.armor.check_stamina(0)
                    print('%s-й воин был заморожен и не может атаковать еще %s ход(а)!' % (
                    warrior.name, warrior.count - 1))
                    warrior.weapon[0].stopfight_count = warrior.count - 1
                    warrior.count -= 1
                else:
                    warrior.weapon[0].stopfight_count = 0

    def effects_print(self):
        return f"эффект поджога - {self.__burn}, эффект заморозки - {self.__freeze}"
