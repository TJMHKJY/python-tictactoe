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
from python_tictactoe.strategy.input_strategy import InputStrategy

class TestInputStrategy(object):

    def test_that_best_move_returns_a_move(self):
        game_params = {
            'messages': CliMessages(),
            'cli_input': FakeInput("363", "7"),
            'cli_output': Output(),
            'validator': Validator() 
        }
        board = Board()
        rules = Rules(board)
        game = Game(board, rules)
        
        human_player = Player("Player 1", "x", "foo")
        computer_player = Player("Computer", "o", "foo")
        game.add_player(human_player)
        game.add_player(computer_player)
        game.set_current_player(computer_player)

        test_input_strategy = InputStrategy()
        assert test_input_strategy.best_move(game, game_params) == "7"

    def test_that_it_can_return_a_user_move(self, monkeypatch):
        game_params = {
            'messages': CliMessages(),
            'cli_input': Input(),
            'cli_output': Output(),
            'validator': Validator() 
        }
        test_input_strategy = InputStrategy()
        monkeypatch.setattr('builtins.input', lambda x: " 5  ")
        i = test_input_strategy.get_move("player name", game_params)
        assert i == "5"

    def test_that_it_can_check_if_the_user_move_is_valid(self, monkeypatch, capsys):
        game_params = {
            'messages': CliMessages(),
            'cli_input': FakeInput("363", "7"),
            'cli_output': Output(),
            'validator': Validator() 
        }
        name = "foo"
        test_input_strategy = InputStrategy()
        result = test_input_strategy.get_move(name, game_params)
        assert result == "7"

    def test_that_it_can_check_if_the_user_move_is_invalid(self, monkeypatch, capsys):
        game_params = {
            'messages': CliMessages(),
            'cli_input': FakeInput("568", "4"),
            'cli_output': Output(),
            'validator': Validator() 
        }
        game_params['cli_input'].reset_count()
        name = "foo"
        test_input_strategy = InputStrategy()
        test_input_strategy.get_move(name, game_params)
        captured = capsys.readouterr()
        assert captured.out == "That was an invalid move, please try again. Please select a move between 1 - 9:\nfoo selects square 4. Placing foo's move.\n"

    