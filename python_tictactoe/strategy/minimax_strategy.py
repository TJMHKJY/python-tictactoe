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

    def available_squares(self, flattened_board):
        index_replaced_list = [(idx if val == None else None) for idx, val in enumerate(flattened_board, start=1)]
        return [element for element in index_replaced_list if element != None]