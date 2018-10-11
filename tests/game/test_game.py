import pytest
from python_tictactoe.game.game import Game
from python_tictactoe.game.board import Board
from python_tictactoe.game.rules import Rules

class TestGame(object):

    @pytest.fixture
    def test_board_array(self):
        return [
            ["o", "x", "x"],
            ["x", "o", "x"],
            ["o", "x", "o"]
        ]

    @pytest.fixture
    def test_game_2(self):
        board = [
            [None, None, None],
            ["x", "o", "x"],
            ["o", "x", None]
        ]
        test_board = Board(board)
        test_rules = Rules(test_board)
        return Game(test_board, test_rules)

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

    def test_if_game_is_over(self, test_game):
        assert test_game.is_over()

    def test_if_game_is_tied(self, test_game):
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
        test_board = Board(test_board_array)
        test_rules = "foo"
        test_game = Game(test_board, test_rules)
        assert test_game.get_rules() == "foo"

    def test_it_can_return_the_games_players(self, test_game):
        test_game.add_player("foo")
        test_game.add_player("bar")

        assert test_game.get_players() == ["foo", "bar"]

    def test_it_can_get_and_set_the_current_player(self, test_game):
        test_game.set_current_player("player1")

        assert test_game.get_current_player() == "player1"

    def test_that_it_can_mark_a_square(self, test_game_2):
        square = 9
        icon = "x"

        test_game_2.mark_square(square, icon)

        expected_board = [
            [None, None, None],
            ["x", "o", "x"],
            ["o", "x", "x"],
        ]

        assert test_game_2.get_board().board() == expected_board

    def test_that_it_can_unmark_a_square(self, test_game_2):
        board = [
            [None, None, None],
            ["x", "o", "x"],
            ["o", "x", "x"]
        ]
        test_board = Board(board)
        test_rules = Rules(test_board)
        test_game = Game(test_board, test_rules)
        
        square = 9

        test_game.unmark_square(square)

        expected_board = [
            [None, None, None],
            ["x", "o", "x"],
            ["o", "x", None],
        ]

        assert test_game.get_board().board() == expected_board

    def test_that_it_can_switch_the_current_player(self, test_game_2):
        test_game_2.add_player("foo")
        test_game_2.add_player("bar")
        test_game_2.set_current_player("foo")

        test_game_2.switch_current_player()

        assert test_game_2.get_current_player() == "bar"

    def test_that_it_can_check_if_a_move_is_valid(self, test_game_2):
        assert test_game_2.is_valid_move(1) == True
        assert test_game_2.is_valid_move(2) == True
        assert test_game_2.is_valid_move(3) == True
        assert test_game_2.is_valid_move(9) == True


    
        