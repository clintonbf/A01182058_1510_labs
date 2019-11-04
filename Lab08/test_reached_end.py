from unittest import TestCase

from Lab08.maze import reached_end


class TestReached_end(TestCase):
    def test_reached_end_not_at_end(self):
        position = reached_end({'x-coord': 0, 'y-coord': 3})

        self.assertFalse(position)

    def test_reached_end_reached_end(self):
        position = reached_end({'x-coord': 4, 'y-coord': 4})

        self.assertTrue(position)
