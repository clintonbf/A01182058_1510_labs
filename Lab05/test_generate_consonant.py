from unittest import TestCase

from Lab05 import Lab_05


class TestGenerate_consonant(TestCase):
    def test_generate_consonant(self):
        my_consonant = Lab_05.generate_consonant()

        self.assertIn(my_consonant,
                      ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x',
                       'y',
                       'z'])
