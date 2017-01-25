import pygame
from Color import *
from database import *
def process_events():
    pygame.init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def main_game(screen, button, BackGround_Game):
    upload_score('test', 5)
    while process_events():
        pygame.display.set_caption('Battleport')
        screen.blit(BackGround_Game.image, BackGround_Game.rect)
        button.Back(screen, 900, 25, 100, 70)
        pygame.display.update()
    pygame.quit()

