from unittest import TestCase
from Lab04 import time_calculator


class TestHow_many_minutes(TestCase):
    def test_how_many_minutes(self):
        self.assertEqual(0, time_calculator.how_many_minutes(40))
        self.assertEqual(1, time_calculator.how_many_minutes(60))
        self.assertEqual(1, time_calculator.how_many_minutes(85))
        self.assertEqual(2, time_calculator.how_many_minutes(120))
