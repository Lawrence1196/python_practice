import unittest
from Weapon.Bow import Bow


class TestBowMethods(unittest.TestCase):

    def test_bowdamage(self):
        bow = Bow("Лук", 10, 100)
        self.assertEqual(bow.damage, 10)

    def test_attack(self):
        bow = Bow("Лук", 20, 100)
        self.assertEqual(bow.damage, 20)

    def test_le1(self):
        bow1 = Bow("Лук1", 40, 100)
        bow2 = Bow("Лук2", 10, 100)
        self.assertFalse(bow1.__le__(bow2))

    def test_le2(self):
        bow1 = Bow("Лук1", 40, 100)
        bow2 = Bow("Лук2", 10, 100)
        self.assertTrue(bow2.__le__(bow1))



if __name__ == '__main__':
    unittest.main()
