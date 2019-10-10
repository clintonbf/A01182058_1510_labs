from unittest import TestCase
from Lab05 import Lab_05


class TestGenerate_name(TestCase):

    def test_generate_name_returns_list(self):
        test_list = Lab_05.generate_name(4)

        self.assertIsInstance(test_list, list)

    def test_generate_name_correct_length(self):
        test_list = Lab_05.generate_name(4)

        self.assertEqual(len(test_list), 4)
