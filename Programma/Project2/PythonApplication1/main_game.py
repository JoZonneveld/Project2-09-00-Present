import pygame
from Color import *

def process_events():
    pygame.init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def main_game(screen):
    while process_events():
        pygame.display.set_caption('Battleport')
        screen.fill(black)
        pygame.display.update()