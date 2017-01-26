import pygame
from Color import *
from database import *
def process_events():
    pygame.init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def main_game(screen, button, BackGround_Game):
    while process_events():
        pygame.display.set_caption('Battleport')
        pygame.init()
        clock = pygame.time.Clock()
        Done = False
        global MapSize
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
            def __init__(self, Name, color, HP, move, list, HRange, VRange):
                self.Name = Name
                self.Color = color
                self.HP = HP
                self.Move = move
                self.PositionList = list
                self.HRange = HRange
                self.VRange = VRange

            def MoveUp(self):
                for i in self.PositionList:
                    i.y -= 1

            def MoveDown(self):
                for i in self.PositionList:
                    i.y += 1

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
                    if self.Column < MapSize - 1:
                        if self.CollisionCheck("RIGHT") == False:
                            self.Column += 1

                elif Direction == "DOWN":
                    if self.Row < MapSize - 1:
                        if self.CollisionCheck("DOWN") == False:
                            self.Row += 1

                Map.update()

            def CollisionCheck(self, Direction):
                if Direction == "UP":
                    if len(Map.Grid[self.Column][(self.Row) - 1]) > 1:
                        return True
                elif Direction == "LEFT":
                    if len(Map.Grid[self.Column - 1][(self.Row)]) > 1:
                        return True
                elif Direction == "RIGHT":
                    if len(Map.Grid[self.Column + 1][(self.Row)]) > 1:
                        return True
                elif Direction == "DOWN":
                    if len(Map.Grid[self.Column][(self.Row) + 1]) > 1:
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

            #Player 1 globals

            global MerapiP1
            global AmadeaP1

            global Silver_whisperP1
            global Windsurf_Sea_SpiritP1
            global IntensityP1

            global Furgo_SaltireP1
            global Santa_BettinaP1

            # PLAYER 1

            # Biggest boats
            MerapiP1 = Character("Merapi", GREEN, 4, 1, [Vector(3, 20), Vector(3, 19), Vector(3, 18), Vector(3, 17)], 4, 4)
            AmadeaP1 = Character("Amadea ", GREEN, 4, 1, [Vector(5, 20), Vector(5, 19), Vector(5, 18), Vector(5, 17)], 4, 4)

            # Bigger boats
            Silver_whisperP1 = Character("Silver whisper", GREEN, 3, 2, [Vector(7, 20), Vector(7, 19), Vector(7, 18)], 3, 3)
            Windsurf_Sea_SpiritP1 = Character("Windsurf Sea Spirit", GREEN, 3, 2, [Vector(9, 20), Vector(9, 19), Vector(9, 18)], 3, 3)
            IntensityP1 = Character("Intensity", GREEN, 3, 2, [Vector(11, 20), Vector(11, 19), Vector(11, 18)], 3, 3)

            # Big boats
            Furgo_SaltireP1 = Character("Furgo Saltire", GREEN, 2, 3, [Vector(13, 20), Vector(13, 19)], 2, 2)
            Santa_BettinaP1 = Character("Santa Bettina", GREEN, 2, 3, [Vector(15, 20), Vector(15, 19)], 2, 2)


            #Player 2 Globals
            global MerapiP2
            global AmadeaP2

            global Silver_whisperP2
            global Windsurf_Sea_SpiritP2
            global IntensityP2

            global Furgo_SaltireP2
            global Santa_BettinaP2

            MerapiP2 = Character("Merapi", GREEN, 4, 1, [Vector(3, 10), Vector(3, 9), Vector(3, 8), Vector(3, 7)], 4, 4)
            AmadeaP2 = Character("Amadea ", GREEN, 4, 1, [Vector(5, 20), Vector(5, 19), Vector(5, 18), Vector(5, 17)],
                                 4, 4)

            # Bigger boats
            Silver_whisperP2 = Character("Silver whisper", GREEN, 3, 2, [Vector(7, 20), Vector(7, 19), Vector(7, 18)], 3, 3)
            Windsurf_Sea_SpiritP2 = Character("Windsurf Sea Spirit", GREEN, 3, 2, [Vector(9, 20), Vector(9, 19), Vector(9, 18)], 3, 3)
            IntensityP2 = Character("Intensity", GREEN, 3, 2, [Vector(11, 20), Vector(11, 19), Vector(11, 18)], 3, 3)

            # Big boats
            Furgo_SaltireP2 = Character("Furgo Saltire", GREEN, 2, 3, [Vector(13, 20), Vector(13, 19)], 2, 2)
            Santa_BettinaP2 = Character("Santa Bettina", GREEN, 2, 3, [Vector(15, 20), Vector(15, 19)], 2, 2)

            def update(self):
                for Column in range(MapSize):
                    for Row in range(MapSize):
                        for i in range(len(Map.Grid[Column][Row])):
                            if Map.Grid[Column][Row][i].Column != Column:
                                Map.Grid[Column][Row].remove(Map.Grid[Column][Row][i])
                            elif Map.Grid[Column][Row][i].Name == "Boat":
                                Map.Grid[Column][Row].remove(Map.Grid[Column][Row][i])
                                # Map.Grid[int(Map.Boat.Column)][int(Map.Boat.Row)].append(Map.Boat)

        Map = Map()

        while not Done:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP]:
                MerapiP1.MoveUp()
                print("up")
            elif keys[pygame.K_DOWN]:
                MerapiP1.MoveDown()
                print("down")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Done = True
            screen.fill(BLACK)

            for Row in range(MapSize):
                for Column in range(MapSize):
                    for i in range(0, len(Map.Grid[Column][Row])):
                        Color = BLUE
                        # if Map.Grid[Column][Row][i].Name == "Boat":
                        #    Color = GREEN

                    pygame.draw.rect(screen, Color, [(TileMargin + TileWidth) * Column + TileMargin,
                                                     (TileMargin + TileHeight) * Row + TileMargin,
                                                     TileWidth,
                                                     TileHeight])

            for positionnumber in range(0, len(MerapiP1.PositionList)):  # determines length of boat
                x = MerapiP1.PositionList[positionnumber].x
                y = MerapiP1.PositionList[positionnumber].y
                color = MerapiP1.Color
                pygame.draw.rect(screen, color, [(TileMargin + TileWidth) * x + TileMargin,
                                                 (TileMargin + TileHeight) * y + TileMargin,
                                                 TileWidth,
                                                 TileHeight])

            clock.tick(30)
            button.Back(screen, 900, 25, 100, 70, "Quit")
            pygame.display.flip()

            Map.update()
        quit()