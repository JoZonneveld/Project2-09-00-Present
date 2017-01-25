import pygame
from database import *
from random import randint


class Cards:
    def __init__(self, type, name, amount):
        self.Type = type
        self.Name = name
        self.Amount = amount
        self.cardAmount = 100

    def pick_card(self):
        random = randint(0, self.cardAmount)
        card = self.cards[random]
        return card

    def draw_card(self):
        self.Amount -= 1
    # def update_card(self):
        # self.cardCount =-1



# Offensieve kaarten
FMJ_upgrade = Cards("Offensieve", "FMJ upgrade", 2)
Rifling = Cards("Offensieve", "Rifling", 2)
Advanced_Rifling = Cards("Offensieve", "Advanced Rifling", 2)
Naval_Mine = Cards("Offensieve", "Naval Mine", 6)
EMP_upgrade = Cards("Offensieve", "EMP upgrade", 4)

# Defensieve kaarten
Reinforced_Hull = Cards("Defensieve", "Reinforced Hull", 2)
Sonar = Cards("Defensieve", "Sonar", 4)
Smokescreen = Cards("Defensieve", "Smokescreen", 2)
Sabotage = Cards("Defensieve", "Sabotage", 2)

# Hulp kaarten
Backup = Cards("Hulp", "Backup", 2)
Extra_Fuel_II = Cards("Hulp", "Extra Fuel II", 4)
Extra_Fuel = Cards("Hulp", "Extra Fuel", 6)
Rally = Cards("Hulp", "Rally", 1)
Adrenaline_rush = Cards("Hulp", "Adrenaline rush", 4)

#Special kaarten
Repair = Cards("Special", "Repair", 2)
Flak_armor = Cards("Special", "Flak armor", 2)
Hack_Intel = Cards("Special", "Hack Intel", 1)
Far_sight = Cards("Special", "Far sight", 1)
Aluminum_hull = Cards("Special", "Aluminum hull", 1)
Jack_Sparrow = Cards("Special", "Jack Sparrow", 1)


