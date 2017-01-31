import pygame
from Color import *
from database import *

Turn = "P1"
endturn = True
win = False
game = True
turncount1 = 0
turncount2 = 0
class GameButtons:
    def __init__(self):
        self.showCard = True

    def text_objects(self, text, font):
        textSurface = font.render(text, True, (0, 0, 0))
        return textSurface, textSurface.get_rect()

    def winscreentext(self, screen, test):

        smallText = pygame.font.Font("freesansbold.ttf", 80)
        textSurf, textRect = self.text_objects(test, smallText)
        textRect.center = ((512 + (50 / 2)), (300 + (50 / 2)))
        screen.blit(textSurf, textRect)

    def PlayerTurn(self, screen, x, y, b, h, tekst):
        pygame.draw.rect(screen, white, (x, y, b, h))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = self.text_objects(tekst, smallText)
        textRect.center = ((840 + (50 / 2)), (160 + (50 / 2)))
        screen.blit(textSurf, textRect)


    def EndTurn(self, screen, x, y, b, h):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        global Turn
        global endturn

        if x + b > mouse[0] > x and y + h > mouse[1] > y:  # hor, vert
            pygame.draw.rect(screen, hover_red, (x, y, b, h))  # hor, vert, length, height
        else:
            pygame.draw.rect(screen, red, (x, y, b, h))

        if x + b > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1 and endturn == True:
            # endturn(screen)
            if Turn == "P1":
                global turncount1
                turncount1 += 1
                Furgo_SaltireP1.EndTurn()
                Turn = "P2"
            elif Turn == "P2":
                global turncount2
                turncount2 += 1
                Furgo_SaltireP2.EndTurn()
                Turn = "P1"
            endturn = False
            print("Click")

        if click[0] != 1 and endturn == False:
            print("Release")

            endturn = True


        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = self.text_objects("End turn", smallText)
        textRect.center = ((920 + (50 / 2)), (310 + (50 / 2)))
        screen.blit(textSurf, textRect)

    def DrawCard(self, screen, x, y, b, h):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        imagex = 500
        imagey = 300
        imagew = 125
        imageh = 175

        image = pygame.image.load("gif/card.jpg").convert()

        if x + b > mouse[0] > x and y + h > mouse[1] > y:  # hor, vert
            pygame.draw.rect(screen, hover_green, (x, y, b, h))  # hor, vert, length, height
        else:
            pygame.draw.rect(screen, green, (x, y, b, h))

        if x + b > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1:
            if self.showCard == True:
                self.showCard = False
                print("Click")
            else:
                self.showCard = True
        if imagex + imagew > mouse[0] > imagex and imagey + imageh > mouse[1] > imagey and click[0] == 1:
            self.showCard = True


        if  click[0] != 1 and self.showCard == False:
            screen.blit(image, pygame.Rect((imagex, imagey),(imagew, imageh)))
            print("Released")



        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = self.text_objects("Draw card", smallText)
        textRect.center = ((920 + (50 / 2)), (310 + (50 / 2)))
        screen.blit(textSurf, textRect)

