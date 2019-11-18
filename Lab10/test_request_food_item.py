from unittest import TestCase
from unittest.mock import patch

from Lab10.question_07 import request_food_item


class TestRequest_food_item(TestCase):
    @patch('builtins.input', return_value='banana')
    def test_request_food_item(self, mock_input):
        input_to_test = request_food_item()

        self.assertEqual(input_to_test, 'banana')
