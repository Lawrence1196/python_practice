
class Effects():
    __burn = 0
    __freeze = 0
    stopfight_count = 0

    def burn(self):
        self.__burn = 1

    def freeze(self):
        self.__freeze = 1

    def burn_attack(self, warrior):
        if self.__burn == 1:
            print('%s-й воин только что был подожжен!' % warrior.name)
            return self.attack() + warrior.health * 0.05
        else:
            return self.attack()

    def freeze_attack(self, warrior):
        if warrior.count <= 0:
            warrior.count = 3
        if self.__freeze == 1:
            print('%s-й воин был заморожен и не может атаковать еще %s ход(а)!' % (warrior.name, warrior.count - 1))
            warrior.weapon[0].stopfight_count = warrior.count - 1
            warrior.count -= 1
        else:
            warrior.weapon[0].stopfight_count = 0

    def effects_print(self):
        return f"эффект поджога - {self.__burn}, эффект заморозки - {self.__freeze}"
