from unittest import TestCase

from Lab05 import Lab_05

class TestCreate_character(TestCase):
    def test_create_character_is_7_elements(self):
        my_char = Lab_05.create_character(5)

        self.assertEqual(len(my_char), 7)

    def test_first_element_is_string(self):
        my_char = Lab_05.create_character(5)

        self.assertIsInstance(my_char[0], str)

    def test_other_elements_are_lists(self):
        my_char = Lab_05.create_character(5)

        for i in range(1, len(my_char)):
            self.assertIsInstance(my_char[i], list)

    def test_attributes_element_0_are_strings(self):
        my_char = Lab_05.create_character(5)

        for i in range(1, len(my_char)):
            self.assertIsInstance(my_char[i][0], str)

    def test_attributes_element_1_are_ints(self):
        my_char = Lab_05.create_character(5)

        for i in range(1, len(my_char)):
            self.assertIsInstance(my_char[i][1], int)
