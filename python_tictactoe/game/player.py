class Player:

    def __init__(self, name, icon, strategy):
        self.name = name
        self.icon = icon
        self.strategy = strategy

    def select_move(self, gamestate):
        return self.strategy.best_move(gamestate)