import pygame
from database import *
from random import randint

class Cards:
    def __init__(self):
        self.cards = download_cards()
        self.cardCount = 3
        self.cardAmount = 100

    def pick_card(self):
        random = randint(0, self.cardAmount)
        card = self.cards[random]
        return card

    #def update_card(self):
        #self.cardCount =-1

    #def draw_card(self):

