import pygame


BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)


width  = 20
height = 20


margin = 5

grid = []
for row in range(10):

    grid.append([])
    for column in range(10):
        grid[row].append(0)

pygame.init()


size = [255, 255]
screen = pygame.display.set_mode(size)



done = False


clock = pygame.time.Clock()

#Main Program Loop
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:

            pos = pygame.mouse.get_pos()

            column = pos[0] // (width + margin)
            row = pos[1] // (height + margin)

            grid[row][column] = 1
            grid[row+1][column+1] = 1
            grid[row-1][column-1] = 1
            grid[row-1][column] = 1
            grid[row+1][column] = 1
            grid[row][column+1] = 1
            grid[row][column-1] = 1
            grid[row-1][column+1] = 1
            grid[row+1][column-1] = 1

            print("Click ", pos, "Grid coordinates: ", row, column)

    # Set the screen background
    screen.fill(BLACK)


    for row in range(10):
       for column in range(10):
            color = WHITE
            if grid[row][column] == 1:
                color = RED
            pygame.draw.rect(screen,
                             color,
                             [(margin+width)*column+margin,
                              (margin+height)*row+margin,
                              width,
                              height])


    clock.tick(90)



    pygame.display.flip()

pygame.quit()