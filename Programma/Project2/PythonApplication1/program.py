from Color import *
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

class quit_button():
    def text_objects(self, text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    def draw_button(self, screen, x, y, b, h):

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

class start_button():
    def text_objects(self, text, font):
        textSurface = font.render(text, True, (0, 0, 0))
        return textSurface, textSurface.get_rect()

    def draw_button(self, screen, x, y, b, h):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + b > mouse[0] > x and y + h > mouse[1] > y:  # hor, vert
            pygame.draw.rect(screen, hover_grey, (x, y, b, h))  # hor, vert, length, height
        else:
            pygame.draw.rect(screen, grey, (x, y, b, h))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = self.text_objects("Start", smallText)
        textRect.center = ((475 + (50 / 2)), (335 + (50 / 2)))
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


    start = start_button()

    while process_events():
        screen.fill(black)
        screen.blit(BackGround.image, BackGround.rect)

        start.draw_button(screen, 350, 325, 300, 70)
        quit.draw_button(screen, 350, 450, 300, 70)


        pygame.display.flip()