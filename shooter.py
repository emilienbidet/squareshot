import pygame
from src.game_config import *
from src.game_state import *
from src.player_state import *

def playAgain():
    return False

def game_loop(window, clock):
    #Initialiser les variables;
    game_over = False;
    game_state = GameState()


    while not game_over:
        clock.tick(60)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        next_player_state = get_next_player_state(events)
        next_ia_state = get_next_ia_state(game_state)
        # Modifier l'état du jeu (GameState)
        game_state.update(next_player_state, next_ia_state)

        # Afficher l'écran
        game_state.draw(window)
        pygame.display.update()

    if playAgain == True:
        game_loop(window)

def get_next_ia_state(game_state):
    next_ia_state = PlayerState()
    next_ia_state.shot = True
    next_ia_state.mouse_pos = (220,310)
    return next_ia_state

def get_next_player_state(events):
    next_player_state = PlayerState()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_z]:
        next_player_state.up = True
    if keys[pygame.K_s]:
        next_player_state.down = True
    if keys[pygame.K_d]:
        next_player_state.right = True
    if keys[pygame.K_q]:
        next_player_state.left = True
    if keys[pygame.K_LSHIFT]:
        next_player_state.run = True
    # Mouse actions
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            next_player_state.shot = True
            next_player_state.mouse_pos = pygame.mouse.get_pos()
    return next_player_state

def main():
    pygame.init()
    window = pygame.display.set_mode((GameConfig.WINDOW_WIDTH, GameConfig.WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Shooter PyGame")
    game_loop(window,  clock)

    pygame.quit()
    exit()



main()
