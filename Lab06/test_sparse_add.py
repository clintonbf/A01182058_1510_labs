from unittest import TestCase
import sparsevector


class TestSparse_add(TestCase):
    def test_sparse_all_zeros(self):
        test_dict = sparsevector.sparse_add({}, {})

        self.assertDictEqual(test_dict, {})

    def test_sparse_same_indices(self):
        test_dict = sparsevector.sparse_add({0: 1, 1: 2, 2: 3}, {0: 1, 1: 2, 2: 3})
        self.assertDictEqual(test_dict, {0: 2, 1: 4, 2: 6})

    def test_sparse_v1_empty(self):
        test_dict = sparsevector.sparse_add({}, {0: 1, 1: 2, 2: 3})

        self.assertDictEqual(test_dict, {0: 1, 1: 2, 2: 3})

    def test_sparse_v2_empty(self):
        test_dict = sparsevector.sparse_add({0: 1, 1: 2, 2: 3}, {})

        self.assertDictEqual(test_dict, {0: 1, 1: 2, 2: 3})

    def test_sparse_non_matching_indices(self):
        test_dict = sparsevector.sparse_add({0: 1, 3: 4, 6: 5}, {2: 1, 4: 7, 10: 4})

        self.assertDictEqual(test_dict, {0: 1, 3: 4, 6: 5, 2: 1, 4: 7, 10: 4})

    def test_sparse_some_matching_indices(self):
        test_dict = sparsevector.sparse_add({0: 4, 1: 5, 2: 7}, {0: 3, 1: 4, 3: 9})

        self.assertDictEqual(test_dict, {0: 7, 1: 9, 2: 7, 3: 9})

    def test_sparse_one_index_adds_to_zero(self):
        test_dict = sparsevector.sparse_add({0: -5, 4: -3}, {0: 5, 4: 3})
        self.assertDictEqual(test_dict, {})
