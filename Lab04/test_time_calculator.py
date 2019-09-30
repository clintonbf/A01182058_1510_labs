import io
from unittest import TestCase
from Lab04 import time_calculator
from unittest.mock import patch


class TestTime_calculator(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_time_calculator_1(self, mock_output):
        expected_output = 'We have 0 days, 0 hours, 0 minutes and 1 seconds\n'
        time_calculator.time_calculator(1)
        self.assertEqual(mock_output.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_time_calculator_60(self, mock_output):
        expected_output = 'We have 0 days, 0 hours, 1 minutes and 0 seconds\n'
        time_calculator.time_calculator(60)
        self.assertEqual(mock_output.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_time_calculator_3600(self, mock_output):
        expected_output = 'We have 0 days, 1 hours, 0 minutes and 0 seconds\n'
        time_calculator.time_calculator(3600)
        self.assertEqual(mock_output.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_time_calculator_86400(self, mock_output):
        expected_output = 'We have 1 days, 0 hours, 0 minutes and 0 seconds\n'
        time_calculator.time_calculator(86400)
        self.assertEqual(mock_output.getvalue(), expected_output)

