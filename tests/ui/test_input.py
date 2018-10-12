import pytest
from python_tictactoe.ui.input import Input

class TestInput(object):

    def test_it_can_get_user_input(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda x: "foo")
        message = "Please enter some text for dummy input"
        test_input = Input()
        assert test_input.get_input(message) == "foo"