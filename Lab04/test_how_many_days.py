from unittest import TestCase
from Lab04 import time_calculator


class TestHow_many_days(TestCase):
    def test_how_many_days(self):
        self.assertEqual(0, time_calculator.how_many_days(700))
        self.assertEqual(1, time_calculator.how_many_days(86400))
        self.assertEqual(1, time_calculator.how_many_days(95000))
        self.assertEqual(2, time_calculator.how_many_days(172800))