gamebutton = GameButtons()
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

                self.MoveReset = self.Move

            def MoveUp(self):
                self.able = True
                for i in self.PositionList:
                    if i.y == 0:
                        self.able = False
                if self.able == True and self.Move != 0:
                    for i in self.PositionList:
                        i.y -= 1
                    self.Move -= 1

            def MoveDown(self):
                self.able = True
                for i in self.PositionList:
                    if i.y == 20:
                        self.able = False
                if self.able == True and self.Move != 0:
                    for i in self.PositionList:
                        i.y += 1
                    self.Move -= 1

            def EndTurn(self):
                self.Move = self.MoveReset

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
            global listp1
            listp1 = [MerapiP1, AmadeaP1, Silver_whisperP1, Windsurf_Sea_SpiritP1, IntensityP1, Furgo_SaltireP1,
                      Santa_BettinaP1]

            #Player 2 Globals
            global MerapiP2
            global AmadeaP2

            global Silver_whisperP2
            global Windsurf_Sea_SpiritP2
            global IntensityP2

            global Furgo_SaltireP2
            global Santa_BettinaP2

            MerapiP2 = Character("Merapi", RED, 4, 1, [Vector(3, 0), Vector(3, 1), Vector(3, 2), Vector(3, 3)], 4, 4)
            AmadeaP2 = Character("Amadea ", RED, 4, 1, [Vector(5, 0), Vector(5, 1), Vector(5, 2), Vector(5, 3)],
                                 4, 4)

            # Bigger boats
            Silver_whisperP2 = Character("Silver whisper", RED, 3, 2, [Vector(7, 0), Vector(7, 1), Vector(7, 2)], 3, 3)
            Windsurf_Sea_SpiritP2 = Character("Windsurf Sea Spirit", RED, 3, 2, [Vector(9, 0), Vector(9, 1), Vector(9, 2)], 3, 3)
            IntensityP2 = Character("Intensity", RED, 3, 2, [Vector(11, 0), Vector(11, 1), Vector(11, 2)], 3, 3)

            # Big boats
            Furgo_SaltireP2 = Character("Furgo Saltire", RED, 2, 3, [Vector(13, 0), Vector(13, 1)], 2, 2)
            Santa_BettinaP2 = Character("Santa Bettina", RED, 2, 3, [Vector(15, 0), Vector(15, 1)], 2, 2)

            global listp2
            listp2 = [MerapiP2, AmadeaP2, Silver_whisperP2, Windsurf_Sea_SpiritP2, IntensityP2, Furgo_SaltireP2,
                      Santa_BettinaP2]

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
            if Turn == "P1":
                if keys[pygame.K_UP]:
                    Furgo_SaltireP1.MoveUp()
                elif keys[pygame.K_DOWN]:
                    Furgo_SaltireP1.MoveDown()
            elif Turn == "P2":
                if keys[pygame.K_UP]:
                    Furgo_SaltireP2.MoveUp()
                elif keys[pygame.K_DOWN]:
                    Furgo_SaltireP2.MoveDown()


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

            for list in listp1:
                for positionnumber in range(0, len(list.PositionList)):
                    x = list.PositionList[positionnumber].x
                    y = list.PositionList[positionnumber].y
                    color = list.Color
                    pygame.draw.rect(screen, color, [(TileMargin + TileWidth) * x + TileMargin,
                                                     (TileMargin + TileHeight) * y + TileMargin,
                                                     TileWidth,
                                                     TileHeight])

            for list in listp2:
                for positionnumber in range(0, len(list.PositionList)):
                    x = list.PositionList[positionnumber].x
                    y = list.PositionList[positionnumber].y
                    color = list.Color
                    pygame.draw.rect(screen, color, [(TileMargin + TileWidth) * x + TileMargin,
                                                     (TileMargin + TileHeight) * y + TileMargin,
                                                     TileWidth,
                                                     TileHeight])

            clock.tick(30)
            if Turn == "P1":
                tekst = "Player 1's turn" + str(turncount1)
            elif Turn == "P2":
                tekst = "Player 2's turn" + str(turncount2)


            button.Back(screen, 900, 25, 100, 70, "Quit")
            gamebutton.DrawCard(screen, 900, 500, 100, 70)
            gamebutton.EndTurn(screen, 900, 300, 100, 70)
            gamebutton.PlayerTurn(screen, 710, 150, 300, 70, tekst)

            if win == False:
                if game == True:
                    if Turn == "P1":
                        upload_score("P1", turncount1)
                    global game
                    game = False

                screen.fill(GREEN)
                gamebutton.winscreentext(screen,"victory" )
                button.Back(screen, 900, 25, 100, 70, "Back")






            pygame.display.flip()

            Map.update()
        quit()
