from python_tictactoe.app.game_config import GameConfig
from python_tictactoe.ui.cli_messages import CliMessages

class App:

    def run(self):
        self.game_config(CliMessages)

    def game_config(self, messages):
        cli_messages = messages()
        print(cli_messages.welcome_message())
        #game_config = GameConfig()
        #GameConfig
        #game set up, cli messages

    #def game_loop(self):
        #game loop, print board

    #def game_over(self):
        #game over, cli messages