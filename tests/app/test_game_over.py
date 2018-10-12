import pytest
from python_tictactoe.app.game_config import GameConfig
from python_tictactoe.app.game_over import GameOver
from python_tictactoe.ui.cli_messages import CliMessages
from python_tictactoe.ui.input import Input
from python_tictactoe.ui.output import Output
from python_tictactoe.ui.validator import Validator
from python_tictactoe.mocks.fake_cli_messages import FakeCliMessages
from python_tictactoe.mocks.fake_validator import FakeValidator
from python_tictactoe.game.rules import Rules
from python_tictactoe.game.board import Board
from python_tictactoe.game.game import Game
from python_tictactoe.game.player import Player

class TestGameOver(object):

    def test_that_run_returns_a_game_over_message(self, capsys):
        board = [
            ["@", "x", "x"],
            ["x", "@", "x"],
            ["@", "x", "@"],
        ]
        test_board = Board(board)
        test_rules = Rules(test_board)
        test_game = Game(test_board, test_rules)
        test_game_over = GameOver()

        game_params = {
            'messages': FakeCliMessages(),
            'game_input': Input(),
            'cli_output': Output(),
            'validator': Validator()
        }

        human_player = Player("Player 1", "x", "foo")
        computer_player = Player("Computer", "@", "foo")
        test_game.add_player(human_player)
        test_game.add_player(computer_player)

        test_game.set_current_player(computer_player)

        test_game_over.run(test_game, game_params)
        captured = capsys.readouterr()
        assert captured.out.strip().split("\n")[-1] == "game has ended"

    def test_that_it_can_check_for_a_win(self):
        board = [
            ["@", "x", "x"],
            ["x", "@", "x"],
            ["@", "x", "@"],
        ]
        test_board = Board(board)
        test_rules = Rules(test_board)
        test_game = Game(test_board, test_rules)
        test_messages = CliMessages()
        test_game_config = GameConfig()
        test_game_over = GameOver()

        player_settings_dict = {
            'name': 'Player 1',
            'icon': 'x',
            'turn_order': '1',
            'computer_name': 'Computer',
            'computer_icon': '@'
        }
        
        result = test_game_config.create_players(player_settings_dict, test_game)

        assert test_game_over.check_for_win(result, test_messages) == "\nComputer wins!"

    def test_that_it_can_check_for_a_tie(self):
        board = [
            ["o", "x", "x"],
            ["x", "o", "o"],
            ["o", "x", "x"],
        ]
        test_board = Board(board)
        test_rules = Rules(test_board)
        test_game = Game(test_board, test_rules)
        test_messages = CliMessages()
        game_config = GameConfig()
        test_game_over = GameOver()

        player_settings_dict = {
            'name': 'Player 1',
            'icon': 'x',
            'turn_order': '1',
            'computer_name': 'Computer',
            'computer_icon': 'o'
        }
        game_config = game_config.create_players(player_settings_dict, test_game)
        assert test_game_over.check_for_win(test_game, test_messages) == "\nGame is tied!"