from unittest import TestCase

import midterm


class TestPrepender(TestCase):
    def test_prepender_empty_list_no_char(self):
        lst = []

        midterm.prepender(lst, "")

        self.assertEqual(lst, [])

    def test_prepender_empty_list_string(self):  # ii               TROUBLE HERE: ERROR here, function may need re-code
        lst = []

        midterm.prepender(lst, "Python")

        self.assertEqual(lst[0], "Python")

    def test_prepender_list_length_one_empty_string(self):
        lst = ["Python"]

        midterm.prepender(lst, "")

        self.assertEqual(lst[0], "Python")

    def test_prepender_list_length_one_nonempty_string(self):  # iv
        lst = ["Python"]

        midterm.prepender(lst, "I love ")

        self.assertEqual(lst[0], "I love Python")

    def test_prepender_list_several_items_empty_string(self):
        lst = ["Python", "is", "better", "than", "JavaScript"]
        check_lst = ["Python", "is", "better", "than", "JavaScript"]

        midterm.prepender(lst, "")

        for i in range(len(lst)):
            self.assertEqual(lst[i], check_lst[i])

    def test_prepender_list_several_items_nonempty_string(self):
        lst = ["Python", "is", "better", "than", "JavaScript"]
        check_lst = ["Umm...Python", "Umm...is", "Umm...better", "Umm...than", "Umm...JavaScript"]

        midterm.prepender(lst, "Umm...")

        for i in range(len(lst)):
            self.assertEqual(lst[i], check_lst[i])
    # def test_prepender_single_char(self):
    #     my_list = ['boo', 'foo', 'goo']
    #     expected_list = ['sboo', 'sfoo', 'sgoo']
    #     midterm.prepender(my_list, "s")
    #
    #     self.assertEqual(my_list, expected_list)
    #
    # def test_prepender_no_char(self):
    #     my_list = ['boo', 'foo', 'goo']
    #     expected_list = ['boo', 'foo', 'goo']
    #     midterm.prepender(my_list, "")
    #
    #     self.assertEqual(my_list, expected_list)
