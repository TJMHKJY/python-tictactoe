import pytest
from python_tictactoe.app.game_loop import GameLoop
from python_tictactoe.ui.cli_messages import CliMessages
from python_tictactoe.ui.input import Input
from python_tictactoe.ui.output import Output
from python_tictactoe.ui.validator import Validator
from python_tictactoe.mocks.fake_input import FakeInput
from python_tictactoe.mocks.fake_player_config_input import FakePlayerConfigInput
from python_tictactoe.mocks.fake_cli_messages import FakeCliMessages
from python_tictactoe.mocks.fake_validator import FakeValidator
from python_tictactoe.game.rules import Rules
from python_tictactoe.game.board import Board
from python_tictactoe.game.game import Game
from python_tictactoe.game.player import Player
from python_tictactoe.strategy.input_strategy import InputStrategy
from python_tictactoe.strategy.minimax_strategy import MinimaxStrategy

class TestGameLoop(object):

    @pytest.fixture
    def test_game_loop(self):
        return GameLoop()

    @pytest.fixture
    def test_game_params(self):
        game_params = {
            'messages': CliMessages(),
            'cli_input': FakeInput("7", "5"),
            'cli_output': Output(),
            'validator': Validator()
        }
        return game_params

    def test_that_run_returns_a_game_object(self, test_game_params):
        board_array = [
            ["x", "x", "o"],
            ["o", "x", "o"],
            ["x", "o", "x"]
        ]
        board = Board(board_array)
        rules = Rules(board)
        game = Game(board, rules)

        human_player = Player("Player 1", "x", InputStrategy())
        computer_player = Player("Computer", "o", "foo")
        game.add_player(human_player)
        game.add_player(computer_player)
        game.set_current_player(human_player)

        test_game_loop = GameLoop()
        result = test_game_loop.run(game, test_game_params)
        assert game == result

    def test_that_the_game_loop_can_place_a_move(self, test_game_params):
        board_array = [
            ["x", "x", "o"],
            ["o", None, "o"],
            ["x", "o", "x"]
        ]
        expected_board_array = [
            ["x", "x", "o"],
            ["o", "x", "o"],
            ["x", "o", "x"]
        ]
        board = Board(board_array)
        rules = Rules(board)
        game = Game(board, rules)

        human_player = Player("Player 1", "x", InputStrategy())
        computer_player = Player("Computer", "o", "foo")
        game.add_player(human_player)
        game.add_player(computer_player)
        game.set_current_player(human_player)

        test_game_loop = GameLoop()

        test_game_loop.place_move(game, test_game_params)

        assert game.get_board().board() == expected_board_array

    def test_that_it_runs_the_loop_again_if_selected_move_is_a_filled_position(self, capsys, test_game_params):
        board_array = [
            ["x", "x", "o"],
            ["o", None, "o"],
            ["x", "o", "x"]
        ]
        board = Board(board_array)
        rules = Rules(board)
        game = Game(board, rules)

        human_player = Player("Player 1", "x", InputStrategy())
        computer_player = Player("Computer", "o", "foo")
        game.add_player(human_player)
        game.add_player(computer_player)
        game.set_current_player(human_player)

        test_game_loop = GameLoop()
        test_game_loop.place_move(game, test_game_params)
        captured = capsys.readouterr()
        expected_output = "Player 1 selects square 7. Placing Player 1's move.\nThat was an invalid move, please try again. Please select a move between 1 - 9:\nPlayer 1 selects square 5. Placing Player 1's move."
        assert captured.out.split("\n\n")[0] == expected_output

    def test_that_game_loop_can_mark_the_board(self, test_game_params):
        board_array = [
            ["x", "x", "o"],
            ["o", None, "o"],
            ["x", "o", "x"]
        ]

        expected_board_array = [
            ["x", "x", "o"],
            ["o", "x", "o"],
            ["x", "o", "x"]
        ]
        board = Board(board_array)
        rules = Rules(board)
        game = Game(board, rules)

        human_player = Player("Player 1", "x", InputStrategy())
        computer_player = Player("Computer", "o", "foo")
        game.add_player(human_player)
        game.add_player(computer_player)
        game.set_current_player(human_player)

        test_game_loop = GameLoop()
        test_game_loop.mark_board(5, game, test_game_params)

        assert game.get_board().board() == expected_board_array


