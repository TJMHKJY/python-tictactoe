class Board:

    def __init__(self, row_size=3):
        self.row_size = row_size

    def create_board(self, row_size):
        return [[None] * row_size] * row_size

    def rows(self, board): 
        return board

    def columns(self, board):
        zipped = zip(*board)
        columns = [list(x) for x in zipped]
        return columns

    def left_diagonal(self, board):
        left_diagonal = [val[idx] for idx, val in enumerate(board)]
        return left_diagonal

    def right_diagonal(self, board):
        right_diagonal = [val[len(board) - (idx + 1)] for idx, val in enumerate(board)]
        return right_diagonal

    def diagonals(self, board):
        return [self.left_diagonal(board), self.right_diagonal(board)]
   
    def get_row_at(self, board, index):
        return self.rows(board)[index]

    def get_col_at(self, board, index):
        return self.columns(board)[index]

    def get_square(self, board, row, col):
        row = self.get_row_at(board, row)
        square = row[col]
        return square

    def empty_squares(self, board):
        flattened_board = [item for sublist in board for item in sublist]
        index_replaced_list = [(idx if val == None else None) for idx, val in enumerate(flattened_board, start=1)]
        return [element for element in index_replaced_list if element != None]

    def is_full(self, board):
        flattened_board = [item for sublist in board for item in sublist]
        list_of_empties = [element for element in flattened_board if element == None]
        return len(list_of_empties) == 0