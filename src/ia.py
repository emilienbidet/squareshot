from src.player_state import *

class IA(object):
    """docstring for IA."""
    STATES = ["STANDBY",
              "DODGE"]

    def __init__(self, game_state):
        self.state = IA.STATES[0]
        self.game_state = game_state

    def get_next_ia_state(self):
        next_ia_state = PlayerState()
        next_ia_state.shot = True
        next_ia_state.mouse_pos = self.shot_to_player()
        return next_ia_state

    def shot_to_player(self):
        return self.game_state.player_1.rect.center
