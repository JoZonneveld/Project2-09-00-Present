import pygame
from Color import *
def main_screen(screen, BackGround, button, Proccess):
    while Proccess:
        pygame.display.set_caption('Battleport')
        screen.fill(black)
        screen.blit(BackGround.image, BackGround.rect)


        pygame.display.update()

    pygame.quit()