import pytest
from python_tictactoe.game_modules.game import Game
from python_tictactoe.game_modules.board import Board
from python_tictactoe.game_modules.rules import Rules

class TestGame(object):

    def test_if_game_has_a_win(self):
        test_board = Board()
        test_rules = Rules(test_board)
        test_game = Game(test_board, test_rules)
        board = [
            ["o", "x", "x"],
            ["x", "o", "x"],
            ["o", "x", "o"],
        ]        
        assert test_game.has_win(board, test_rules)
