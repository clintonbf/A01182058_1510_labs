from unittest import TestCase

import midterm


class TestMultiples_of_3(TestCase):
    def test_multiples_of_3_0_multiples(self):
        s = midterm.multiples_of_3(2)

        self.assertEqual(s, 0)

    def test_multiples_of_3_2_multiples(self):
        s = midterm.multiples_of_3(7)

        self.assertEqual(s, 9)
