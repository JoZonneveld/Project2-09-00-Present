import pygame
from Color import *

def process_events():
    pygame.init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def Settings(screen, button, BackGround):
    while process_events():
        pygame.display.set_caption('Battleport')
        screen.blit(BackGround.image, BackGround.rect)
        button.Back(screen, 900, 25, 100, 70)
        pygame.display.update()