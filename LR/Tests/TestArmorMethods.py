import unittest
from Armor.Armor import Armor


class TestArmorMethods(unittest.TestCase):

    def test_check_stamina(self):
        armor = Armor("Броня", 40, 100)
        armor.check_stamina(1)
        self.assertEqual(armor.stamina, 90)
        armor.check_stamina(0)
        self.assertEqual(armor.stamina, 80)
