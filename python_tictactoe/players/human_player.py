from python_tictactoe.strategy.input_strategy import user_input

class HumanPlayer:

    def __init__(self, name, icon):
        self.name = name
        self.icon = icon

    def select_move(self):
        return user_input()