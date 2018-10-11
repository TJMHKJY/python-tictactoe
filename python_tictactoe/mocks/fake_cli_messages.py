class FakeCliMessages:

    def welcome_message(self):
        ""

    def ask_for_name(self):
        ""

    def invalid_user_name(self):
        ""

    def invalid_user_icon(self):
        ""

    def confirm_name(self, name):
        ""

    def ask_for_icon(self):
        ""

    def confirm_icon(self, icon):
        ""

    def ask_for_turn_order(self):
        ""

    def confirm_turn_order(self, turn_order):
        ""

    def computer_name(self):
        return "foo"

    def computer_icon(self):
        return "foo"

    def confirm_computer_name(self, name):
        ""
    
    def confirm_computer_icon(self, icon):
        ""
    
    def confirm_computer_turn_order(self, turn_order):
        ""

    def turn_order(self):
        ""

    def format_board_for_cli(self, board):
        ""

    def game_won(self, name):
        ""
    
    def game_tied(self):
        ""

    def game_end(self):
        return "game has ended"