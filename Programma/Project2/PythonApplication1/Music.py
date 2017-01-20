import pygame
from pygame.locals import *

def music(screen):

    pygame.mixer.music.load("gif/mp3/test_1.mp3")
    pygame.mixer.music.play(-1,0.0)

    circle = pygame.draw.circle(screen, (50,30,90),(90,30),16,5)

    screen.blit(screen,circle)

