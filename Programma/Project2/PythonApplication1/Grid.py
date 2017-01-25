import random as random
import pygame as pygame

pygame.init()
clock = pygame.time.Clock()
Screen = pygame.display.set_mode([1024, 768])
Done = False
MapSize = 20

TileWidth = 43
TileHeight = 32
TileMargin = 1

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)



class MapTile(object):
    def __init__(self, Name, Column, Row):
        self.Name = Name
        self.Column = Column
        self.Row = Row


class Character(object):
    def __init__(self, Name, HP, Column, Row):
        self.Name = Name
        self.HP = HP
        self.Column = Column
        self.Row = Row

    def Move(self, Direction):

        if Direction == "UP":
            if self.Row > 0:
                if self.CollisionCheck("UP") == False:
                   self.Row -= 1

        elif Direction == "LEFT":
            if self.Column > 0:
                if self.CollisionCheck("LEFT") == False:
                    self.Column -= 1

        elif Direction == "RIGHT":
            if self.Column < MapSize-1:
                if self.CollisionCheck("RIGHT") == False:
                         self.Column += 1

        elif Direction == "DOWN":
            if self.Row < MapSize-1:
                if self.CollisionCheck("DOWN") == False:
                    self.Row += 1

        Map.update()

    def CollisionCheck(self, Direction):
        if Direction == "UP":
            if len(Map.Grid[self.Column][(self.Row)-1]) > 1:
                return True
        elif Direction == "LEFT":
            if len(Map.Grid[self.Column-1][(self.Row)]) > 1:
                return True
        elif Direction == "RIGHT":
            if len(Map.Grid[self.Column+1][(self.Row)]) > 1:
                return True
        elif Direction == "DOWN":
            if len(Map.Grid[self.Column][(self.Row)+1]) > 1:
                return True
        return False

    def Location(self):
        print("Coordinates: " + str(self.Column) + ", " + str(self.Row))


class Map(object):
    global MapSize

    Grid = []

    for Row in range(MapSize):
        Grid.append([])
        for Column in range(MapSize):
            Grid[Row].append([])

    for Row in range(MapSize):
        for Column in range(MapSize):
            TempTile = MapTile("WaterTile", Column, Row)
            Grid[Column][Row].append(TempTile)

    RandomRow = random.randint(0, MapSize - 1)
    RandomColumn = random.randint(0, MapSize - 1)
    Hero = Character("Hero", 10, RandomColumn, RandomRow)

    def update(self):

        for Column in range(MapSize):
            for Row in range(MapSize):
                for i in range(len(Map.Grid[Column][Row])):
                    if Map.Grid[Column][Row][i].Column != Column:
                        Map.Grid[Column][Row].remove(Map.Grid[Column][Row][i])
                    elif Map.Grid[Column][Row][i].Name == "Hero":
                        Map.Grid[Column][Row].remove(Map.Grid[Column][Row][i])
        Map.Grid[int(Map.Hero.Column)][int(Map.Hero.Row)].append(Map.Hero)

Map = Map()

while not Done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Done = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            Pos = pygame.mouse.get_pos()
            Column = Pos[0] // (TileWidth + TileMargin)
            Row = Pos[1] // (TileHeight + TileMargin)
            print(str(Row) + ", " + str(Column))

            for i in range(len(Map.Grid[Column][Row])):
                print(str(Map.Grid[Column][Row][i].Name))

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Map.Hero.Move("LEFT")
            if event.key == pygame.K_RIGHT:
                Map.Hero.Move("RIGHT")
            if event.key == pygame.K_UP:
                Map.Hero.Move("UP")
            if event.key == pygame.K_DOWN:
                Map.Hero.Move("DOWN")

    Screen.fill(BLACK)

    for Row in range(MapSize):           # Drawing grid
        for Column in range(MapSize):
            for i in range(0, len(Map.Grid[Column][Row])):
                Color = WHITE
                if len(Map.Grid[Column][Row]) == 2:
                    Color = RED
                if Map.Grid[Column][Row][i].Name == "Hero":
                    Color = GREEN


            pygame.draw.rect(Screen, Color, [(TileMargin + TileWidth) * Column + TileMargin,
                                             (TileMargin + TileHeight) * Row + TileMargin,
                                             TileWidth,
                                             TileHeight])

    clock.tick(30)

    pygame.display.flip()
    Map.update()

pygame.quit()
