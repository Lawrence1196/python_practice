import unittest
from Weapon.Weapon import Weapon


class TestWeaponMethods(unittest.TestCase):

    def test_damage(self):
        weapon = Weapon("Оружие", 100)
        self.assertEqual(weapon.damage, 100)

    def test_damage_setter(self):
        weapon = Weapon("Оружие", 30)
        self.assertEqual(weapon.damage, 30)
        weapon.damage = 0
        self.assertEqual(weapon.damage, 30)
        weapon.damage = 60
        self.assertEqual(weapon.damage, 60)

    def test_le1(self):
        weapon1 = Weapon("Оружие1", 40)
        weapon2 = Weapon("Оружие2", 20)
        self.assertFalse(weapon1.__le__(weapon2))

    def test_le2(self):
        weapon1 = Weapon("Оружие1", 80)
        weapon2 = Weapon("Оружие2", 10)
        self.assertTrue(weapon2.__le__(weapon1))


if __name__ == '__main__':
    unittest.main()
