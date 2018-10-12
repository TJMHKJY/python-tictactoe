import sys
import pytest
from python_tictactoe.ui.cli_messages import CliMessages
from python_tictactoe.game.board import Board

class TestCliMessages(object):

    @pytest.fixture
    def test_cli(self):
        return CliMessages()

    def test_it_has_a_welcome_message(self, test_cli):
        message = "\nWelcome to Tictactoe, human vs computer version\n"
        assert test_cli.welcome_message() == message

    def test_that_it_can_ask_for_the_player_name(self, test_cli):
        message = "Please enter the name you'd like to play as:\n"
        assert test_cli.ask_for_name() == message

    def test_that_it_can_ask_for_icon(self, test_cli):
        message = "\nPlease enter any alpha character as your icon:\n"
        assert test_cli.ask_for_icon() == message

    def test_that_it_can_ask_for_a_turn_order(self, test_cli):
        message = "\nEnter 1 if you would like to go first or 2 if second:\n"
        assert test_cli.ask_for_turn_order() == message

    def test_that_it_can_confirm_a_name(self, test_cli):
        message = "Your selected player name is foo"
        assert test_cli.confirm_name("foo") == message

    def test_that_it_can_confirm_an_icon(self, test_cli):
        message = "Your selected icon is x"
        assert test_cli.confirm_icon("x") == message

    def test_that_it_can_confirm_a_turn_order(self, test_cli):
        message = "Your selected turn order is 1"
        assert test_cli.confirm_turn_order("1") == message

    def test_that_it_can_return_an_invalid_name_message(self, test_cli):
        message = "\nName should not be empty, please try again\n"
        assert test_cli.invalid_user_name() == message

    def test_that_it_can_return_an_invalid_icon_message(self, test_cli):
        message = "\nThat was an invalid selection. Icon should be one alpha character. Please try again.\n"
        assert test_cli.invalid_user_icon() == message

    def test_that_it_can_return_an_invalid_turn_order_message(self, test_cli):
        message = "\nThat was an invalid selection. Please enter 1 if you would like to go first or 2 if second.\n"
        assert test_cli.invalid_turn_order() == message

    def test_that_it_can_return_a_computer_name(self, test_cli):
        message = "Computer"
        assert test_cli.computer_name() == message

    def test_that_it_can_return_a_computer_icon(self, test_cli):
        message = "@"
        assert test_cli.computer_icon() == message

    def test_that_it_can_confirm_the_computers_name(self, test_cli):
        message = "Computer's name will be foo"
        assert test_cli.confirm_computer_name("foo") == message

    def test_that_it_can_confirm_the_computers_icon(self, test_cli):
        message = "Computer's icon will be @"
        assert test_cli.confirm_computer_icon("@") == message
    
    def test_that_it_can_format_the_turn_order_for_the_computer(self, test_cli):
        message = "second"
        assert test_cli.format_computer_turn_order("1") == message

    def test_that_it_can_confirm_the_computers_turn_order(self, test_cli):
        message = "Computer will go second"
        assert test_cli.confirm_computer_turn_order("1") == message

    def test_that_it_can_announce_a_turn(self, test_cli):
        name = "Player 1"
        message = "Player 1, your turn. Please select a move between 1 - 9:\n"
        assert test_cli.announce_turn(name) == message

    def test_that_it_can_return_an_invalid_move_message(self, test_cli):
        message = "That was an invalid move, please try again. Please select a move between 1 - 9:"
        assert test_cli.invalid_move() == message

    def test_that_it_can_confirm_a_move(self, test_cli):
        name = "Player 1"
        move = "7"
        message = "Player 1 selects square 7. Placing Player 1's move."
        assert test_cli.confirm_move(name, move) == message  

    def test_that_it_can_confirm_the_computers_move(self, test_cli):
        name = "Computer"
        message = "\nComputer's move. Computer is generating a move.\n"
        assert test_cli.computer_move(name) == message

    def test_that_it_can_announce_if_a_game_is_won(self, test_cli):
        message = "\nPlayer 1 wins!"
        assert test_cli.game_won("Player 1") == message  

    def test_that_it_can_announce_if_a_game_is_tied(self, test_cli):
        message = "\nGame is tied!"
        assert test_cli.game_tied() == message

    def test_that_it_can_announce_that_the_game_has_ended(self, test_cli):
        message = "\nThank you for playing!\n"
        assert test_cli.game_end() == message

    def test_that_given_a_board_array_it_can_print_a_board(self, test_cli):
        board_array = [
            ["x", None, "o"],
            ["o", None, "x"],
            ["x", "o", None]
        ]
        board = Board(board_array)
        formatted_board = "\n| x | 2 | o |\n-------------\n| o | 5 | x |\n-------------\n| x | o | 9 |\n"
        assert test_cli.format_board_for_cli(board) == formatted_board