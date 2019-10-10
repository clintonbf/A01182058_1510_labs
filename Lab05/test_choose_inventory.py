import io
from unittest import TestCase
from unittest.mock import patch

from Lab05 import Lab_05

"""Test cases
inventory size = 0
selection = 0
selection < 0
selection > len(inventory)
selection == len(inventory)
"""

class TestChoose_inventory(TestCase):
    def test_choose_inventory_inventory_empty(self):
        return_list = Lab_05.choose_inventory([], 4)
        self.assertEqual(len(return_list), 0)

    def test_choose_inventory_selection_0(self):
        return_list = Lab_05.choose_inventory(['bucket'], 0)
        self.assertEqual(len(return_list), 0)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_inventory_selection_lt_0(self, mock_output):
        expected_output = 'Error: selection < 0 is NOT permitted.\n'
        Lab_05.choose_inventory(['bucket'], -1)
        self.assertEqual(mock_output.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_inventory_selection_gt_inventory_length(self, mock_output):
        expected_output = "Getting greedy. Venger would be proud.\n"

        Lab_05.choose_inventory(['bucket'], 2)
        self.assertEqual(mock_output.getvalue(), expected_output)

    @patch('random.choice', side_effect=['c', 'a', 'd', 'b'])
    def test_choose_inventory_ok_inventory_ok_selection(self, mock_inventory):
        expected_output = ['a', 'b', 'c', 'd']

        self.assertEqual(Lab_05.choose_inventory(['b', 'a', 'd', 'c', 'e', 'f', 'boo'], 4), expected_output)

    @patch('random.choice', side_effect=['c', 'a', 'd', 'b'])
    def test_choose_inventory_inventory_size_eq_selection(self, mock_inventory):
        expected_output = ['a', 'b', 'c', 'd']

        self.assertEqual(Lab_05.choose_inventory(['b', 'a', 'd', 'c'], 4), expected_output)
