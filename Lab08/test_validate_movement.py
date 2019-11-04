from unittest import TestCase

from Lab08.maze import validate_movement


class TestValidate_movement(TestCase):
    def test_validate_movement_with_valid_input(self):
        movements = ('n', 's', 'e', 'w')

        for movement in movements:
            self.assertTrue(validate_movement(movement))

    def test_validate_movement_with_valid_input_in_caps(self):
        movements = ('N', 'S', 'E', 'W')

        for movement in movements:
            self.assertTrue(validate_movement(movement))

    def test_validate_movement_with_invalid_input(self):
        movements = ('North', '1', 'g', 'north')

        for movement in movements:
            self.assertFalse(validate_movement(movement))
