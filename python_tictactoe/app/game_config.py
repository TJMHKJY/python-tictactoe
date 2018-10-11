from python_tictactoe.game.game import Game
from python_tictactoe.game.player import Player
from python_tictactoe.strategy.input_strategy import InputStrategy
from python_tictactoe.strategy.minimax_strategy import MinimaxStrategy

class GameConfig:

    def run(self, game, game_params):
        self.intro(game_params)
        player_settings = self.player_config(game_params)
        game = self.create_game(game.get_board(), game.get_rules())
        return self.create_players(player_settings, game)

    
    def intro(self, game_params):
        messages = game_params['messages']
        output = game_params['cli_output']
        output.display(messages.welcome_message())

    
    def player_config(self, game_params):
        messages = game_params['messages']
        output = game_params['cli_output']
        
        name = self.get_name(game_params)
        icon = self.get_icon(game_params) 
        turn_order = self.get_turn_order(game_params)

        output.display(messages.confirm_computer_name(messages.computer_name()))
        output.display(messages.confirm_computer_icon(messages.computer_icon()))
        output.display(messages.confirm_computer_turn_order(turn_order))

        return {
            'name': name,
            'icon': icon,
            'turn_order': turn_order,
            'computer_name': messages.computer_name(),
            'computer_icon': messages.computer_icon()
        }

    
    def create_game(self, board, rules):
        return Game(board, rules)

    
    def create_players(self, player_settings, game):
        player_settings['human_player'] = Player(player_settings['name'], player_settings['icon'], InputStrategy())
        player_settings['computer_player'] = Player(player_settings['computer_name'], player_settings['computer_icon'], MinimaxStrategy())
        return self.add_players_to_game(player_settings, game)


    def add_players_to_game(self, player_settings, game):
        human_player = player_settings['human_player']
        computer_player = player_settings['computer_player']
        if player_settings['turn_order'] == "1":
            game.add_player(human_player) 
            game.add_player(computer_player)
            game.set_current_player(human_player)
        else: 
            game.add_player(computer_player) 
            game.add_player(human_player)
            game.set_current_player(computer_player)
        return game


    def get_name(self, game_params):
        messages = game_params['messages']
        cli_input = game_params['cli_input']

        name = cli_input.get_input(messages.ask_for_name())
        return self.validate_name(name, game_params)


    def get_icon(self, game_params):
        messages = game_params['messages']
        cli_input = game_params['cli_input']

        icon = cli_input.get_input(messages.ask_for_icon())
        return self.validate_icon(icon, game_params)


    def get_turn_order(self, game_params):
        messages = game_params['messages']
        cli_input = game_params['cli_input']

        turn_order = cli_input.get_input(messages.ask_for_turn_order())
        return self.validate_turn_order(turn_order, game_params)


    def validate_name(self, name, game_params):
        messages = game_params['messages']
        validator = game_params['validator']
        output = game_params['cli_output']

        if validator.is_valid_name(name):
            output.display(messages.confirm_name(name))
            return(name)
        else:
            print(messages.invalid_user_name())
            return(self.get_name(game_params))


    def validate_icon(self, icon, game_params):
        messages = game_params['messages']
        validator = game_params['validator']
        output = game_params['cli_output']

        if validator.is_valid_icon(icon):
            output.display(messages.confirm_icon(icon))
            return(icon)
        else:
            output.display(messages.invalid_user_icon())
            return(self.get_icon(game_params))


    def validate_turn_order(self, turn_order, game_params):
        messages = game_params['messages']
        validator = game_params['validator']
        output = game_params['cli_output']

        if validator.is_valid_turn_order(turn_order):
            output.display(messages.confirm_turn_order(turn_order))
            return(turn_order)
        else:
            output.display(messages.invalid_turn_order())
            return(self.get_turn_order(game_params))