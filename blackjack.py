from random import randint
from collections import namedtuple #used to store the card with no logic but a structure - ('Card', ('rank', 'suit'))


class Card:
    def __init__(self):
        pass

    def card_value(self):
        pass

    card_face = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    card_suit = ['Hearts','Spades','Clubs','Diamonds']


class Deck(Card):
    new_deck = []
    length = len(new_deck)

    for i in Card.card_suit:
        for j in Card.card_face:
            new_deck.append(j + ' of ' + i)

    def new_card(self):
        return (self.new_deck[randint(0,len(self.new_deck)-1)])

    def remove_card(self,card):
        self.new_deck.remove(card)





#def card_deck():
   # card = namedtuple('Card', ('rank', 'suit'))
    
  #  deck = []

  #  for i in card_type:
     #   for j in card_value:
      #    deck.append(j + ' of ' + i)
    #      print(deck)

 #   return deck

