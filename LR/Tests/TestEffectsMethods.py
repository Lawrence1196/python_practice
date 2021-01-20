import unittest
from Warrior.Warrior import Warrior
from Weapon.Sword import Sword
from Armor.Armor import Armor


class TestEffectsMethods(unittest.TestCase):

    def test_burn_attack1(self):
        armor = Armor("Броня", 100, 100)
        weapon = Sword("Меч1", 50, 1)
        warrior = Warrior('1', 3, 100)
        warrior.setArmor(armor)
        warrior.setWeapon(weapon)
        self.assertEqual(warrior.weapon.burn_attack(warrior), 50)

    def test_burn_attack2(self):
        armor = Armor("Броня", 100, 100)
        weapon = Sword("Меч1", 50, 1)
        weapon.burn()
        warrior = Warrior('1', 3, 100)
        warrior.setArmor(armor)
        warrior.setWeapon(weapon)
        self.assertEqual(warrior.weapon.burn_attack(warrior), 55)

    def test_burn_attack3(self):
        armor = Armor("Броня", 100, 100)
        armor.burn()
        weapon = Sword("Меч1", 50, 1)
        weapon.burn()
        warrior = Warrior('1', 3, 100)
        warrior.setArmor(armor)
        warrior.setWeapon(weapon)
        self.assertEqual(warrior.weapon.burn_attack(warrior), 0)

    def test_freeze_attack1(self):
        armor = Armor("Броня", 100, 100)
        weapon1 = Sword("Меч1", 50, 1)
        weapon2 = Sword("Меч1", 50, 1)
        list = [weapon1, weapon2]
        warrior = Warrior('1', 3, 100)
        warrior.setArmor(armor)
        warrior.setWeapon(list)
        warrior.weapon[0].freeze_attack(warrior)
        self.assertEqual(warrior.weapon[0].stopfight_count, 0)

    def test_freeze_attack2(self):
        armor = Armor("Броня", 100, 100)
        weapon1 = Sword("Меч1", 50, 1)
        weapon1.freeze()
        weapon2 = Sword("Меч1", 50, 1)
        weapon2.freeze()
        list = [weapon1, weapon2]
        warrior = Warrior('1', 3, 100)
        warrior.setArmor(armor)
        warrior.setWeapon(list)
        warrior.weapon[0].freeze_attack(warrior)
        self.assertEqual(warrior.weapon[0].stopfight_count, 2)

    def test_freeze_attack3(self):
        armor = Armor("Броня", 100, 100)
        armor.freeze()
        weapon1 = Sword("Меч1", 50, 1)
        weapon1.freeze()
        weapon2 = Sword("Меч1", 50, 1)
        weapon2.freeze()
        list = [weapon1, weapon2]
        warrior = Warrior('1', 3, 100)
        warrior.setArmor(armor)
        warrior.setWeapon(list)
        warrior.weapon[0].freeze_attack(warrior)
        self.assertEqual(warrior.weapon[0].stopfight_count, 0)
