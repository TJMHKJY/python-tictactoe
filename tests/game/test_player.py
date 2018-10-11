import pytest
from python_tictactoe.game.board import Board
from python_tictactoe.game.rules import Rules
from python_tictactoe.game.game import Game
from python_tictactoe.ui.input import Input
from python_tictactoe.ui.output import Output
from python_tictactoe.ui.validator import Validator
from python_tictactoe.ui.cli_messages import CliMessages
from python_tictactoe.strategy.minimax_strategy import MinimaxStrategy
from python_tictactoe.strategy.input_strategy import InputStrategy
from python_tictactoe.mocks.fake_minimax_strategy import FakeMinimaxStrategy
from python_tictactoe.mocks.fake_input_strategy import FakeInputStrategy
from python_tictactoe.game.player import Player

class TestPlayer(object):

    def test_minimax_move(self):
        game_params = {
            'messages': CliMessages(),
            'cli_input': Input(),
            'cli_output': Output(),
            'validator': Validator()
        }
        board = Board()
        rules = Rules(board)
        game = Game(board, rules)

        strategy = FakeMinimaxStrategy()
        computer_player = Player("computer", "o", strategy)

        assert computer_player.select_move(game, game_params) == "5"

    def test_input_move(self):
        game_params = {
            'messages': CliMessages(),
            'cli_input': Input(),
            'cli_output': Output(),
            'validator': Validator()
        }
        board = Board()
        rules = Rules(board)
        game = Game(board, rules)

        strategy = FakeInputStrategy()
        human_player = Player("player 1", "x", strategy)
        assert human_player.select_move(game, game_params) == 5