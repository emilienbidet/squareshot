import pygame
from src.game_config import *

class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(GameConfig.WALL_IMAGE[0])
        self.image = pygame.transform.scale(self.image, (GameConfig.WALL_WIDTH, GameConfig.WALL_HEIGHT))
        self.rect = pygame.Rect(GameConfig.WALL_WIDTH*x, GameConfig.WALL_HEIGHT*y, GameConfig.WALL_WIDTH, GameConfig.WALL_HEIGHT)

    def draw(self,window):
        window.blit(self.image ,self.rect.topleft)
