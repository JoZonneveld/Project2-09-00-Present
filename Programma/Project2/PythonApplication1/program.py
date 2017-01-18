from Color import *
import pygame


def process_events():
    pygame.init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


class quit_button():
    def text_objects(self, text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    def draw_button(self, screen):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 350 + 300 > mouse[0] > 350 and 350 + 70 > mouse[1] > 350:
            pygame.draw.rect(screen, hover_red, (350, 350, 300, 70))

        else:
            pygame.draw.rect(screen, red, (350, 350, 300, 70))

        smallText = pygame.font.Font("freesansbold.ttf", 14)
        textSurf, textRect = self.text_objects("Exit", smallText)
        textRect.center = ((150 + (100 / 2)), (450 + (50 / 2)))
        screen.blit(textSurf, textRect)

        if click[0] == 1:
            pygame.quit()


class start_button():
    def text_objects(self, text, font):
        textSurface = font.render(text, True, (0, 0, 0))
        return textSurface, textSurface.get_rect()

    def draw_button(self, screen):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 350 + 300 > mouse[0] > 350 and 350 + 70 > mouse[1] > 350:  # hor, vert
            pygame.draw.rect(screen, hover_grey, (350, 350, 300, 70))  # hor, vert, length, height

        else:
            pygame.draw.rect(screen, grey, (350, 350, 300, 70))

        smallText = pygame.font.Font("freesansbold.ttf", 14)
        textSurf, textRect = self.text_objects("Start", smallText)
        textRect.center = ((475 + (50 / 2)), (360 + (50 / 2)))
        screen.blit(textSurf, textRect)

        if click[0] == 1:
            pass


def program():
    pygame.init()

    width = 1024
    height = 768

    size = (width, height)

    screen = pygame.display.set_mode(size)

    quit = quit_button()

    start = start_button()

    while process_events():
        screen.fill(Deep_Sky_Blue)

        quit.draw_button(screen)
        start.draw_button(screen)

        pygame.display.flip()