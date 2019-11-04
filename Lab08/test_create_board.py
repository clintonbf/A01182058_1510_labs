from unittest import TestCase

from Lab08.maze import create_board


class TestCreate_board(TestCase):
    def test_create_board_is_5_rows(self):
        board = create_board()

        self.assertEqual(len(board), 5)

    def test_create_board_cols_are_5_long(self):
        board = create_board()

        for sub_row in board:
            self.assertEqual(len(sub_row), 5)
