import mock 
import pytest
from mock import patch
from pytest_mock import mocker
from python_tictactoe.players.human_player import HumanPlayer

class TestHumanPlayer(object):

    def test_select_move(self):
        player = HumanPlayer("human", "x")
        assert player.select_move() == 5

    def test_mocked_move(self, mocker):
        mocker.patch('python_tictactoe.players.human_player.user_input', return_value='foo')
        player = HumanPlayer("player 1", "x")
        assert player.select_move() == "foo"

    