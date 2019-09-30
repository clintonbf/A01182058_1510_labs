from unittest import TestCase
from Lab04 import roman_numbers

class TestConvert_to_roman_tens(TestCase):
    def test_convert_to_roman_tens_eq_1(self):
        self.assertEqual(roman_numbers.convert_to_roman_tens(1), "X")

    def test_convert_to_roman_tens_eq_4(self):
        self.assertEqual(roman_numbers.convert_to_roman_tens(4), "XL")

    def test_convert_to_roman_tens_eq_5(self):
        self.assertEqual(roman_numbers.convert_to_roman_ones(5), "L")

    def test_convert_to_roman_tens_gt_5(self):
        self.assertEqual(roman_numbers.convert_to_roman_tens(7), "LXX")

    def test_convert_to_roman_tens_eq_9(self):
        self.assertEqual(roman_numbers.convert_to_roman_tens(9), "XC")


