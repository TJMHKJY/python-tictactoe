import pytest
from python_tictactoe.game_modules.board import Board

class TestBoard(object):

    def test_create_board(self):
        row_size = 3
        test_board = Board()
        board = test_board.create_board(row_size)
        assert len(board) == row_size
    
    def test_row_size(self):
        test_board = Board()
        assert test_board.row_size == 3

    def test_rows(self):
        test_board = Board()
        board = [[1,2,3],[4,5,6],[7,8,9]]
        rows = test_board.rows(board)
        assert rows == [[1,2,3], [4,5,6], [7,8,9]]

    def test_columns(self):
        test_board = Board()
        board = [[1,2,3],[4,5,6],[7,8,9]]
        columns = test_board.columns(board)
        assert columns == [[1,4,7], [2,5,8], [3,6,9]]

    def test_left_diagonal(self):
        test_board = Board()
        board = [[1,2,3],[4,5,6],[7,8,9]]
        left_diagonal = test_board.left_diagonal(board)
        assert left_diagonal == [1,5,9]

    def test_right_diagonal(self):
        test_board = Board()
        board = [[1,2,3],[4,5,6],[7,8,9]]
        right_diagonal = test_board.right_diagonal(board)
        assert right_diagonal == [3,5,7]

    def test_diagonals(self):
        test_board = Board()
        board = [[1,2,3],[4,5,6],[7,8,9]]
        diagonals = test_board.diagonals(board)
        assert diagonals == [[1,5,9], [3,5,7]]

    def test_get_row_at(self):
        test_board = Board()
        index = 1
        board = [[1,2,3],[4,5,6],[7,8,9]]
        row = test_board.get_row_at(board, index)
        assert row == [4,5,6]

    def test_get_col_at(self):
        test_board = Board()
        index = 1
        board = [[1,2,3],[4,5,6],[7,8,9]]
        row = test_board.get_col_at(board, index)
        assert row == [2,5,8]

    def test_get_square(self):
        test_board = Board()
        row = 0
        col = 0
        board = [[1,2,3],[4,5,6],[7,8,9]]
        square = test_board.get_square(board, row, col)
        assert square == 1

    def test_empty_squares(self):
        test_board = Board()
        board = [[None, "x", None], ["x", "o", "x"], ["o", "x", None]]
        empty_squares = test_board.empty_squares(board)
        assert empty_squares == [1,3,9]

    def test_is_full(self):
        test_board = Board()
        board = [["o", "x", "o"], ["x", "x", "o"], ["o", "o", "x"]]
        assert test_board.is_full(board)