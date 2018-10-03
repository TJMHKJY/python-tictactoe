class Game:

    def __init__(self, board, rules):
        self.board = board
        self.rules = rules

    def has_win(self, board, rules):
        return self.rules.has_winning_row(board) or\
        self.rules.has_winning_column(board) or\
        self.rules.has_winning_diagonal(board)