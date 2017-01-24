from msilib import Table

import pygame
from Color import *
from database import *

def process_events():
    pygame.init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def Score(screen, button):
    print("Naam", " Beurten")
    for row in download_scores():
        print(row[1], row[2])



    while process_events():
        pygame.display.set_caption('Battleport')
        screen.fill(black)
        button.Back(screen, 900, 25, 100, 70)
        pygame.display.update()
    quit()