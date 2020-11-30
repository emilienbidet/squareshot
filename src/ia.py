from src.player_state import *
import random
import pygame
from src.game_config import *

class IA(object):
    """docstring for IA."""
    STATES = ["STANDBY",
              "DODGE"]

    def __init__(self, game_state):
        self.state = IA.STATES[0]
        self.game_state = game_state
        self.last = pygame.time.get_ticks()
        self.last_state = PlayerState()

    def get_next_ia_state(self):
        now = pygame.time.get_ticks()
        if now - self.last >= 200:
            self.last = now
            next_ia_state = PlayerState()
            next_ia_state.shot = True
            next_ia_state.mouse_pos = self.shot_to_player()

            if bool(random.getrandbits(1)):
                next_ia_state.run = True

            if bool(random.getrandbits(1)):
                next_ia_state.up = True
            else:
                next_ia_state.down = True
            if bool(random.choice([0,0,0,0,0,1])):
                next_ia_state.right = True
            else:
                next_ia_state.left = True
            self.last_state = next_ia_state
            return next_ia_state
        else:
            return self.last_state

    def shot_to_player(self):
        return self.game_state.player_1.rect.center
