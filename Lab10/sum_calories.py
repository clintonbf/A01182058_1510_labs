import io
from unittest import TestCase
from unittest.mock import patch

from Lab10.question_07 import sum_calories


class TestOutput_calorie_sum(TestCase):
    def test_sum_calories_two_items_all_above_0_cal(self):
        self.assertEqual(sum_calories({'a': 1, 'b': 2}), 3)

    def test_sum_calories_1_item_0_cal(self):
        self.assertEqual(sum_calories({'a': 0}), 0)

    def test_sum_calories_1_item_gt_0_cal(self):
        self.assertEqual(sum_calories({'a': 5}), 5)

    def test_sum_calories_gt_1_item_with_1_item_of_0_cal(self):
        self.assertEqual(sum_calories({'a': 50, 'b': 0}), 50)
