from src.game_config import *
from src.player import *
from src.wall import *
from src.map import *

class GameState:

    def __init__(self):
        self.game_result = "In Game"
        self.player_1 = Player(0, self)
        self.player_2 = Player(1, self)
        map = Map(int(GameConfig.WINDOW_WIDTH/GameConfig.WALL_WIDTH),
                  int(GameConfig.WINDOW_HEIGHT/GameConfig.WALL_HEIGHT),
                  GameConfig.WALL_QUANTITY)
        self.walls = map.walls

    def update(self, player_1_state, player_2_state):
        self.player_1.update(player_1_state)
        self.player_2.update(player_2_state)
        GameState.remove_bullets_collided(self.player_1.bullets, self.player_2.bullets, self.walls)
        self.update_health(self.player_1, self.player_2)

    def draw(self, window):
        window.fill(GameConfig.COLOR_BLUE)
        GameState.draw_all(window, self.walls)
        self.player_1.draw(window)
        self.player_2.draw(window)


    def draw_all(window, group):
        for element in group:
            element.draw(window)

    def check_collisions(self, sprite, group):
        return pygame.sprite.spritecollideany(sprite, group)

    def update_health(self, player_1, player_2):
        """
            Remove bullets if they touched the enemy and update his health
            If both death --> 3
            If player 1 death --> 2
            If player 2 death --> 1
        """
        player_1_delta_health = len(pygame.sprite.spritecollide(player_1, player_2.bullets, True)) * GameConfig.HEALTH_PER_BULLET
        player_2_delta_health = len(pygame.sprite.spritecollide(player_2, player_1.bullets, True)) * GameConfig.HEALTH_PER_BULLET
        if player_1.health - player_1_delta_health <= 0 and player_2.health - player_2_delta_health <= 0:
            player_1.health = 0
            player_2.health = 0
            self.game_result = "Null"
        elif player_1.health - player_1_delta_health <= 0:
            player_1.health = 0
            self.game_result = "Player 2"
        elif player_2.health - player_1_delta_health <= 0:
            player_2.health = 0
            self.game_result = "Player 1"
        else:
            player_1.health -= player_1_delta_health
            player_2.health -= player_2_delta_health

    def remove_bullets_collided(player_1_bullets, player_2_bullets, walls):
        """
            Remove Bullets when they are collide or when they are in a wall
        """
        pygame.sprite.groupcollide(player_1_bullets, player_2_bullets, True, True)
        pygame.sprite.groupcollide(player_1_bullets, walls, True, False)
        pygame.sprite.groupcollide(player_2_bullets, walls, True, False)
