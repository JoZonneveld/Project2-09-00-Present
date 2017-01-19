import pygame
from Color import *
def Settings(screen, BackGround, button, Proccess):
    while Proccess:
        pygame.display.set_caption('Battleport')
        screen.fill(black)


        pygame.display.update()

    pygame.quit()