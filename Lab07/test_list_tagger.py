from unittest import TestCase

from midterm import list_tagger


class TestList_tagger(TestCase):
    def test_list_tagger_0_length_list_supplied(self):
        lst = list_tagger([])

        self.assertEqual(len(lst), 1)

    def test_list_tagger_0_length_list_supplied_has_0th_element_0(self):
        lst = list_tagger([])

        self.assertEqual(lst[0], 0)

    def test_list_tagger_1_item_list_supplied(self):
        lst = list_tagger(['a'])

        self.assertEqual(len(lst), 2)

    def test_list_tagger_1_item_list_supplied_has_element_0_eq_1(self):
        lst = list_tagger(['a'])

        self.assertEqual(lst[0], 1)

    def test_list_tagger_2_item_list_supplied(self):
        lst = list_tagger(['a', 'b'])

        self.assertEqual(len(lst), 3)

    def test_list_tagger_2_item_list_supplied_has_element_0_eq_2(self):
        lst = list_tagger(['a', 'b'])

        self.assertEqual(lst[0], 2)
