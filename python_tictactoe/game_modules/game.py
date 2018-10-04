class Game:

    def __init__(self, board, rules):
        self.__board = board
        self.__rules = rules
        self.__players = []
        self.__current_player = None

    def is_won(self):
        return self.get_rules().has_winning_row() or self.get_rules().has_winning_column() or self.get_rules().has_winning_diagonal()

    def is_over(self):
        return self.is_won or self.get_board().is_full()

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
        
    #def mark_square(self, row, col):

    #switch_player

    #valid_move(move)


