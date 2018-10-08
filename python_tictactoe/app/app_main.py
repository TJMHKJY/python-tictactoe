from python_tictactoe.ui.cli_messages import CliMessages
from python_tictactoe.ui.input import Input
from python_tictactoe.ui.validator import Validator
from python_tictactoe.game.rules import Rules
from python_tictactoe.game.board import Board
from python_tictactoe.game.game import Game
from python_tictactoe.game.player import Player
from python_tictactoe.strategy.input_strategy import InputStrategy
from python_tictactoe.strategy.minimax_strategy import MinimaxStrategy


class App:

    def run(self):
        messages = CliMessages()

        player_config_params = {
            'messages': messages,
            'game_input': Input(),
            'validator': Validator()
        }

        board = Board()
        rules = Rules(board)
        game = Game(board, rules)
        
        # game_config(player_config_params, game)
        self.intro(messages, board)
        player_settings = self.player_config(player_config_params)
        game = self.create_game(board, rules)
        print(messages.format_board_for_cli(game.get_board()))
        game = self.create_players(player_settings, game)

        # game loop(messages, game)
        # if game is not over
        # play loop
        # else 
        # self.game_over(messages, game)

        # game_over(messages, game)
        print(messages.format_board_for_cli(game.get_board()))
        self.check_for_win_or_tie(game, messages)
        print(messages.game_end())

        # minimax
        # input strategy

    def intro(self, messages, board):
        print(messages.welcome_message())
        print(messages.format_board_for_cli(board))

    def player_config(self, player_config_params):
        messages = player_config_params['messages']
        
        name = self.get_name(player_config_params)
        icon = self.get_icon(player_config_params) 
        turn_order = self.get_turn_order(player_config_params)

        print(messages.confirm_computer_name(messages.computer_name()))
        print(messages.confirm_computer_icon(messages.computer_icon()))
        print(messages.confirm_computer_turn_order(turn_order))

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

    def get_name(self, player_config_params):
        messages = player_config_params['messages']
        game_input = player_config_params['game_input']

        name = game_input.get_input(messages.ask_for_name())
        return self.validate_name(name, player_config_params)

    def get_icon(self, player_config_params):
        messages = player_config_params['messages']
        game_input = player_config_params['game_input']

        icon = game_input.get_input(messages.ask_for_icon())
        return self.validate_icon(icon, player_config_params)
    
    def get_turn_order(self, player_config_params):
        messages = player_config_params['messages']
        game_input = player_config_params['game_input']

        turn_order = game_input.get_input(messages.ask_for_turn_order())
        return self.validate_turn_order(turn_order, player_config_params)

    def validate_name(self, name, player_config_params):
        messages = player_config_params['messages']
        validator = player_config_params['validator']

        if validator.is_valid_name(name):
            print(messages.confirm_name(name))
            return(name)
        else:
            print(messages.invalid_user_name())
            return(self.get_name(player_config_params))

    def validate_icon(self, icon, player_config_params):
        messages = player_config_params['messages']
        validator = player_config_params['validator']

        if validator.is_valid_icon(icon):
            print(messages.confirm_icon(icon))
            return(icon)
        else:
            print(messages.invalid_user_icon())
            return(self.get_icon(player_config_params))

    def validate_turn_order(self, turn_order, player_config_params):
        messages = player_config_params['messages']
        validator = player_config_params['validator']

        if validator.is_valid_turn_order(turn_order):
            print(messages.confirm_turn_order(turn_order))
            return(turn_order)
        else:
            print(messages.invalid_turn_order())
            return(self.get_turn_order(player_config_params))
    
    # goes in game loop
    def get_move(self, name, player_config_params):
        messages = player_config_params['messages']
        game_input = player_config_params['game_input']
        
        move = game_input.get_input(messages.announce_turn(name))
        return self.validate_move(move, name, player_config_params)

    def validate_move(self, move, name, player_config_params):
        messages = player_config_params['messages']
        validator = player_config_params['validator']

        if validator.is_valid_move(move):
            print(messages.confirm_move(name, move))
            return(move)
        else:
            print(messages.invalid_move())
            return(self.get_move(name, player_config_params))

    # goes in game over
    def check_for_win_or_tie(self, game, messages):
        if game.is_over():
            player1 = game.get_players()[0]
            player2 = game.get_players()[1]
            winning_icon = game.get_rules().winning_icon(game.get_board().rows())
            winners_name = player1.name if player1.icon == winning_icon else player2.name
            return messages.game_won(winners_name) if game.is_won() else messages.game_tied()


        
