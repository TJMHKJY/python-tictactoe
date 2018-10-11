from python_tictactoe.game.game import Game
from python_tictactoe.game.player import Player
from python_tictactoe.strategy.input_strategy import InputStrategy
from python_tictactoe.strategy.minimax_strategy import MinimaxStrategy

class GameLoop:

    def run(self, game, game_params):
        if not game.is_over():
            self.place_move(game, game_params)
            game.switch_current_player()
            return self.run(game, game_params)
        else:
            return game
        
        
    def place_move(self, game, game_params):
        current_player = game.get_current_player()
        move = current_player.select_move(game, game_params)
        
        self.mark_board(move, game, game_params)

    
    def mark_board(self, move, game, game_params):
        output = game_params['cli_output']
        messages = game_params['messages']
        current_player = game.get_current_player()

        move_int = int(move)
        if game.is_valid_move(move_int):
            game.mark_square(move_int, current_player.icon)
        else:
            output.display(messages.invalid_move())
            self.place_move(game, game_params)