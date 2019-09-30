from unittest import TestCase
from Lab04 import time_calculator


class TestHow_many_minutes(TestCase):
    def test_how_many_minutes_lt_1(self):
        self.assertEqual(0, time_calculator.how_many_minutes(40))

    def test_how_many_minutes_eq_1(self):
        self.assertEqual(1, time_calculator.how_many_minutes(60))

    def test_how_many_minutes_gt_1_lt_2(self):
        self.assertEqual(1, time_calculator.how_many_minutes(85))

    def test_how_many_minutes_eq_2(self):
        self.assertEqual(2, time_calculator.how_many_minutes(120))
