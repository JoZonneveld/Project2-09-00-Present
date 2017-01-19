import pygame

from Color import *
def Rules(screen, BackGround, button, Proccess):
    while Proccess:
        pygame.display.set_caption('Battleport')
        screen.fill(black)
        screen.blit(BackGround.image, BackGround.rect)


