class InputStrategy:

    def best_move(self, game, game_params):
        name = game.get_current_player().name
        return self.get_move(name, game_params)
    
    def get_move(self, name, game_params):
        messages = game_params['messages']
        game_input = game_params['cli_input']
        
        move = game_input.get_input(messages.announce_turn(name))
        return self.validate_move(move, name, game_params)

    def validate_move(self, move, name, game_params):
        messages = game_params['messages']
        validator = game_params['validator']
        output = game_params['cli_output']

        if validator.is_valid_move(move):
            output.display(messages.confirm_move(name, move))
            return(move)
        else:
            output.display(messages.invalid_move())
            return(self.get_move(name, game_params))