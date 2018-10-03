class Rules:

    def __init__(self, board):
        self.board = board

    def all_elements_are_the_same(self, row):
        return all(element == row[0] for element in row)

    def no_elements_are_empty(self, row):
        return all(element != None for element in row)

    def is_winning_row(self, row):
        return self.all_elements_are_the_same(row) and self.no_elements_are_empty(row) 

    def check_for_win(self, rows):
        return any(self.is_winning_row(row) for row in rows)

    def winning_icon(self, rows):  
        for row in rows: 
            if self.is_winning_row(row):
                return row[0]

    def square_to_rows_and_cols(self, square, row_size):
        return [ 
            (square - 1) // row_size,
            (square - 1) % row_size
        ]

    def has_winning_row(self, board):
        rows = self.board.rows(board)
        return self.check_for_win(rows)

    def has_winning_column(self, board):
        columns = self.board.columns(board)
        return self.check_for_win(columns)

    def has_winning_diagonal(self, board):
        diagonals = self.board.diagonals(board)
        return self.check_for_win(diagonals)



    