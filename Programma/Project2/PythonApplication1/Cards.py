import pygame
from database import *
from random import randint, random


class Cards:
    def __init__(self):
        self.cards = download_cards()
        self.cardCount = 3
        self.cardAmount = 100

    def pick_card(self):
        random = randint(0, self.cardAmount)
        card = self.cards[random]
        return card

class Empty:
   def __init__ (self):
       self.IsEmpty = True

class Node:
    def __init__(self, type, name, amount, tail):
        self.IsEmpty =False
        self.Type = type
        self.Name = name
        self.Amount = amount
        self.Tail = tail

list = Empty()

for rows in NormalCards():
    list = Node(rows[3], rows[2], rows[4],list)

foo = ['a', 'b', 'c', 'd', 'e']
print(random.choice(foo))




    #def update_card(self):
        #self.cardCount =-1

    #def draw_card(self):

