import pytest
from python_tictactoe.app.app_main import App
from python_tictactoe.app.game_config import GameConfig
from python_tictactoe.ui.cli_messages import CliMessages
from python_tictactoe.ui.input import Input
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


class TestApp(object):

    @pytest.fixture
    def test_app(self):
        return App()

    @pytest.fixture
    def test_game_params(self):
        return {
            'messages': CliMessages(),
            'game_input': Input(),
            'validator': Validator(), 
        }

    @pytest.fixture
    def test_game(self):
        test_board = Board()
        test_rules = Rules(test_board)
        test_game = Game(test_board, test_rules)