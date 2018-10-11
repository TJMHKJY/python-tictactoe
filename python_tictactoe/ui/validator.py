import re

class Validator:

    def is_valid_name(self, name):
        return False if len(name) <= 1 else True

    def is_valid_icon(self, icon):
        return True if re.search(r'^[A-Za-z]$', icon) else False

    def is_valid_turn_order(self, turn_order):
        return True if re.search(r'^[1|2]$', turn_order) else False

    def is_valid_move(self, move):
        return True if re.search(r'^[0-9]$', move) else False
