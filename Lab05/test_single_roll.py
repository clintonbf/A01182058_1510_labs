from unittest import TestCase
import random
from unittest.mock import patch
from Lab05 import Lab_05


class TestSingle_roll(TestCase):

    @patch('random.randint', return_value=5)
    def test_single_roll_6_side(self, mock_sides):
        self.assertEqual(Lab_05.single_roll(mock_sides), 5)
