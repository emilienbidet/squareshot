import pygame
from src.game_config import *
import math

class Bullet(pygame.sprite.Sprite):

    def __init__(self, player, player_type, mouse_pos):
        """
            Method to create a new Bullet
        """
        super().__init__()
        self.player = player
        # Bullet's hitbox
        x = player.rect.x + GameConfig.PLAYER_WIDTH/4
        y = player.rect.y + GameConfig.PLAYER_HEIGHT/4
        self.rect = pygame.Rect(x, y, GameConfig.BULLET_WIDTH, GameConfig.BULLET_HEIGHT)
        # Bullet's image
        self.image = pygame.image.load(GameConfig.BULLET_IMAGE[player_type])
        self.image = pygame.transform.scale(self.image, (GameConfig.BULLET_WIDTH, GameConfig.BULLET_HEIGHT))
        # Bullet's angle
        self.angle = self.get_angle(mouse_pos)

    def draw(self, window):
        """
            Method to draw the bullet
        """
        window.blit(self.image ,self.rect.topleft)

    def get_angle(self, mouse_pos):
        """
            Method to get the angle in radian
        """
        mouse_x, mouse_y = mouse_pos
        player_x, player_y = self.player.rect.x + GameConfig.PLAYER_WIDTH/4, self.player.rect.y + GameConfig.PLAYER_HEIGHT/4
        return math.atan2(mouse_y-player_y, mouse_x-player_x)

    def update(self):
        """
            Method to update the bullet
        """
        self.move()

    def move(self):
        """
            Method to move the bullet according to its angle
        """
        self.rect.x += int(math.cos(self.angle)*GameConfig.BULLET_SPEED)
        self.rect.y += int(math.sin(self.angle)*GameConfig.BULLET_SPEED)
