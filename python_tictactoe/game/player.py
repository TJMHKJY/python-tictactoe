class Player:

    def __init__(self, name, icon, strategy):
        self.name = name
        self.icon = icon
        self.strategy = strategy

    def select_move(self, game, game_params):
        return self.strategy.best_move(game, game_params)