import random

# Get numerical value of card string
def letter_card_values(card):
    if card in ['J','Q','K']:
        card_vals.append(10)
    elif card == 'A' and 11 not in card_vals:
        card_vals.append(11)
    elif card == 'A':
        card_vals.append(1)
    else:
        card_vals.append(int(card))

# Assuming multiple decks in play
deck = ['1','2','3','4','5','6','7','8','9','10','A','J','Q','K']
card_vals = []

# Start game
print("              Blackjack")
print("-------------------------------------")

# Pick first two cards
cards = [random.choice(deck)]
cards.append(random.choice(deck))

print(cards)

letter_card_values(cards[0])
letter_card_values(cards[1])

print(card_vals)

# Show user their hand
print("Your hand: " + cards[0] + ", " + cards[1])
print("Card value total = " + str(sum(card_vals)))
if sum(card_vals) == 21:
    print("You win!")

hit_or_stay = input("(H)it or (S)tay? ")

while hit_or_stay.upper() == "H":
    cards.append(random.choice(deck))
    print("Your hand: " + cards[0] + ", " + cards[1] + ", " + cards[2])
    if cards[2] in ['J', 'Q', 'K']:
        card_vals.append(10)
    else:
        card_vals.append(int(cards[2]))

    if sum(card_vals) == 21:
        print("You win!")
    elif sum(card_vals) > 21:
        print("You bust!")
        break
    else:
        hit_or_stay = input("(H)it or (S)tay? ")