from Color import *
import pygame 
def program():
    pygame.init()

    width = 1024
    height = 768

    size = (width, height)

    screen = pygame.display.set_mode(size)

    while True:
        screen.fill(Deep_Sky_Blue)

        pygame.display.flip()