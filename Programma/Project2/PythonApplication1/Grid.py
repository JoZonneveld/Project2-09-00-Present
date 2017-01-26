import random as random
import pygame
def grid():
    pygame.init()
    clock = pygame.time.Clock()
    Screen = pygame.display.set_mode([1024, 768])
    Done = False
    MapSize = 21

    TileWidth = 32
    TileHeight = 32
    TileMargin = 1

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (50, 50, 200)

    class Vector:
        def __init__(self, x, y):
            self.x = x
            self.y = y


    class MapTile(object):
        def __init__(self, Name, Column, Row):
            self.Name = Name
            self.Column = Column
            self.Row = Row


    class Character(object):
        def __init__(self, Name, color, HP, move, list):
            self.Name = Name
            self.Color = color
            self.HP = HP
            self.Move = move
            self.PositionList = list

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
        global objectslistp1
        objectslistp1 = [Character("Merapi", GREEN, 4, 1, [Vector(5,20), Vector(5, 19), Vector(5, 18), Vector(5, 17)]),
                         Character("Silver whisper", GREEN, 3, 2, [Vector(7,20),Vector(7,19),Vector(7,18)]),
                         Character("Furgo Saltire ", GREEN, 2, 3, [Vector(9,20), Vector(9,19)])]


        def update(self):
            for Column in range(MapSize):
                for Row in range(MapSize):
                    for i in range(len(Map.Grid[Column][Row])):
                        if Map.Grid[Column][Row][i].Column != Column:
                            Map.Grid[Column][Row].remove(Map.Grid[Column][Row][i])
                        elif Map.Grid[Column][Row][i].Name == "Boat":
                            Map.Grid[Column][Row].remove(Map.Grid[Column][Row][i])
            #Map.Grid[int(Map.Boat.Column)][int(Map.Boat.Row)].append(Map.Boat)

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
                    Map.Boat.Move("LEFT")
                if event.key == pygame.K_RIGHT:
                    Map.Boat.Move("RIGHT")
                if event.key == pygame.K_UP:
                    Map.Boat.Move("UP")
                if event.key == pygame.K_DOWN:
                    Map.Boat.Move("DOWN")

        Screen.fill(BLACK)

        for Row in range(MapSize):
            for Column in range(MapSize):
                for i in range(0, len(Map.Grid[Column][Row])):
                    Color = BLUE
                    #if Map.Grid[Column][Row][i].Name == "Boat":
                    #    Color = GREEN


                pygame.draw.rect(Screen, Color, [(TileMargin + TileWidth) * Column + TileMargin,
                                                 (TileMargin + TileHeight) * Row + TileMargin,
                                                 TileWidth,
                                                 TileHeight])

        for objectje in objectslistp1:
            for positionnumber in range(0, len(objectje.PositionList)): #determines length of boat
                x = objectje.PositionList[positionnumber].x
                y = objectje.PositionList[positionnumber].y
                color = objectje.Color
                pygame.draw.rect(Screen, color, [(TileMargin + TileWidth) * x + TileMargin,
                                             (TileMargin + TileHeight) * y + TileMargin,
                                             TileWidth,
                                             TileHeight])

        clock.tick(30)

        pygame.display.flip()
        Map.update()

    pygame.quit()