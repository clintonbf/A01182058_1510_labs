from unittest import TestCase

from midterm import list_tagger


class TestList_tagger(TestCase):
    def test_list_tagger_0_length_list_supplied(self):
        lst = []
        lst = list_tagger([])

        self.assertEqual(len(lst), 0)

    def test_list_tagger_2_item_list_supplied(self):
        lst = list_tagger(['a', 'b'])

        self.assertEqual(len(lst), 3)
