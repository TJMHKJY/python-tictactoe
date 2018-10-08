import pytest
from python_tictactoe.app.app_main import App
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
    def test_valid_game_config(self):
        messages = CliMessages()
        game_input = Input()
        validator = Validator()
        player_config_params = {
            'messages': messages,
            'game_input': game_input,
            'validator': validator, 
        }
        return player_config_params

    def test_that_it_can_capture_the_user_name(self, test_app, test_valid_game_config, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda x: " Player 1  ")
        player_config_params = test_valid_game_config
        i = test_app.get_name(player_config_params)
        assert i == "Player 1"

    def test_that_it_can_check_if_the_user_name_is_invalid(self, test_app, monkeypatch, capsys):
        player_config_params = {
            'messages': CliMessages(),
            'game_input': FakeInput("p", "Player 1"),
            'validator': Validator() 
        }
        player_config_params['game_input'].reset_count()
        test_app.get_name(player_config_params)
        captured = capsys.readouterr()
        assert captured.out == "\nName should not be empty, please try again\n\nYour selected player name is Player 1\n"

    def test_that_it_can_capture_the_user_icon(self, test_app, test_valid_game_config, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda x: " Player 1  ")
        player_config_params = test_valid_game_config
        i = test_app.get_icon(player_config_params)
        assert i == "Player 1"

    def test_that_it_can_check_if_the_user_icon_is_invalid(self, test_app, monkeypatch, capsys):
        player_config_params = {
            'messages': CliMessages(),
            'game_input': FakeInput("p", "Player 1"),
            'validator': Validator() 
        }
        player_config_params['game_input'].reset_count()
        test_app.get_icon(player_config_params)
        captured = capsys.readouterr()
        assert captured.out == "\nThat was an invalid selection. Icon should be one alpha character. Please try again.\n\nYour selected icon is Player 1\n"
    
    def test_that_it_can_capture_the_user_turn_order(self, test_app, test_valid_game_config, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda x: " Player 1  ")
        player_config_params = test_valid_game_config
        i = test_app.get_turn_order(player_config_params)
        assert i == "Player 1"

    def test_that_it_can_check_if_the_user_turn_is_invalid(self, test_app, monkeypatch, capsys):
        player_config_params = {
            'messages': CliMessages(),
            'game_input': FakeInput("p", "Player 1"),
            'validator': Validator() 
        }
        player_config_params['game_input'].reset_count()
        test_app.get_turn_order(player_config_params)
        captured = capsys.readouterr()
        assert captured.out == "\nThat was an invalid selection. Please enter 1 if you would like to go first or 2 if second.\n\nYour selected turn order is Player 1\n"
    
    def test_that_it_can_capture_a_user_move(self, test_app, test_valid_game_config, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda x: " Player 1  ")
        player_config_params = test_valid_game_config
        name = "foo"
        i = test_app.get_move(name, player_config_params)
        assert i == "Player 1"

    def test_that_it_can_check_if_the_user_move_is_invalid(self, test_app, monkeypatch, capsys):
        player_config_params = {
            'messages': CliMessages(),
            'game_input': FakeInput("p", "Player 1"),
            'validator': Validator() 
        }
        player_config_params['game_input'].reset_count()
        name = "foo"
        test_app.get_move(name, player_config_params)
        captured = capsys.readouterr()
        assert captured.out == "That was an invalid move, please try again. Please select a move between 1 - 9:\nfoo selects square Player 1. Placing foo's move.\n"

    def test_that_it_returns_a_user_config_hash(self, test_app):
        player_config_params = {
        'messages': FakeCliMessages(),
        'game_input': FakePlayerConfigInput(),
        'validator': FakeValidator() 
        } 
        expected_result = {
            'name': 'foo',
            'icon': 'foo',
            'turn_order': 'foo',
            'computer_name': 'foo',
            'computer_icon': 'foo'
        }

        assert test_app.player_config(player_config_params) == expected_result

    def test_that_create_game_returns_a_game(self, test_app):
        board = Board()
        rules = Rules(board)
        
        result = test_app.create_game(board, rules)

        assert result.get_board() == board
    
    def test_that_create_players_returns_an_updated_game(self, test_app):
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

        result = test_app.create_players(player_settings_dict, game)

        assert len(result.get_players()) == 2
        assert result.get_players()[0] == result.get_current_player()
        assert result.get_players()[0].name == 'Player 1'
        assert result.get_players()[1].name == 'Computer'

    def test_that_it_can_check_for_a_win(self, test_app):
        board = [
            ["@", "x", "x"],
            ["x", "@", "x"],
            ["@", "x", "@"],
        ]
        board = Board(board)
        rules = Rules(board)
        game = Game(board, rules)

        player_settings_dict = {
            'name': 'Player 1',
            'icon': 'x',
            'turn_order': '1',
            'computer_name': 'Computer',
            'computer_icon': '@'
        }
        test_messages = CliMessages()
        result = test_app.create_players(player_settings_dict, game)

        assert len(result.get_players()) == 2
        assert result.get_players()[0].name == 'Player 1'
        assert test_app.check_for_win_or_tie(result, test_messages) == "\nComputer wins!"

    def test_that_it_can_check_for_a_tie(self, test_app):
        board = [
            ["o", "x", "x"],
            ["x", "o", "o"],
            ["o", "x", "x"],
        ]
        test_board = Board(board)
        test_rules = Rules(test_board)
        test_game = Game(test_board, test_rules)
        test_messages = CliMessages()
        player_settings_dict = {
            'name': 'Player 1',
            'icon': 'x',
            'turn_order': '1',
            'computer_name': 'Computer',
            'computer_icon': '@'
        }
        result = test_app.create_players(player_settings_dict, test_game)
        assert test_app.check_for_win_or_tie(test_game, test_messages) == "\nGame is tied!"