from Effects.Effects import Effects


class Armor(Effects):

    def __init__(self, name, chance, stamina=100):
        self.name = name
        self.chance = chance
        self.stamina = stamina

    def check_stamina(self, count):
        if count == 1:
            print('%s помогает спастись воину от негативного эффекта оружия, но теряет 10 HP прочности' % self.name)
        else:
            print('%s не помогает спастись воину от негативного эффекта оружия и теряет 10 HP прочности' % self.name)
        self.stamina -= 10
        print('Текущая прочность брони: %s HP' % self.stamina)
        if self.stamina <= 0:
            self.__del__()

    def __str__(self):
        return f"{self.name},с шансом против негативных эффектов – {self.chance} %,прочностью – {self.stamina} НР,против: {self.effects_print()}"

    def __del__(self):
        print('%s развалилась!' % self.name)
