import io
import sys
from unittest import TestCase
from unittest.mock import patch

from Lab05 import Lab_05


class TestPrint_character(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_attributes(self, mock_output):
        test_list = ["Gandalf", ["Strength", 1], ["Dexterity", 2], ["Constitution", 3], ["Intelligence", 4],
                     ["Wisdom", 5], ["Charisma", 6]]

        expected_output = ("Gandalf\n"
                           "Strength: 1!\n"
                           "Dexterity: 2!\n"
                           "Constitution: 3!\n"
                           "Intelligence: 4!\n"
                           "Wisdom: 5!\n"
                           "Charisma: 6!\n")
        Lab_05.print_character(test_list)

        self.assertEqual(mock_output.getvalue(), expected_output)
