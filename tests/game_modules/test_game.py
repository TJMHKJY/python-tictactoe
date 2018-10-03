import pytest
from python_tictactoe.game_modules.game import Game
from python_tictactoe.game_modules.board import Board
from python_tictactoe.game_modules.rules import Rules

class TestGame(object):

    @pytest.fixture
    def test_game(self):
        board = [
            ["o", "x", "x"],
            ["x", "o", "x"],
            ["o", "x", "o"],
        ]
        test_board = Board(board)
        test_rules = Rules(test_board)
        return Game(test_board, test_rules)

    def test_if_game_has_a_win(self, test_game):   
        assert test_game.is_won()

    def test_if_game_is_over(self):
        board = [
            ["o", "x", "x"],
            ["x", "o", "o"],
            ["o", "x", "x"],
        ] 
        test_board = Board(board)
        test_rules = Rules(test_board)
        test_game = Game(test_board, test_rules) 
        assert test_game.is_over(board)
