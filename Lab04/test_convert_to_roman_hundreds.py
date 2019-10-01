from unittest import TestCase
from Lab04 import roman_numbers


class TestConvert_to_roman_hundreds(TestCase):
    def test_convert_to_roman_hundreds_lt_4(self):
        self.assertEqual(roman_numbers.convert_to_roman_hundreds(2), "CC")

    def test_convert_to_roman_hundreds_eq_4(self):
        self.assertEqual(roman_numbers.convert_to_roman_hundreds(4), "CD")

    def test_convert_to_roman_hundreds_eq_5(self):
        self.assertEqual(roman_numbers.convert_to_roman_hundreds(5), "D")

    def test_convert_to_roman_hundreds_gt_5(self):
        self.assertEqual(roman_numbers.convert_to_roman_hundreds(7), "DCC")

    def test_convert_to_roman_hundreds_eq_9(self):
        self.assertEqual(roman_numbers.convert_to_roman_hundreds(9), "CM")
