import pytest
from python_tictactoe.game.rules import Rules
from python_tictactoe.game.board import Board

class TestRules(object):

    @pytest.fixture
    def test_board(self):
        return Board()

    @pytest.fixture
    def test_rules(self):
        board = Board()
        return Rules(board)

    @pytest.fixture
    def test_rules_filled(self):
        board_array = [
            ["x", "x", "x"],
            ["o", "o", "x"],
            ["o", "x", "o"],
        ]
        board = Board(board_array)
        return Rules(board)

    def test_all_elements_are_the_same(self, test_rules):
        row = ["x", "x", "x"]        
        assert test_rules.all_elements_are_the_same(row)

    def test_no_elements_are_empty(self, test_rules):
        row = ["x", "x", "x"]        
        assert test_rules.no_elements_are_empty(row)

    def test_is_winning_row(self, test_rules):
        row = ["x", "x", "x"]        
        assert test_rules.is_winning_row(row)

    def test_is_not_a_winning_row_if_all_elements_are_none(self, test_rules):
        row = [None, None, None]        
        assert test_rules.is_winning_row(row) == False

    def test_check_for_win(self, test_rules_filled):
        rows = test_rules_filled.board.rows()
        assert test_rules_filled.check_for_win(rows) == True

    def test_winning_icon(self, test_rules_filled):
        rows = test_rules_filled.board.rows()
        assert test_rules_filled.winning_icon(rows) == "x"

    def test_square_to_rows_and_cols(self, test_rules):
        square = 9
        row_size = 3
        assert test_rules.square_to_rows_and_cols(square, row_size) == [2,2]

    def test_has_winning_row(self, test_rules_filled):
        assert test_rules_filled.has_winning_row() == True
    
    def test_has_winning_column(self):
        board_array = [
            ["o", "x", "x"],
            ["o", "o", "x"],
            ["o", "x", "o"],
        ]
        board = Board(board_array)
        test_rules = Rules(board)
        assert test_rules.has_winning_column() == True

    def test_has_winning_diagonal(self):
        board_array = [
            ["o", "x", "x"],
            ["x", "o", "x"],
            ["o", "x", "o"],
        ]
        board = Board(board_array)
        test_rules = Rules(board)
        assert test_rules.has_winning_diagonal() == True