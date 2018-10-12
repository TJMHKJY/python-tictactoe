class Rules:

    def __init__(self, board):
        self.board = board

    def all_elements_are_the_same(self, row):
        #return all(element == row[0] for element in row)
        return len(set(row)) == 1

    def no_elements_are_empty(self, row):
        return all(element != None for element in row)

    def is_winning_row(self, row):
        return self.all_elements_are_the_same(row) and self.no_elements_are_empty(row) 

    def check_for_win(self, rows):
        for row in rows:
            if self.is_winning_row(row):
                return True    

    def winning_icon(self, rows):
        rows = self.board.rows()
        columns = self.board.columns()
        diagonals = self.board.diagonals()
        rows.extend(columns)
        rows.extend(diagonals)
        for row in rows: 
            if self.is_winning_row(row):
                return row[0]

    def square_to_rows_and_cols(self, square, row_size):
        return [ 
            (square - 1) // row_size,
            (square - 1) % row_size
        ]

    def has_winning_row(self):
        rows = self.board.rows()
        return self.check_for_win(rows)

    def has_winning_column(self):
        columns = self.board.columns()
        return self.check_for_win(columns)

    def has_winning_diagonal(self):
        diagonals = self.board.diagonals()
        return self.check_for_win(diagonals)