import pygame
from Color import *
def main_screen(screen, BackGround, button, Proccess):
    while Proccess:
        pygame.display.set_caption('Battleport')
        screen.fill(black)
        screen.blit(BackGround.image, BackGround.rect)

        button.Start(screen, 350, 250, 300, 70)
        button.Rules(screen, 25, 25, 100, 70)
        button.Setting(screen, 350, 350, 300, 70)
        button.Exit(screen, 350, 450, 300, 70)
        pygame.display.update()

    pygame.quit()