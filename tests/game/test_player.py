import mock 
import pytest
from mock import patch
from python_tictactoe.strategy.minimax_strategy import MinimaxStrategy
from python_tictactoe.strategy.input_strategy import InputStrategy
from python_tictactoe.mocks.fake_minimax_strategy import FakeMinimaxStrategy
from python_tictactoe.mocks.fake_input_strategy import FakeInputStrategy
from python_tictactoe.game.player import Player
# from python_tictactoe.strategy.input_strategy import InputStrategy
# from python_tictactoe.strategy.minimax_strategy import MinimaxStrategy

class TestPlayer(object):

    def test_minimax_move(self):
        strategy = FakeMinimaxStrategy()
        gamestate = {
            'players': None,
            'current_player': None,
            'board': None,
            'rules': None,
            'game': None
        }
        computer_player = Player("computer", "o", strategy)
        assert computer_player.select_move(gamestate) == "minimax"

    def test_input_move(self):
        strategy = FakeInputStrategy()
        gamestate = {
            'players': None,
            'current_player': None,
            'board': None,
            'rules': None,
            'game': None
        }
        human_player = Player("player 1", "x", strategy)
        assert human_player.select_move(gamestate) == 5

    # def test_mocked_move(self):
    #     player = Player("computer", "o")
    #     assert player.select_move() == "123456"