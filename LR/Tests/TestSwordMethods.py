import unittest
from Weapon.Sword import Sword


class TestSwordMethods(unittest.TestCase):

    def test_attack(self):
        sword = Sword("Меч", 100, 1)
        self.assertEqual(sword.damage, 100)

    def test_le1(self):
        sword1 = Sword("Меч1", 50, 1)
        sword2 = Sword("Меч2", 40, 1)
        self.assertFalse(sword1.__le__(sword2))

    def test_le2(self):
        sword1 = Sword("Меч1", 50, 1)
        sword2 = Sword("Меч2", 40, 1)
        self.assertTrue(sword2.__le__(sword1))


if __name__ == '__main__':
    unittest.main()
