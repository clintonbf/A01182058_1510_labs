from unittest import TestCase

from Lab08.maze import create_character


class TestCreate_character(TestCase):
    def test_create_character_contains_dict(self):
        c = create_character()

        self.assertIsInstance(c, dict)

    def test_create_character_coordinates_are_0(self):
        c = create_character()

        for k in c:
            self.assertEqual(c[k], 0)
