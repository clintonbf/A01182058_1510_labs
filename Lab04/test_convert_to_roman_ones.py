from unittest import TestCase
from Lab04 import roman_numbers

class TestConvert_to_roman_ones(TestCase):
    def test_convert_to_roman_ones_lt_4(self):
        self.assertEqual(roman_numbers.convert_to_roman_ones(2), "II")

    def test_convert_to_roman_ones_eq_4(self):
        self.assertEqual(roman_numbers.convert_to_roman_ones(4), "IV")

    def test_convert_to_roman_ones_eq_5(self):
        self.assertEqual(roman_numbers.convert_to_roman_ones(5), "V")

    def test_convert_to_roman_ones_gt_5(self):
        self.assertEqual(roman_numbers.convert_to_roman_ones(7), "VII")

    def test_convert_to_roman_ones_eq_9(self):
        self.assertEqual(roman_numbers.convert_to_roman_ones(9), "IX")
