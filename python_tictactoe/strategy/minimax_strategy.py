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
        game_copy = copy.deepcopy(game)
        move = self.random(game_copy)
        output.display(messages.confirm_move(name, move))  
        return move

    def random(self, game):
        available_squares = game.get_board().empty_squares()
        return random.choice(available_squares)
        
    def place_move(self, game, square):
        game.mark_square(square, game.get_current_player().icon)
        game.switch_current_player()
        return game

    # def minimax_alt(self, game, depth=0, scores_map={}):
    #     available_squares = game.get_board().empty_squares()
        
    #     if game.is_over():
    #         return self.player_score_value(game)
    #     else:
    #         for square in available_squares:
    #             scores_map[square] = -1 * self.minimax_alt(self.place_move(game, square), depth+1, {})

    #             game.unmark_square(square)
    #             game.switch_current_player()

    #         if depth == 0:
    #             return self.highest_score(scores_map)
    #         elif depth > 0:
    #             return self.best_score(scores_map)

    # def player_score_value(self, game):
    #     return -1 if game.is_won() else 0

    # def best_score(self, scores_dict):
    #     return max(scores_dict.values())

    # def highest_score(self, scores_dict):
    #     score_tuple = max(scores_dict.items(), key=lambda k: k[1])
    #     return score_tuple[0]

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


    # def minimax_ruby(self, game, depth=0, scores_map={}):
    #     available_squares = game.get_board().empty_squares()
        
    #     if game.is_over():
    #         return self.player_score_value(game)
    
    #     for square in available_squares:

    #         self.place_move(game, square)
    #         game.switch_current_player()
    #         #print(scores_map[square])
    #         scores_map[square] =  -1 * self.minimax_ruby(game, depth+1, {})

    #         game.unmark_square(square)
    #         game.switch_current_player()

    #     if depth == 0:
    #         return self.highest_score(scores_map)
    #     elif depth > 0:
    #         return self.best_score(scores_map) 


    # def minimax_geeks(self, game, player, max_depth, depth=0):
    #     if ( game.is_over() or depth == max_depth ):
    #         return self.evaluate_board(game, depth), None
        
    #     best_move = None

    #     if ( game.get_current_player() == game.get_players()[0] ):
    #         best_score = -1000
    #     else:
    #         best_score = +1000

    #     for square in game.get_board().empty_squares():
            
    #         new_game = game.mark_square(square, game.get_current_player().icon)
    #         score, move = self.minimax_geeks(new_game, player, max_depth, depth+1)

    #         if ( new_game.get_current_player() == player ):
    #             if ( score > best_score ): # max
    #                 best_score = score
    #                 best_move = move
    #             elif ( score < best_score ): # min
    #                 best_score = score
    #                 best_move = move

    #         #game.unmark_square(square)

    #     return best_score, best_move

    # def minimax_geeks_2(self, game, depth, is_max):
    #     current_player = game.get_current_player()
    #     available_squares = game.get_board().empty_squares()
    #     player1 = game.get_players()[0]
    #     player2 = game.get_players()[1]
    #     opponent = player2 if current_player.icon == player1.icon else player1

    #     score = self.evaluate_board(game, depth)

    #     if(score == 10):
    #         return score - depth
    #     elif(score == -10):
    #         return score + depth
    #     if (game.get_board().is_full()): 
    #         return 0

    #     if is_max:
    #         best = -1000
    #         for square in available_squares:
    #             game.mark_square(square, current_player.icon)
    #             best = max(best, self.minimax_geeks_2(game, depth+1, not is_max))
    #             game.unmark_square(square)
    #         return best
    #     else:
    #         best = 1000
    #         for square in available_squares:
    #             game.mark_square(square, opponent.icon)
    #             best = min(best, self.minimax_geeks_2(game, depth+1, not is_max))
    #             game.unmark_square(square)
    #         return best


    # def maximized_move(self, game):   
    #     bestscore = None
    #     bestmove = None

    #     player_icon = game.get_current_player().icon
    #     opponent_icon = game.get_players[0].icon if player_icon == game.get_players[0].icon else game.get_players[1].icon

    #     for square in game.get_board().empty_squares():
    #         game.mark_square(square, player_icon)
       
    #         if game.is_over():
    #             score = self.get_score(game)
    #         else:
    #             move_position, score = self.minimized_move(game)
       
    #         game.unmark_square(square)
           
    #         if bestscore == None or score > bestscore:
    #             bestscore = score
    #             bestmove = square

    #     return bestmove, bestscore

    # def minimized_move(self, game):

    #     bestscore = None
    #     bestmove = None

    #     player_icon = game.get_current_player().icon
    #     opponent_icon = game.get_players[0].icon if player_icon == game.get_players[0].icon else game.get_players[1].icon

    #     for square in game.game.get_board().empty_squares():
    #         game.mark(square, opponent_icon)
       
    #         if game.is_gameover():
    #             score = self.get_score(game)
    #         else:
    #             move_position, score = self.maximized_move(game)
       
    #         game.revert_last_move()
           
    #         if bestscore == None or score < bestscore:
    #             bestscore = score
    #             bestmove = square

    #     return bestmove, bestscore


    # def get_score(self, game):
    #     player_icon = game.get_current_player().icon
    #     opponent_icon = game.get_players[0].icon if player_icon == game.get_players[0].icon else game.get_players[1].icon

    #     if game.is_over():
    #         if game.winning_icon  == player_icon:
    #             return 1
    #         elif game.winning_icon == opponent_icon:
    #             return -1
    #     return 0
