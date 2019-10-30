from unittest import TestCase

import midterm


class TestPrepender(TestCase):
    def test_prepender_single_char(self):
        my_list = ['boo', 'foo', 'goo']
        expected_list = ['sboo', 'sfoo', 'sgoo']
        midterm.prepender(my_list, "s")

        self.assertEqual(my_list, expected_list)

    def test_prepender_no_char(self):
        my_list = ['boo', 'foo', 'goo']
        expected_list = ['boo', 'foo', 'goo']
        midterm.prepender(my_list, "")

        self.assertEqual(my_list, expected_list)
