import mock 
import pytest
from mock import patch
from pytest_mock import mocker
from python_tictactoe.player_modules.computer_player import ComputerPlayer

class TestComputerPlayer(object):

    def test_select_move(self):
        player = ComputerPlayer("computer", "o")
        assert player.select_move() == "minimax"

    def test_mocked_move(self, mocker):
        mocker.patch('python_tictactoe.player_modules.computer_player.best_move', return_value='123456')
        player = ComputerPlayer("computer", "o")
        assert player.select_move() == "123456"