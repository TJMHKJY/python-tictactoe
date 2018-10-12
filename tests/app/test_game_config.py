import pytest
from python_tictactoe.app.app_main import App
from python_tictactoe.app.game_config import GameConfig
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
from python_tictactoe.app.app_main import App
from python_tictactoe.strategy.input_strategy import InputStrategy
from python_tictactoe.strategy.minimax_strategy import MinimaxStrategy

class TestGameConfig(object):

    @pytest.fixture
    def test_game_config(self):
        return GameConfig()

    @pytest.fixture
    def test_valid_game_config(self):
        game_params = {
            'messages': CliMessages(),
            'cli_input': Input(),
            'cli_output': Output(),
            'validator': Validator() 
        }
        return game_params

    def test_that_run_returns_a_game_object_with_an_empty_board(self, test_game_config):
        game_params = {
            'messages': FakeCliMessages(),
            'cli_input': FakePlayerConfigInput(),
            'cli_output': Output(),
            'validator': FakeValidator() 
        }

        board = Board()
        rules = Rules(board)
        game = Game(board, rules)

        result = test_game_config.run(game, game_params)
        assert result.get_board().board() == [[None, None, None], [None, None, None], [None, None, None]]


    def test_that_intro_prints_a_welcome_message(self, capsys, test_valid_game_config, test_game_config):
        board = Board()
        rules = Rules(board)
        game = Game(board, rules)
        test_game_config.intro(game, test_valid_game_config)
        captured = capsys.readouterr()
        assert captured.out.split("\n\n")[0].strip() == "Welcome to Tictactoe, human vs computer version"


    def test_that_it_can_capture_the_user_name(self, test_game_config, test_valid_game_config, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda x: " Player 1  ")
        game_params = test_valid_game_config
        i = test_game_config.get_name(game_params)
        assert i == "Player 1"


    def test_that_it_can_check_if_the_user_name_is_invalid(self, test_game_config, monkeypatch, capsys):
        game_params = {
            'messages': CliMessages(),
            'cli_input': FakeInput("p", "Player 1"),
            'cli_output': Output(),
            'validator': Validator() 
        }
        game_params['cli_input'].reset_count()
        test_game_config.get_name(game_params)
        captured = capsys.readouterr()
        assert captured.out == "\nName should not be empty, please try again\n\nYour selected player name is Player 1\n"


    def test_that_it_can_capture_the_user_icon(self, test_game_config, test_valid_game_config, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda x: " x  ")
        game_params = test_valid_game_config
        i = test_game_config.get_icon(game_params)
        assert i == "x"


    def test_that_it_can_check_if_the_user_icon_is_invalid(self, test_game_config, monkeypatch, capsys):
        game_params = {
            'messages': CliMessages(),
            'cli_input': FakeInput("test", "x"),
            'cli_output': Output(),
            'validator': Validator() 
        }
        game_params['cli_input'].reset_count()
        test_game_config.get_icon(game_params)
        captured = capsys.readouterr()
        assert captured.out == "\nThat was an invalid selection. Icon should be one alpha character. Please try again.\n\nYour selected icon is x\n"


    def test_that_it_can_capture_the_user_turn_order(self, test_game_config, test_valid_game_config, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda x: "  1  ")
        game_params = test_valid_game_config
        i = test_game_config.get_turn_order(game_params)
        assert i == "1"


    def test_that_it_can_check_if_the_user_turn_is_invalid(self, test_game_config, monkeypatch, capsys):
        game_params = {
            'messages': CliMessages(),
            'cli_input': FakeInput("345", "2"),
            'cli_output': Output(),
            'validator': Validator() 
        }
        game_params['cli_input'].reset_count()
        test_game_config.get_turn_order(game_params)
        captured = capsys.readouterr()
        assert captured.out == "\nThat was an invalid selection. Please enter 1 if you would like to go first or 2 if second.\n\nYour selected turn order is 2\n"


    def test_that_it_returns_a_user_config_hash(self, test_game_config):
        game_params = {
        'messages': FakeCliMessages(),
        'cli_input': FakePlayerConfigInput(),
        'cli_output': Output(),
        'validator': FakeValidator() 
        } 
        expected_result = {
            'name': 'foo',
            'icon': 'foo',
            'turn_order': 'foo',
            'computer_name': 'foo',
            'computer_icon': 'foo'
        }

        assert test_game_config.player_config(game_params) == expected_result

    def test_that_create_game_returns_a_game(self, test_game_config):
        board = Board()
        rules = Rules(board)
        
        result = test_game_config.create_game(board, rules)

        assert result.get_board() == board
    
    def test_that_create_players_creates_the_players_and_returns_an_updated_game(self, test_game_config):
        board = Board()
        rules = Rules(board)
        game = Game(board, rules)

        player_settings_dict = {
            'name': 'Player 1',
            'icon': 'x',
            'turn_order': '1',
            'computer_name': 'Computer',
            'computer_icon': '@'
        }

        result = test_game_config.create_players(player_settings_dict, game)

        assert len(result.get_players()) == 2
        assert result.get_players()[0] == result.get_current_player()
        assert result.get_players()[0].name == 'Player 1'
        assert result.get_players()[1].name == 'Computer'