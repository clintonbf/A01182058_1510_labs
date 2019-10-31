from unittest import TestCase

from midterm import cutoff


class TestCutoff(TestCase):

    def test_cutoff_empty_list_and_0(self):  # condition i
        my_count = cutoff([], 0)

        self.assertEqual(my_count, 0)

    def test_cutoff_empty_list_and_5(self):  # condition ii
        my_count = cutoff([], 5)

        self.assertEqual(my_count, 0)

    # TROUBLE HERE
    def test_cutoff_0_in_list_and_0(self):  # condition iii
        my_count = cutoff([0], 0)

        self.assertEqual(my_count, 1)

    # POSSIBLE LOGIC ERROR: is 0 a multiple of 5?
    def test_cutoff_0_in_list_and_5(self):
        my_count = cutoff([0], 5)

        self.assertEqual(my_count, 1)

    def test_cutoff_one_element_2_and_cutoff_2(self):
        my_count = cutoff([2], 2)

        self.assertEqual(my_count, 1)

    # number of integers in the list that are a multiple of divisor
    # "is 2 a multiple of 4?" NO But 4 is a multiple of 2!!!
    def test_cutoff_one_element_2_and_cutoff_4(self):  # condition vi
        my_count = cutoff([2], 4)

        self.assertEqual(my_count, 0)

    # TROUBLE HERE!!!
    def test_cutoff_five_element_and_cutoff_0(self):  # condition vii
        # my_count = cutoff([1, 2, 3, 4, 5], 0)

        self.assertRaises(cutoff([1, 2, 3, 4, 5], 0), ZeroDivisionError)

    def test_cutoff_some_elements_are_multiples(self):
        my_count = cutoff([1, 2, 3, 4, 5], 2)

        self.assertEqual(my_count, 2)

    def test_cutoff_identical_elements_are_multiples(self):  # condition x
        my_count = cutoff([2, 2, 2, 2, 2], 2)

        self.assertEqual(my_count, 5)

    def test_cutoff_no_elements_are_multiples(self):
        my_count = cutoff([2, 2, 2, 2, 2], 10)

        self.assertEqual(my_count, 0)

    def test_cutoff_all_elements_are_multiples(self):  # condition xi
        my_count = cutoff([3, 6, 9, 12, 15], 3)

        self.assertEqual(my_count, 5)
