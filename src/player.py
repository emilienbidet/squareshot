import pygame
from src.game_config import *

class Player:

    #CONFIGURATION ET PROPRIETES
    IMAGE_FOR_PLAYERS = ["media/player.png", "media/ia.png"]

    HEIGHT = 40
    WIDTH = HEIGHT

    SPEED = 2

    def __init__(self, type_player):
        ## IA OU PLAYER :
        self.type_player = type_player

        #HITBOX
        self.rect = pygame.Rect(GameConfig.WINDOW_WIDTH/2, GameConfig.WINDOW_HEIGHT/2, Player.WIDTH, Player.HEIGHT)

        #IMAGE
        self.image = pygame.image.load(Player.IMAGE_FOR_PLAYERS[type_player])

        #POSITION, MOVE, ACCELERATION, ETC
        self.position = (GameConfig.WINDOW_WIDTH/2, GameConfig.WINDOW_HEIGHT/2)
        self.vx = 0
        self.vy = 0

        #ETAT, PROPRIETES DE JOUEUR
        self.vie = 100
        self.endurance = 100

        self.acceleration = 1
        self.tired = False


    def draw(self, window):
        window.blit(self.image ,self.rect.topleft)

    def update(self):
        print("Endurance : " + str(self.endurance))
        self.move()
        self.recepurationEndurance()

    def move(self):
        keys = pygame.key.get_pressed()
        vx = 0
        vy = 0

        if keys[pygame.K_z]:
            vy-=1
        if keys[pygame.K_q]:
            vx-=1
        if keys[pygame.K_s]:
            vy+=1
        if keys[pygame.K_d]:
            vx+=1

        self.vx = vx
        self.vy = vy

        if self.isRunning():
            self.acceleration = 2
        else:
            self.acceleration = 1

        self.rect = self.rect.move(vx*Player.SPEED*self.acceleration, vy*Player.SPEED*self.acceleration)

        if self.acceleration == 2:
            self.endurance -= 2
            if self.endurance <= 0:
                self.tired = True

    def isRunning(self):
        if pygame.key.get_pressed()[pygame.K_LSHIFT] and self.endurance > 0 and not self.tired:
            return True
        return False

    def recepurationEndurance(self):
        if self.endurance < 100:
            self.endurance+=1
        else:
            self.tired = False

    def shot():
        #make bullet
        return 0
