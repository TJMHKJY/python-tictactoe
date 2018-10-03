import pytest
from python_tictactoe.game_modules.board import Board

class TestBoard(object):

    @pytest.fixture
    def test_board(self):
        return Board()

    @pytest.fixture
    def test_board_filled(self):
        return Board([[1,2,3], [4,5,6], [7,8,9]])

    def test_create_board(self, test_board):
        row_size = 3
        board = test_board.create_board(row_size)
        assert len(board) == row_size
    
    def test_row_size(self, test_board):
        assert test_board.row_size == 3

    def test_board_returns_a_board(self, test_board):
        board = test_board.board()
        assert board == [[None, None, None], [None, None, None], [None, None, None]]

    def test_rows(self, test_board_filled):
        rows = test_board_filled.rows()
        assert rows == [[1,2,3], [4,5,6], [7,8,9]]

    def test_columns(self, test_board_filled):
        columns = test_board_filled.columns()
        assert columns == [[1,4,7], [2,5,8], [3,6,9]]

    def test_left_diagonal(self, test_board_filled):
        left_diagonal = test_board_filled.left_diagonal()
        assert left_diagonal == [1,5,9]

    def test_right_diagonal(self, test_board_filled):
        right_diagonal = test_board_filled.right_diagonal()
        assert right_diagonal == [3,5,7]

    def test_diagonals(self, test_board_filled):
        diagonals = test_board_filled.diagonals()
        assert diagonals == [[1,5,9], [3,5,7]]

    def test_get_row_at(self, test_board_filled):
        index = 1
        row = test_board_filled.get_row_at(index)
        assert row == [4,5,6]

    def test_get_col_at(self, test_board_filled):
        index = 1
        row = test_board_filled.get_col_at(index)
        assert row == [2,5,8]

    def test_get_square(self, test_board_filled):
        row = 0
        col = 0
        square = test_board_filled.get_square(row, col)
        assert square == 1

    def test_empty_squares(self):
        board = [[None, "x", None], ["x", "o", "x"], ["o", "x", None]]
        test_board = Board(board)
        empty_squares = test_board.empty_squares()
        
        assert empty_squares == [1,3,9]

    def test_is_full(self):
        board = [["o", "x", "o"], ["x", "x", "o"], ["o", "o", "x"]]
        test_board = Board(board)
        
        assert test_board.is_full()