import io
from unittest import TestCase
from unittest.mock import patch

from Lab10.question_07 import output_calorie_sum


class TestOutput_calorie_sum(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_output_calorie_sum_two_items_all_above_0_cal(self, mock_output):
        expected_output = "Total calories: 3\n"

        output_calorie_sum({'a': 1, 'b': 2})

        self.assertEqual(mock_output.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_output_calorie_sum_1_item_0_cal(self, mock_output):
        expected_output = "Total calories: 0\n"

        output_calorie_sum({'a': 0})

        self.assertEqual(mock_output.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_output_calorie_sum_1_item_gt_0_cal(self, mock_output):
        expected_output = "Total calories: 5\n"

        output_calorie_sum({'a': 5})

        self.assertEqual(mock_output.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_output_calorie_sum_gt_1_item_with_1_item_of_0_cal(self, mock_output):
        expected_output = "Total calories: 50\n"

        output_calorie_sum({'a': 50, 'b': 0})

        self.assertEqual(mock_output.getvalue(), expected_output)
