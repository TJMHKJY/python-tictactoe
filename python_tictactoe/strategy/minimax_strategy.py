import random
from python_tictactoe.game.game import Game

class MinimaxStrategy:

    #def best_move(self, game, depth=0, scores_map={}, input=None):
        
    def best_move(self, game, game_params):
        output = game_params['cli_output'] 
        messages = game_params['messages']
        current_player = game.get_current_player()
        name = current_player.name

        output.display(messages.computer_move(name))
        move = self.random(game)
        output.display(messages.confirm_move(name, move))  
        return move

    def random(self, game):
        available_squares = game.get_board().empty_squares()
        return random.choice(available_squares)

    def minimax(self, game, player, max_depth, depth=0):
        if ( game.is_over() or depth == max_depth ):
            return self.evaluate_board(game, depth), None
        
        best_calc_move = None

        if ( game.get_current_player() == game.get_players()[0] ):
            best_score = -1000
        else:
            best_score = +1000

        for square in game.get_board().empty_squares():
            
            new_game = game.mark_square(square, game.get_current_player().icon)
            score, move = self.minimax(new_game, player, max_depth, depth+1)

            if ( new_game.get_current_player() == player ):
                if ( score > best_score ): # max
                    best_score = score
                    best_calc_move = square
                elif ( score < best_score ): # min
                    best_score = score
                    best_calc_move = square

            #game.unmark_square(square)
            #or deepcopy... or clone?

        return best_score, best_calc_move
        

    def place_move(self, game, square):
        game.mark_square(square, game.get_current_player().icon)
        game.switch_current_player()
        return game

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

    def evaluate_board(self, game, depth):
        if game.is_won():
            if(game.get_rules().winning_icon(game.get_board().rows()) == game.get_current_player().icon):
                return 10 - depth
            else: 
                return -10 + depth 
        else:
            return 0

    ###
    # def best_move(self, game, depth=0, scores_map={}, input=None):
    # board_array = game.get_board().board()
    #     available_squares = game.get_board().empty_squares()
        
    #     if game.is_over():
    #         return self.player_score_value(game)
    
    #     for square in available_squares:
    #         scores_map[square] = -1 * self.best_move(self.place_move(game, square), depth+1, scores_map)
    #         #return scores_map[square] += depth if scores_map[square] < 0 else scores_map[square] -= depth    
    #         #reset

    #         if depth == 0:
    #             return self.highest_score(scores_map)
    #         elif depth > 0:
    #             return self.best_score(scores_map) 


    # def best_move(self, game):
    #     current_player = game.get_current_player()
    #     available_squares = game.get_board().empty_squares()
    #     bestVal = -1000
    #     bestMove = -1

    #     for square in available_squares:
    #         game.mark_square(square, current_player.icon)
    #         moveVal = self.minimax(game, 0, False)
    #         game.unmark_square(square)

    #         if moveVal > bestVal:
    #             bestMove = square
    #             bestVal = moveVal


    # def minimax(self, game, depth, is_max):
    #     current_player = game.get_current_player()
    #     available_squares = game.get_board().empty_squares()
    #     player1 = game.get_players()[0]
    #     player2 = game.get_players()[1]
    #     board_array = game.get_board().board()
    #     opponent = player2 if current_player.icon == player1.icon else player1

    #     score = self.evaluate_board(game)

    #     if(score == 10):
    #         return score - depth
    #     elif(score == -10):
    #         return score + depth
    #     if (game.get_board().is_full()): 
    #         return 0; 

    #     if is_max:
    #         best = -1000
    #         for square in available_squares:
    #             game.mark_square(square, current_player.icon)
    #             best = max(best, self.minimax(game, depth+1, not is_max))
    #             game.unmark_square(square)
    #         return best
    #     else:
    #         best = 1000
    #         for square in available_squares:
    #             game.mark_square(square, opponent.icon)
    #             best = min(best, self.minimax(game, depth+1, not is_max))
    #             game.unmark_square(square)
    #         return best

    ################################################

    # board_array = game.get_board().board()
    #     available_squares = game.get_board().empty_squares()
        
    #     if game.is_over():
    #         return self.player_score_value(game)
    
    #     for square in available_squares:
    #         print("square: " + str(square) + " avail: " + str(available_squares))
    #         print(scores_map)

    #         self.place_move(game, square)
    #         game.switch_current_player()

    #         scores_map[square] =  -1 * self.best_move(game, depth+1)

    #         game.unmark_square(square)
    #         game.switch_current_player()

    #     if depth == 0:
    #         return self.highest_score(scores_map)
    #     elif depth > 0:
    #         return self.best_score(scores_map) 