from python_tictactoe.strategy_modules.minimax_strategy import best_move

class ComputerPlayer:

    def __init__(self, name, icon):
        self.name = name
        self.icon = icon

    def select_move(self):
        return best_move()