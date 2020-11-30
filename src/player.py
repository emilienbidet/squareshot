import pygame
from src.game_config import *
from src.bullet import *

class Player(pygame.sprite.Sprite):

    def __init__(self, player_type, game):
        super().__init__()
        self.game = game
        # Player
        self.player_type = player_type
        # Player's hitbox
        self.rect = pygame.Rect((GameConfig.PLAYER_SPAWNS[player_type]), (GameConfig.PLAYER_WIDTH, GameConfig.PLAYER_HEIGHT))
        # Player's image
        self.image = pygame.image.load(GameConfig.PLAYER_IMAGE[player_type])
        self.image = pygame.transform.scale(self.image, (GameConfig.PLAYER_WIDTH, GameConfig.PLAYER_HEIGHT))
        # Player's state
        self.health = 100
        self.stamina = 100
        self.acceleration = 1
        self.tired = False
        self.bullets = pygame.sprite.Group()
        # Last bullet
        self.last = pygame.time.get_ticks()

    def update(self, next_state):
        self.move(next_state)
        self.updateStamina(next_state)
        self.recoverStamina()
        self.shot(next_state)
        [bullet.move() for bullet in self.bullets]
        self.update_health_stamina_bar()

    def update_health_stamina_bar(self):
        self.health_bar_position = [self.rect.x,self.rect.y - GameConfig.BAR_OFFSET - GameConfig.BAR_HEIGHT,
                                    self.health*GameConfig.PLAYER_WIDTH/GameConfig.PLAYER_MAX_HEALTH,
                                    GameConfig.BAR_HEIGHT]
        self.max_health_bar_position = [self.rect.x,self.rect.y - GameConfig.BAR_OFFSET - GameConfig.BAR_HEIGHT,
                                        GameConfig.PLAYER_MAX_HEALTH*GameConfig.PLAYER_WIDTH/GameConfig.PLAYER_MAX_HEALTH,
                                        GameConfig.BAR_HEIGHT]
        self.stamina_bar_position = [self.rect.x,self.rect.y - GameConfig.BAR_OFFSET,
                                     self.stamina*GameConfig.PLAYER_WIDTH/GameConfig.PLAYER_MAX_STAMINA,
                                     GameConfig.BAR_HEIGHT]
        self.max_stamina_bar_position = [self.rect.x,self.rect.y - GameConfig.BAR_OFFSET,
                                         GameConfig.PLAYER_MAX_STAMINA*GameConfig.PLAYER_WIDTH/GameConfig.PLAYER_MAX_STAMINA,
                                         GameConfig.BAR_HEIGHT]


    def draw(self, window):
        """
            Method to draw the player
        """
        window.blit(self.image ,self.rect.topleft)
        self.bullets.draw(window)
        # Draw Bars
        pygame.draw.rect(window, GameConfig.BAR_NOTHING_COLOR, self.max_health_bar_position)
        pygame.draw.rect(window, GameConfig.BAR_HEALTH_COLOR, self.health_bar_position)
        pygame.draw.rect(window, GameConfig.BAR_NOTHING_COLOR, self.max_stamina_bar_position)
        pygame.draw.rect(window, GameConfig.BAR_STAMINA_COLOR, self.stamina_bar_position)


    def move(self, next_state):
        """
            Method to move the player's hitbox
        """
        # Player's acceleration
        if self.isRunning(next_state):
            self.acceleration = 2
        else:
            self.acceleration = 1

        # Player's hitbox
        x,y = 0,0
        if next_state.up:
            y += GameConfig.PLAYER_STATE_MOVES["UP"]
        if next_state.down:
            y += GameConfig.PLAYER_STATE_MOVES["DOWN"]
        if next_state.left:
            x += GameConfig.PLAYER_STATE_MOVES["LEFT"]
        if next_state.right:
            x += GameConfig.PLAYER_STATE_MOVES["RIGHT"]
        add_x = x*GameConfig.PLAYER_SPEED*self.acceleration
        add_y = y*GameConfig.PLAYER_SPEED*self.acceleration
        previous_rect = self.rect.copy()
        self.rect = self.rect.move(add_x, add_y)
        if self.game.check_collisions(self , self.game.walls):
            self.rect = previous_rect
            previous_rect = self.rect.copy()
            self.rect.x += add_x
            if self.game.check_collisions(self , self.game.walls):
                self.rect = previous_rect
                previous_rect = self.rect.copy()
                self.rect.y += add_y
                if self.game.check_collisions(self , self.game.walls):
                    self.rect = previous_rect


    def isRunning(self, next_state):
        """
            Method to check if the player is running
            return true if the player is running
        """
        if next_state.run and self.stamina > 0 and not self.tired:
            return True
        return False

    def updateStamina(self, next_state):
        """
            Method to increase / decrease the player's stamina
            By 2 while the player is running
            Set the tired mode to true if no more stamina
        """
        if self.acceleration == 2 and ((next_state.up ^ next_state.down) or (next_state.right ^ next_state.left)):
            self.stamina -= 2
            if self.stamina <= 0:
                self.tired = True

    def recoverStamina(self):
        """
            Method to recover the player's stamina
        """
        if self.stamina < 100:
            self.stamina +=1
        else:
            self.tired = False

    def shot(self, next_state):
        if next_state.shot:
            now = pygame.time.get_ticks()
            if now - self.last >= GameConfig.BULLET_COOLDOWN:
                self.last = now
                self.bullets.add(Bullet(self,self.player_type,next_state.mouse_pos))
