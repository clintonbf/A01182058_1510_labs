from unittest import TestCase
import random
from unittest.mock import patch

from Lab05 import Lab_05


class TestRoll_die(TestCase):  # (# rolls 1 - 3, # sides > 0)

    def test_roll_die_0_rolls(self):
        self.assertEqual(Lab_05.roll_die(0, 5), 0)

    def test_roll_die_0_sided_die(self):
        self.assertEqual(Lab_05.roll_die(5, 0), 0)

    @patch('random.randint', side_effect=3)
    def test_roll_1_rolls_of_6(self, mock_roll):
        self.assertEqual(Lab_05.roll_die(1, 6), 3)

    @patch('random.randint', side_effect=[4, 4])
    def test_roll_2_rolls_of_6(self, mock_roll):
        self.assertEqual(Lab_05.roll_die(2, 6), 8)

    @patch('random.randint', side_effect=[1, 6, 4])
    def test_roll_3_rolls_of_6(self, mock_roll):
        self.assertEqual(Lab_05.roll_die(3, 6), 11)
