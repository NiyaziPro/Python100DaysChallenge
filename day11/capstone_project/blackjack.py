import random

import blackjack_art

print(blackjack_art.logo)


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

user_cards = []
pc_cards = []

for i in range(2):
    user_cards.append(deal_card())
    pc_cards.append(deal_card())

