from src.game_config import *
from src.player import *

class GameState:

    def __init__(self):
        self.player = Player(0)

    def update(self):
        self.player.update()

    def draw(self, window):
        window.fill(GameConfig.COLOR_BLUE)
        self.player.draw(window)
