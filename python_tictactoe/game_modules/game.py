class Game:

    def __init__(self, board, rules):
        self.board = board
        self.rules = rules

    def is_won(self):
        return self.rules.has_winning_row() or self.rules.has_winning_column() or self.rules.has_winning_diagonal()

    def is_over(self, board):
        return self.is_won or self.board.is_full()