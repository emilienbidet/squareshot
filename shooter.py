import pygame
from src.game_config import *
from src.game_state import *

def playAgain():
    return False

def game_loop(window):
    #Initialiser les variables;
    game_over = False;
    leaving = False
    gameState = GameState()
    while not game_over and not leaving:
        pygame.time.delay(20)
        #Gérer les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                leaving = True
        #Modifier l'état du jeu (GameState)
        gameState.update()
        #Afficher l'écran
        gameState.draw(window)
        pygame.display.update()
        #Structure conditionnel avec if pour dire la fin de la partie
    if playAgain == True:
        game_loop(window)

def main():
    window = pygame.display.set_mode((GameConfig.WINDOW_WIDTH, GameConfig.WINDOW_HEIGHT))
    pygame.init()
    pygame.display.set_caption("Shooter PyGame")
    game_loop(window)

    pygame.quit()
    exit()



main()
