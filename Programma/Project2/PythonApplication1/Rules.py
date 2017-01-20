import pygame
from Color import *


def process_events():
    pygame.init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def Rules(screen, BackGround_Rules):
    while process_events():
        pygame.display.set_caption('Rules')
        screen.fill(black)
        screen.blit(BackGround_Rules.image, BackGround_Rules.rect)
        pygame.display.update()




