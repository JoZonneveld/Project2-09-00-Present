import pygame
from Color import *
from main_screen import *
from Rules import *
from main_game import *
from Settings import *
from Quit import *
pygame.init()

#game buttons
class Button:
    def text_objects(self, text, font):
        textSurface = font.render(text, True, (0, 0, 0))
        return textSurface, textSurface.get_rect()

    def Start(self, screen, x, y, b, h):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + b > mouse[0] > x and y + h > mouse[1] > y:  # hor, vert
            pygame.draw.rect(screen, hover_grey, (x, y, b, h))  # hor, vert, length, height
        else:
            pygame.draw.rect(screen, grey, (x, y, b, h))

        if x + b > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1:
            main_game(screen, button)

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = self.text_objects("Start", smallText)
        textRect.center = ((475 + (50 / 2)), (260 + (50 / 2)))
        screen.blit(textSurf, textRect)

    def Rules(self, screen, x, y, b, h):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + b > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(screen, hover_grey, (x, y, b, h))
        else:
            pygame.draw.rect(screen, grey, (x, y, b, h))

        smallText = pygame.font.Font("freesansbold.ttf", 18)
        textSurf, textRect = self.text_objects("Rules", smallText)
        textRect.center = ((47 + (50 / 2)), (35 + (50 / 2)))
        screen.blit(textSurf, textRect)

        if x + b > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1:
            Rules(screen, BackGround_Rules, button)

    def Setting(self, screen, x, y, b, h):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + b > mouse[0] > x and y + h > mouse[1] > y:  # hor, vert
            pygame.draw.rect(screen, hover_grey, (x, y, b, h))  # hor, vert, length, height
        else:
            pygame.draw.rect(screen, grey, (x, y, b, h))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = self.text_objects("Settings", smallText)
        textRect.center = ((475 + (50 / 2)), (360 + (50 / 2)))
        screen.blit(textSurf, textRect)

        if x + b > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1:
            Settings(screen, button)

    def Exit(self, screen, x, y, b, h):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + b > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(screen, hover_grey, (x, y, b, h))
        else:
            pygame.draw.rect(screen, grey, (x, y, b, h))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = self.text_objects("Exit", smallText)
        textRect.center = ((475 + (50 / 2)), (460 + (50 / 2)))
        screen.blit(textSurf, textRect)

        if x + b > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1:
            Quit()

    def Back(self, screen, x, y, b, h):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + b > mouse[0] > x and y + h > mouse[1] > y:  # hor, vert
            pygame.draw.rect(screen, hover_grey, (x, y, b, h))  # hor, vert, length, height
        else:
            pygame.draw.rect(screen, grey, (x, y, b, h))
        if x + b > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1:
            main_screen(screen, BackGround, button)

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = self.text_objects("Back", smallText)
        textRect.center = ((920 + (50 / 2)), (35 + (50 / 2)))
        screen.blit(textSurf, textRect)

#game width
width = 1024
height = 768
size = (width, height)

screen = pygame.display.set_mode(size)
button = Button()


def process_events():
    pygame.init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


BackGround = Background('gif/water.jpg', [0, 0])
BackGround_Rules = Background('gif/ruls.jpg', [105, 0])


#screens
main_screen(screen, BackGround, button)
main_game(screen, button)
Settings(screen, button)
Rules(screen, BackGround_Rules)
Quit()
