from unittest import TestCase
import sparsevector


class TestSparse_add(TestCase):
    def test_sparse_all_zeros(self):
        self.fail()

    def test_sparse_same_indices(self):
        test_dict = sparsevector({0: 1, 1: 2, 2: 3}, {0: 1, 1: 2, 2: 3})
        self.fail()

    def test_sparse_v1_empty(self):
        self.fail()

    def test_sparse_v2_empty(self):
        self.fail()

    def test_sparse_non_matching_indices(self):
        self.fail()

    def test_sparse_some_matching_indices(self):
        self.fail()

    def test_sparse_one_index_adds_to_zero(self):
        self.fail()