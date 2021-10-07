import random

# Get numerical value of card string
def letter_card_values(card, vals):
    if card in ['J','Q','K']:
        vals.append(10)
    elif card == 'A' and 11 not in vals and sum(vals) < 21:
        vals.append(11)
    elif card == 'A':
        vals.append(1)
    else:
        vals.append(int(card))

# Show dealt hand
def show_hand(cards, vals):
    print("Your hand: " + ", ".join(str(card) for card in cards))
    print("Card value total = " + str(sum(vals)) + "\n")

# Assuming multiple decks in play
deck = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
player_vals = []
dealer_vals = []

# Start game
print("\n-------------------------------------")
print("              Blackjack")
print("-------------------------------------\n")

# Pick player's first two cards and get values
cards = [random.choice(deck)]
cards.append(random.choice(deck))

letter_card_values(cards[0], player_vals)
letter_card_values(cards[1], player_vals)

# Pick dealer's first two cards and get values
dealer = [random.choice(deck)]
dealer.append(random.choice(deck))

letter_card_values(dealer[0], dealer_vals)
letter_card_values(dealer[1], dealer_vals)

# Show one of dealer's cards
print("Dealer's hand: " + dealer[0] + ", *\n")

# Show user their current hand and check if hit blackjack
show_hand(cards, player_vals)
if sum(player_vals) == 21:
    print("You win!")

hit_or_stay = input("(H)it or (S)tay? ")

while hit_or_stay.upper() == "H":
    cards.append(random.choice(deck))

    letter_card_values(cards[-1], player_vals)

    show_hand(cards, player_vals)

    if sum(player_vals) == 21:
        print("You win!")
        break
    elif sum(player_vals) > 21:
        print("You bust!")
        break
    else:
        hit_or_stay = input("(H)it or (S)tay? ")
        
while sum(dealer_vals) < 17:
    print("Dealer's hand: " + ", ".join(str(card) for card in dealer))
    dealer.append(random.choice(deck))
    letter_card_values(dealer[-1], dealer_vals)
    # infinite loop right now
    print("Dealer card value total: " + str(sum(dealer_vals))) 