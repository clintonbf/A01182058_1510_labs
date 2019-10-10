from unittest import TestCase

from Lab05 import Lab_05


class TestGenerate_vowel(TestCase):
    def test_generate_vowel(self):
        my_vowel = Lab_05.generate_vowel()

        self.assertIn(my_vowel, ['a', 'e', 'i', 'o', 'u', 'y'])
