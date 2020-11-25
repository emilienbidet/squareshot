import pygame

class Wall(pygame.sprite.Sprite):

    WIDTH = 50
    HEIGHT = 50

    IMAGE = pygame.image.load("media/wall.png")

    def __init__(self, x, y):

        pygame.sprite.Sprite.__init__(self)
        self.image = Wall.IMAGE
        self.rect = pygame.Rect(50*x, 50*y, Wall.WIDTH, Wall.HEIGHT)

    def draw(self,window):
        window.blit(self.image ,self.rect.topleft)
