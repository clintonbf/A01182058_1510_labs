import io
from unittest import TestCase
from unittest.mock import patch

import midterm


class TestDie_thing(TestCase):
    @patch('random.randint', side_effect=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    @patch('builtins.input', side_effect=[1, 10])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_die_thing_only_ones_rolled(self, mock_output, mock_input, mock_roll):
        midterm.die_thing()

        self.assertIn("Here's what I rolled:\n1 : 10", mock_output.getvalue())