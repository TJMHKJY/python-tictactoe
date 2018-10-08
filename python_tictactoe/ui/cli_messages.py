class CliMessages:
    
    def welcome_message(self):
        return "\nWelcome to Tictactoe, human vs computer version\n"

    def ask_for_name(self):
        return "Please enter the name you'd like to play as:\n"

    def ask_for_icon(self):
        return "\nPlease enter any alpha character as your icon:\n"

    def ask_for_turn_order(self):
        return "\nEnter 1 if you would like to go first or 2 if second:\n"

    def confirm_name(self, name):
        return "Your selected player name is " + name

    def confirm_icon(self, icon):
        return "Your selected icon is " + icon

    def confirm_turn_order(self, turn_order):
        return "Your selected turn order is " + turn_order

    def invalid_user_name(self):
        return "\nName should not be empty, please try again\n"

    def invalid_user_icon(self):
        return "\nThat was an invalid selection. Icon should be one alpha character. Please try again.\n"

    def invalid_turn_order(self):
        return "\nThat was an invalid selection. Please enter 1 if you would like to go first or 2 if second.\n"

    def computer_name(self):
        return "Computer"

    def computer_icon(self):
        return "@"

    def confirm_computer_name(self, name):
        return "Computer's name will be " + name

    def confirm_computer_icon(self, icon):
        return "Computer's icon will be " + icon

    def format_computer_turn_order(self, turn_order):
        return "second" if (turn_order == "1") else "first"

    def confirm_computer_turn_order(self, turn_order):
        turn_order_text = self.format_computer_turn_order(turn_order)
        return "Computer will go " + turn_order_text

    def announce_turn(self, name):
        return name + ", your turn. Please select a move between 1 - 9:"

    def invalid_move(self):
        return "That was an invalid move, please try again. Please select a move between 1 - 9:"
    
    def confirm_move(self, name, move):
        return name + " selects square " + move + ". Placing " + name + "'s move."

    def game_won(self, name):
        return "\n" + name + " wins!"

    def game_tied(self):
        return "\nGame is tied!"

    def game_end(self):
        return "\nThank you for playing!\n"

    def format_board_for_cli(self, board):
        board_array = board.rows()
        board_string = ""
        row_size = len(board_array)
        flattened_list = [item for sublist in board_array for item in sublist]
        index_replaced_list = [(idx if val == None else val) for idx, val in enumerate(flattened_list, start=1)]
        result = list(map(lambda x: "| " + str(x) + " ", index_replaced_list))
        for idx, val in enumerate(result, start=1):
            if idx % row_size == 0 and idx / row_size != row_size:
                board_string += val + "|\n-------------\n" 
            else:
                board_string += val
        return "\n" + board_string + "|\n"

