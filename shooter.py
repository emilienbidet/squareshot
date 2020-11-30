import pygame
from src.map import *
from src.game_config import *
from src.game_state import *
from src.player_state import *
from src.ia import *

def playAgain():
    return False

def game_loop(window, clock):
    #Initialiser les variables;
    game_state = GameState()
    ia = IA(game_state)


    while game_state.game_result == "In Game":
        clock.tick(60)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        next_player_state = get_next_player_state(events)
        next_ia_state = ia.get_next_ia_state()
        # Modifier l'état du jeu (GameState)
        game_state.update(next_player_state, next_ia_state)

        # Afficher l'écran
        game_state.draw(window)
        pygame.display.update()

    show_winner(window, game_state.game_result)
    pygame.display.update()
    pygame.time.delay(4000)

    if playAgain == True:
        game_loop(window)



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

def show_winner(window, res):
    font_obj = pygame.font.Font('font/IBMPlexMono-Medium.ttf', 32)

    text_surface_obj = font_obj.render(res, True, GameConfig.TEXT_COLOR)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (GameConfig.WINDOW_WIDTH/2, GameConfig.WINDOW_HEIGHT/2)
    window.blit(text_surface_obj, text_rect_obj)

def main():
    pygame.init()
    window = pygame.display.set_mode((GameConfig.WINDOW_WIDTH, GameConfig.WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Shooter PyGame")
    game_loop(window,  clock)

    pygame.quit()
    exit()



main()
