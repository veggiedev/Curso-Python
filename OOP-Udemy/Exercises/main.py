#Trading cards exercise

import random
import cards
from cards import deck
import colorama

colorama.init()


for item in deck:
    print(f"{item.name} {item.emoji}, Element: {item.element}")

#print(deck)
# def confrontation(element, attack, defense):
#     if Card.element == Card.


new_card = random.choice(deck)

my_deck = []

def new_hand():
    my_deck.append(new_card)

print(f"{new_card.name} {new_card.emoji}, Element: {new_card.element}")




print(cards.dragon.name)