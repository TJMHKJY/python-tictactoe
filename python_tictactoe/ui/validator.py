class Validator:

    def is_valid_name(self, name):
        return False if len(name) <= 1 else True

    def is_valid_icon(self, icon):
        return False if len(icon) <= 1 else True

    def is_valid_turn_order(self, turn_order):
        return False if len(turn_order) <= 1 else True

    def is_valid_move(self, move):
        return False if len(move) <= 1 else True
