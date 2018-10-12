import pytest
from python_tictactoe.game.board import Board
from python_tictactoe.game.rules import Rules
from python_tictactoe.game.game import Game
from python_tictactoe.game.player import Player
from python_tictactoe.ui.input import Input
from python_tictactoe.ui.output import Output
from python_tictactoe.ui.validator import Validator
from python_tictactoe.ui.cli_messages import CliMessages
from python_tictactoe.mocks.fake_input import FakeInput
from python_tictactoe.mocks.fake_minimax_strategy import FakeMinimaxStrategy
from python_tictactoe.strategy.minimax_strategy import MinimaxStrategy

class TestMinimaxStrategy:
    
    def test_that_best_move_returns_a_move(self):
        game_params = {
            'messages': CliMessages(),
            'cli_input': FakeInput("363", "7"),
            'cli_output': Output(),
            'validator': Validator() 
        }
        board_array = [
            ["x", "x", "o"],
            ["o", None, "o"],
            ["x", "o", "x"]
        ]
        board = Board(board_array)
        rules = Rules(board)
        game = Game(board, rules)

        human_player = Player("Player 1", "x", "foo")
        computer_player = Player("Computer", "o", "foo")
        game.add_player(human_player)
        game.add_player(computer_player)
        game.set_current_player(computer_player)
        test_strategy = MinimaxStrategy()

        assert test_strategy.best_move(game, game_params) == 5

    def test_that_it_picks_the_only_open_spot(self):
        board_array = [
            ["x", "x", "o"],
            ["o", None, "o"],
            ["x", "o", "x"]
        ]

        board = Board(board_array)
        rules = Rules(board)
        game = Game(board, rules)
        
        human_player = Player("Player 1", "x", "foo")
        computer_player = Player("Computer", "o", "foo")
        game.add_player(human_player)
        game.add_player(computer_player)
        game.set_current_player(human_player)
        test_strategy = MinimaxStrategy()

        result = test_strategy.minimax(game)
        assert result == 5
    
    def test_that_it_picks_a_win(self):
        board_array = [
            ["x",  "o", "x"],
            ["x",  "o", "x"],
            ["o",  None, None]
        ]

        board = Board(board_array)
        rules = Rules(board)
        game = Game(board, rules)

        human_player = Player("Player 1", "x", "foo")
        computer_player = Player("Computer", "o", MinimaxStrategy())
        game.add_player(computer_player)
        game.add_player(human_player)
        game.set_current_player(computer_player)
        test_strategy = MinimaxStrategy()

        result = test_strategy.minimax(game) 
        assert result == 8

    def test_that_it_blocks_a_win(self):
        board_array = [
            ["x",  "x",  "o"],
            [None, "x",  "o"],
            [None, None, None]
        ]

        board = Board(board_array)
        rules = Rules(board)
        game = Game(board, rules)
        
        human_player = Player("Player 1", "x", "foo")
        computer_player = Player("Computer", "o", "foo")
        game.add_player(human_player)
        game.add_player(computer_player)

        game.set_current_player(computer_player)
        test_strategy = MinimaxStrategy()

        result = test_strategy.minimax(game)
        assert result == 9

    def test_that_it_picks_a_win_when_there_are_more_empty_spaces(self):
        board_array = [
            ["x",  "o",  "x"],
            [None, "o",  None],
            [None, None, None]
        ]

        board = Board(board_array)
        rules = Rules(board)
        game = Game(board, rules)
        
        computer_player = Player("Computer", "o", "foo")
        human_player = Player("Player 1", "x", "foo")
        game.add_player(computer_player)
        game.add_player(human_player)

        game.set_current_player(computer_player)
        test_strategy = MinimaxStrategy()

        result = test_strategy.minimax(game)
        assert result == 4


    def test_that_it_can_place_a_move(self):
        board_array = [
            ["x", "x", "o"],
            ["x", None, "o"],
            ["x", "o", "x"]
        ]
        expected_board_array = [
            ["x", "x", "o"],
            ["x", "o", "o"],
            ["x", "o", "x"]
        ]
        board = Board(board_array)
        rules = Rules(board)
        game = Game(board, rules)

        human_player = Player("Player 1", "x", "foo")
        computer_player = Player("Computer", "o", "foo")
        game.add_player(human_player)
        game.add_player(computer_player)
        game.set_current_player(computer_player)

        test_strategy = MinimaxStrategy()
        test_strategy.place_move(game, 5)
        assert game.get_board().empty_squares() == []
        assert game.get_board().board() == expected_board_array
        assert game.get_current_player().icon == "x"

    def test_it_can_return_a_player_score_value(self):
        board_array = [
            ["x", "x", "o"],
            ["x", "o", "o"],
            ["x", "o", "x"]
        ]

        board = Board(board_array)
        rules = Rules(board)
        game = Game(board, rules)
        test_strategy = MinimaxStrategy()

        assert test_strategy.player_score_value(game) == -1

    def test_it_can_return_the_best_score_in_a_scores_dictionary(self):
        scores_dict = {1: 1, 2: 3, 8: 4, 5: 3, 7: 4}
        test_strategy = MinimaxStrategy()
        assert test_strategy.best_score(scores_dict) == 4

    def test_it_can_return_the_highest_score_in_a_scores_dictionary(self):
        scores_dict = {1: 1, 2: 3, 8: 4, 5: 3, 7: 5}
        test_strategy = MinimaxStrategy()
        assert test_strategy.highest_score(scores_dict) == 7

    def test_it_can_return_available_squares_in_a_flattened_board(self):
        board_array = [
            ["x", None, "o"],
            [None, "o", "o"],
            ["x", "o", None]
        ]
        board = Board(board_array)
        rules = Rules(board)
        game = Game(board, rules)
        
        flattened_board = game.get_board().flattened_board()
        test_strategy = MinimaxStrategy()

        assert test_strategy.available_squares(flattened_board) == [2,4,9]

    def test_that_it_can_evaluate_a_board_and_return_a_square(self):   
        board_array = [
            ["x", None, "o"],
            ["x", "o", "o"],
            ["x", "o", None]
        ]

        board = Board(board_array)
        rules = Rules(board)
        game = Game(board, rules)

        human_player = Player("Player 1", "x", "foo")
        computer_player = Player("Computer", "o", "foo")
        game.add_player(human_player)
        game.add_player(computer_player)
        game.set_current_player(human_player)
        test_strategy = MinimaxStrategy()

        assert test_strategy.evaluate_board(game, depth=0) == 10
