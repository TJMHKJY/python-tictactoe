class Game:

    def __init__(self, board, rules):
        self.__board = board
        self.__rules = rules
        self.__players = []
        self.__current_player = None

    def is_won(self):
        return self.get_rules().has_winning_row() or self.get_rules().has_winning_column() or self.get_rules().has_winning_diagonal()

    def is_over(self):
        return self.is_won() or self.get_board().is_full()

    def is_tied(self):
        return self.get_board().is_full() and not self.is_won

    def get_board(self):
        return self.__board

    def get_rules(self):
        return self.__rules

    def add_player(self, value):
        self.__players.append(value) 

    def get_players(self):
        return self.__players

    def set_current_player(self, player):
        self.__current_player = player

    def get_current_player(self):
        return self.__current_player

    def mark_square(self, square, icon):
        coordinates = self.get_rules().square_to_rows_and_cols(square, self.get_board().get_row_size())
        row_coordinate = coordinates[0]
        column_coordinate = coordinates[1]
        row_to_update = self.get_board().get_row_at(row_coordinate)
        row_to_update[column_coordinate] = icon
        return self

    def unmark_square(self, square):
        coordinates = self.get_rules().square_to_rows_and_cols(square, self.get_board().get_row_size())
        row_coordinate = coordinates[0]
        column_coordinate = coordinates[1]
        row_to_update = self.get_board().get_row_at(row_coordinate)
        row_to_update[column_coordinate] = None
        return self

    def switch_current_player(self):
        player_1 = self.get_players()[0]
        player_2 = self.get_players()[1]
        self.set_current_player(player_2) if self.get_current_player() == player_1 else self.set_current_player(player_1)

    def is_valid_move(self, square):
        coordinates = self.get_rules().square_to_rows_and_cols(square, self.get_board().get_row_size())
        row_coordinate = coordinates[0]
        column_coordinate = coordinates[1]
        return self.get_board().get_square(row_coordinate, column_coordinate) == None