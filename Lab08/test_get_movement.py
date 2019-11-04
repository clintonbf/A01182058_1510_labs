from unittest import TestCase
from unittest.mock import patch

from Lab08.maze import get_movement


class TestGet_movement(TestCase):
    @patch('builtins.input', side_effect=['n'])
    def test_get_movement(self, mock_input):
        dir = get_movement()

        self.assertEqual(dir, 'n')
