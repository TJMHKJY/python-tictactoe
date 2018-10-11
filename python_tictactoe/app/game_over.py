from python_tictactoe.game.game import Game
from python_tictactoe.game.player import Player
from python_tictactoe.strategy.input_strategy import InputStrategy
from python_tictactoe.strategy.minimax_strategy import MinimaxStrategy

class GameOver:

    def run(self, game, game_params):
        messages = game_params['messages']
        output = game_params['cli_output']

        output.display(messages.format_board_for_cli(game.get_board()))
        won_or_tied_message = self.check_for_win(game, messages)
        output.display(won_or_tied_message)
        output.display(messages.game_end())
        

    def check_for_win(self, game, messages):
        player1 = game.get_players()[0]
        player2 = game.get_players()[1]
        if game.is_won():
            winning_icon = game.get_rules().winning_icon(game.get_board().rows())
            winners_name = player1.name if player1.icon == winning_icon else player2.name
            return messages.game_won(winners_name)
        else:
            return messages.game_tied()