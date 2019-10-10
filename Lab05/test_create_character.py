from unittest import TestCase

from Lab05 import Lab_05

"""Things to verify
"""

class TestCreate_character(TestCase):
    def test_create_character_is_7_elements(self):
        my_char = Lab_05.create_character(5)

        self.assertEqual(len(my_char), 11)
