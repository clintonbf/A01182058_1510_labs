from unittest import TestCase

from Lab10.question_07 import calculate_average


class TestCalculate_average(TestCase):
    def test_calculate_average_where_no_decimal_created(self):
        self.assertEqual(calculate_average([1, 2, 3]), 2)

    def test_calculate_average_with_repeating_decimal(self):
        self.assertEqual(calculate_average([3, 3, 4]), 3.33)
