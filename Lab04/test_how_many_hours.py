from unittest import TestCase
from Lab04 import time_calculator


class TestHow_many_hours(TestCase):
    def test_how_many_hours(self):
        self.assertEqual(0, time_calculator.how_many_hours(1400))
        self.assertEqual(1, time_calculator.how_many_hours(3600))
        self.assertEqual(1, time_calculator.how_many_hours(5000))
        self.assertEqual(2, time_calculator.how_many_hours(7200))
