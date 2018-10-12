class Board:

    def __init__(self, board_array=None, row_size=3):
        self.row_size = row_size
        self.__cells = board_array if board_array is not None else self.create_board(row_size)

    def create_board(self, row_size):
        return [[None for _ in range(row_size)] for _ in range(row_size)]

    def board(self):
        return self.__cells

    def rows(self): 
        return self.board()

    def columns(self):
        zipped = zip(*self.board())
        columns = [list(x) for x in zipped]
        return columns

    def left_diagonal(self):
        left_diagonal = [val[idx] for idx, val in enumerate(self.board())]
        return left_diagonal

    def right_diagonal(self):
        right_diagonal = [val[len(self.board()) - (idx + 1)] for idx, val in enumerate(self.board())]
        return right_diagonal

    def diagonals(self):
        return [self.left_diagonal(), self.right_diagonal()]

    def get_row_size(self):
        return len(self.rows())
   
    def get_row_at(self, index):
        return self.rows()[index]

    def get_col_at(self, index):
        return self.columns()[index]

    def get_square(self, row, col):
        row = self.get_row_at(row)
        square = row[col]
        return square

    def empty_squares(self):
        flattened_board = self.flattened_board()
        index_replaced_list = [(idx if val == None else None) for idx, val in enumerate(flattened_board, start=1)]
        return [element for element in index_replaced_list if element != None]

    def is_full(self):
        flattened_board = self.flattened_board()
        list_of_empties = [element for element in flattened_board if element == None]
        return len(list_of_empties) == 0

    def flattened_board(self):
        return [item for sublist in self.board() for item in sublist]