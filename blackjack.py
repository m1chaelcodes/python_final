import random
# Assuming multiple decks in play
cards = ['1','2','3','4','5','6','7','8','9','10','A','J','Q','K']

"""
def letter_card_values(card):
    if card in ['J','Q','K']:
        return 10
"""
print("              Blackjack")
print("-------------------------------------")
card_1 = random.choice(cards)
card_2 = random.choice(cards)
card_vals = []
if card_1 in ['J','Q','K']:
    card_vals.append(10)
if card_2 in ['J','Q','K']:
    card_vals.append(10)
print("Your hand: " + card_1 + ", " + card_2)
if sum(card_vals) == 21:
    print("You win!")
hit_or_stay = input("(H)it or (S)tay? ")
if hit_or_stay.upper() == "H":
    card_3 = random.choice(cards)
    print("Your hand: " + card_1 + ", " + card_2 + ", " + card_3)