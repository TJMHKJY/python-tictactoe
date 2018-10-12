import copy
import random
from python_tictactoe.game.game import Game

class MinimaxStrategy:
        
    def best_move(self, game, game_params):
        output = game_params['cli_output'] 
        messages = game_params['messages']
        current_player = game.get_current_player()
        name = current_player.name

        output.display(messages.computer_move(name))
        move = self.minimax(game)
        output.display(messages.confirm_move(name, move))  
        return move

    def random(self, game):
        available_squares = game.get_board().empty_squares()
        return random.choice(available_squares)
        
    def place_move(self, game, square):
        game.mark_square(square, game.get_current_player().icon)
        game.switch_current_player()
        return game

    def minimax(self, game, depth=0, scores_map=None):
        if not scores_map:
            scores_map = {}

        available_squares = game.get_board().empty_squares()
        
        if game.is_over():
            return self.player_score_value(game)
        else:
            for square in available_squares:
                scores_map[square] = -1 * self.minimax(self.place_move(game, square), depth+1, {})

                game.unmark_square(square)
                game.switch_current_player()

            if depth == 0:
                return self.highest_score(scores_map)
            elif depth > 0:
                return self.best_score(scores_map)

    def player_score_value(self, game):
        return -1 if game.is_won() else 0

    def best_score(self, scores_dict):
        return max(scores_dict.values())

    def highest_score(self, scores_dict):
        score_tuple = max(scores_dict.items(), key=lambda k: k[1])
        return score_tuple[0]

    def available_squares(self, flattened_board):
        index_replaced_list = [(idx if val == None else None) for idx, val in enumerate(flattened_board, start=1)]
        return [element for element in index_replaced_list if element != None]

    # def evaluate_board(self, game, depth):
    #     if game.is_won():
    #         if(game.get_rules().winning_icon(game.get_board().rows()) == game.get_current_player().icon):
    #             return 10 - depth
    #         else: 
    #             return -10 + depth 
    #     else:
    #         return 0

    # def get_score(self, game):
    #     player_icon = game.get_current_player().icon
    #     opponent_icon = game.get_players[0].icon if player_icon == game.get_players[0].icon else game.get_players[1].icon

    #     if game.is_over():
    #         if game.winning_icon  == player_icon:
    #             return 1
    #         elif game.winning_icon == opponent_icon:
    #             return -1
    #     return 0