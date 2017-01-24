import pygame
from Color import *
from database import *
from astropy import Table, Column

def process_events():
    pygame.init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def Score(screen, button):
    data_rows = [download_scores()]

    t = Table(rows=data_rows, names=('a', 'b', 'c'))

    print(t)

    while process_events():
        pygame.display.set_caption('Battleport')
        screen.fill(black)
        button.Back(screen, 900, 25, 100, 70)
        pygame.display.update()
    pygame.quit()