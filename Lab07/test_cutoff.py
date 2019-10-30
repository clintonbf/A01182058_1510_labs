from unittest import TestCase

from midterm import cutoff


class TestCutoff(TestCase):
    def test_cutoff_multiples_exist(self):
        my_count = cutoff([9, 9, 9, 4], 3)

        self.assertEqual(my_count, 3)

    def test_cutoff_no_multiples_exist(self):
        my_count = cutoff([10, 14, 17, 32], 3)

        self.assertEqual(my_count, 0)