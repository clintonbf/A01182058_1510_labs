from unittest import TestCase
from Lab04 import roman_numbers


class TestConvert_to_roman_thousands(TestCase):
    def test_convert_to_roman_thousands(self):
        self.assertEqual(roman_numbers.convert_to_roman_thousands(2), "MM")
