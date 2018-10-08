import pytest
from python_tictactoe.ui.validator import Validator

class TestValidator(object):

    def test_that_it_can_validate_the_user_name(self):
        test_validator = Validator()
        name = "foo"
        assert test_validator.is_valid_name(name) == True

    def test_that_it_can_validate_the_user_icon(self):
        test_validator = Validator()
        icon = "foo"
        assert test_validator.is_valid_icon(icon) == True

    def test_that_it_can_validate_the_user_turn_order(self):
        test_validator = Validator()
        turn_order = "foo"
        assert test_validator.is_valid_turn_order(turn_order) == True

    def test_that_it_can_validate_the_a_move(self):
        test_validator = Validator()
        move = "foo"
        assert test_validator.is_valid_move(move) == True