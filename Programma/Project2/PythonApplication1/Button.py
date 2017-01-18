import pygame
from Color import *
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
            print("click")

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = self.text_objects("Start", smallText)
        textRect.center = ((475 + (50 / 2)), (260 + (50 / 2)))
        screen.blit(textSurf, textRect)

    def Setting(self, screen, x, y, b, h):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + b > mouse[0] > x and y + h > mouse[1] > y:  # hor, vert
            pygame.draw.rect(screen, hover_grey, (x, y, b, h))  # hor, vert, length, height
        else:
            pygame.draw.rect(screen, grey, (x, y, b, h))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = self.text_objects("Setting", smallText)
        textRect.center = ((475 + (50 / 2)), (360 + (50 / 2)))
        screen.blit(textSurf, textRect)

        if click[0] == 1:
            pass

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

        if click[0] == 1:
            pygame.quit()
