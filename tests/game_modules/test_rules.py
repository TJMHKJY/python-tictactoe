import pytest
from python_tictactoe.game_modules.rules import Rules
from python_tictactoe.game_modules.board import Board

class TestRules(object):

    def test_all_elements_are_the_same(self):
        test_board = Board()
        test_rules = Rules(test_board)
        row = ["x", "x", "x"]        
        assert test_rules.all_elements_are_the_same(row)

    def test_no_elements_are_empty(self):
        test_board = Board()
        test_rules = Rules(test_board)
        row = ["x", "x", "x"]        
        assert test_rules.no_elements_are_empty(row)

    def test_is_winning_row(self):
        test_board = Board()
        test_rules = Rules(test_board)
        row = ["x", "x", "x"]        
        assert test_rules.is_winning_row(row)

    def test_is_not_a_winning_row_if_all_elements_are_none(self):
        test_board = Board()
        test_rules = Rules(test_board)
        row = [None, None, None]        
        assert test_rules.is_winning_row(row) == False

    def test_check_for_win(self):
        test_board = Board()
        test_rules = Rules(test_board)
        rows = [
            ["x", "x", "x"],
            ["o", "o", "x"],
            ["o", "x", "o"],
        ]
        assert test_rules.check_for_win(rows) == True

    def test_winning_icon(self):
        test_board = Board()
        test_rules = Rules(test_board)
        rows = [
            ["x", "x", "x"],
            ["o", "o", "x"],
            ["o", "x", "o"],
        ]
        assert test_rules.winning_icon(rows) == "x"

    def test_square_to_rows_and_cols(self):
        test_board = Board()
        test_rules = Rules(test_board)
        square = 9
        row_size = 3
        assert test_rules.square_to_rows_and_cols(square, row_size) == [2,2]

    def test_has_winning_row(self):
        test_board = Board()
        test_rules = Rules(test_board)
        board = [
            ["x", "x", "x"],
            ["o", "o", "x"],
            ["o", "x", "o"],
        ]
        assert test_rules.has_winning_row(board) == True
    
    def test_has_winning_column(self):
        test_board = Board()
        test_rules = Rules(test_board)
        board = [
            ["o", "x", "x"],
            ["o", "o", "x"],
            ["o", "x", "o"],
        ]
        assert test_rules.has_winning_column(board) == True

    def test_has_winning_diagonal(self):
        test_board = Board()
        test_rules = Rules(test_board)
        board = [
            ["o", "x", "x"],
            ["x", "o", "x"],
            ["o", "x", "o"],
        ]
        assert test_rules.has_winning_diagonal(board) == True