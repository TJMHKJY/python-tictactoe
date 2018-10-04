import pytest
from python_tictactoe.game.game import Game
from python_tictactoe.game.board import Board
from python_tictactoe.game.rules import Rules

class TestGame(object):

    @pytest.fixture
    def test_board_array(self):
        board = [
            ["o", "x", "x"],
            ["x", "o", "x"],
            ["o", "x", "o"],
        ]
        return board

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
        assert test_game.is_over()

    def test_if_game_is_tied(self):
        board = [
            ["o", "x", "x"],
            ["x", "o", "o"],
            ["o", "x", "x"],
        ] 
        test_board = Board(board)
        test_rules = Rules(test_board)
        test_game = Game(test_board, test_rules) 
        assert test_game.is_tied() == False

    def test_it_can_return_the_board(self, test_game):
        board = [
            ["o", "x", "x"],
            ["x", "o", "x"],
            ["o", "x", "o"],
        ]
        expected_board = Board(board)
        assert test_game.get_board().board() == expected_board.board()

    def test_it_can_return_the_rules(self, test_game, test_board_array):
        board = [
            ["o", "x", "x"],
            ["x", "o", "x"],
            ["o", "x", "o"],
        ]
        test_board = Board(board)
        test_rules = "foo"
        test_game = Game(test_board, test_rules)
        assert test_game.get_rules() == "foo"

    def test_it_can_return_the_games_players(self):
        board = [
            ["o", "x", "x"],
            ["x", "o", "x"],
            ["o", "x", "o"],
        ]
        test_board = Board(board)
        test_rules = "rules"
        test_game = Game(test_board, test_rules)
        test_game.add_player("foo")
        test_game.add_player("bar")

        assert test_game.get_players() == ["foo", "bar"]

        