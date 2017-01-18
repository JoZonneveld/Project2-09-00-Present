from Color import *
from Button import *
import pygame


def process_events():
    pygame.init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


BackGround = Background('gif/water.jpg', [0,0])

def program():
    pygame.init()

    width = 1024
    height = 768

    size = (width, height)

    screen = pygame.display.set_mode(size)
    button = Button()

    while process_events():
        pygame.display.set_caption('Battleport')

        screen.fill(black)
        screen.blit(BackGround.image, BackGround.rect)

        button.Start(screen, 350, 250, 300, 70)
        button.Setting(screen, 350, 350, 300, 70)
        button.Exit(screen, 350, 450, 300, 70)

        pygame.display.flip()
