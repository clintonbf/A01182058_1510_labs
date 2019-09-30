from unittest import TestCase
from Lab04 import time_calculator


class TestHow_many_hours(TestCase):
    def test_how_many_hours__lt_0(self):
        self.assertEqual(0, time_calculator.how_many_hours(1400))

    def test_how_many_hours_eq_1(self):
        self.assertEqual(1, time_calculator.how_many_hours(3600))

    def test_how_many_hours_gt_1_lt_2(self):
        self.assertEqual(1, time_calculator.how_many_hours(5000))

    def test_how_many_hours_eq_2(self):
        self.assertEqual(2, time_calculator.how_many_hours(7200))
