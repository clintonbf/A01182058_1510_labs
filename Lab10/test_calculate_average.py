from unittest import TestCase

from Lab10.question_07 import calculate_average


class TestCalculate_average(TestCase):
    def test_calculate_average_where_no_decimal_created(self):
        self.assertEqual(calculate_average({'a': 1, 'b': 2, 'c': 3}), 2)

    def test_calculate_average_with_repeating_decimal(self):
        self.assertEqual(calculate_average({'a': 3, 'b': 3, 'c': 4}), 3.3)
