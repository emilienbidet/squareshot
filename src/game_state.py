from src.game_config import *
from src.player import *
from src.wall import *

class GameState:

    def __init__(self):
        self.player_1 = Player(0, self)
        self.player_2 = Player(1, self)
        self.walls = pygame.sprite.Group()

        for y in [0,11]:
            for x in range(12):
                self.walls.add(Wall(y,x))

    def update(self, player_1_state, player_2_state):
        self.player_1.update(player_1_state)
        self.player_2.update(player_2_state)
        GameState.remove_bullets_collided(self.player_1.bullets, self.player_2.bullets, self.walls)
        GameState.remove_bullets_on_player(self.player_1, self.player_2)

    def draw(self, window):
        window.fill(GameConfig.COLOR_BLUE)
        self.player_1.draw(window)
        self.player_2.draw(window)
        self.player_1.bullets.draw(window)
        self.player_2.bullets.draw(window)
        GameState.draw_all(window, self.walls)

    def draw_all(window, group):
        for element in group:
            element.draw(window)

    def check_collisions(self, sprite, group):
        return pygame.sprite.spritecollideany(sprite, group)

    def remove_bullets_on_player(player_1, player_2):
        pygame.sprite.spritecollide(player_1, player_2.bullets, True)
        pygame.sprite.spritecollide(player_2, player_1.bullets, True)

    def remove_bullets_collided(player_1_bullets, player_2_bullets, walls):
        """
            Remove Bullets when they are collide or when they are in a wall
        """
        pygame.sprite.groupcollide(player_1_bullets, player_2_bullets, True, True)
        pygame.sprite.groupcollide(player_1_bullets, walls, True, False)
        pygame.sprite.groupcollide(player_2_bullets, walls, True, False)
