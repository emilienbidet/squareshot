from src.game_config import *
from src.player import *
from src.wall import *

class GameState:

    def __init__(self):
        self.player = Player(0)
        self.walls = [Wall(0,3), Wall(1,3), Wall(2,3), Wall(2,4), Wall(3,1), Wall(4,1), Wall(4,2),Wall(4,3)]


    def update(self):
        self.player.update()

    def draw(self, window):
        window.fill(GameConfig.COLOR_BLUE)
        self.player.draw(window)
        self.draw_walls(window)

    def draw_walls(self,window):
        for wall in self.walls:
            wall.draw(window)
