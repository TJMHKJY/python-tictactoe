from python_tictactoe.app.game_config import GameConfig
from python_tictactoe.app.game_loop import GameLoop
from python_tictactoe.app.game_over import GameOver
from python_tictactoe.ui.cli_messages import CliMessages
from python_tictactoe.ui.input import Input
from python_tictactoe.ui.output import Output
from python_tictactoe.ui.validator import Validator
from python_tictactoe.game.rules import Rules
from python_tictactoe.game.board import Board
from python_tictactoe.game.game import Game


class App:

    def run(self):
        messages = CliMessages()
        
        game_params = {
            'messages': messages,
            'cli_input': Input(),
            'cli_output': Output(),
            'validator': Validator()
        }

        board = Board()
        rules = Rules(board)
        game = Game(board, rules)

        game = GameConfig().run(game, game_params)
        game = GameLoop().run(game, game_params)
        GameOver().run(game, game_params)