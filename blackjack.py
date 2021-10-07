import random

# Get numerical value of card string
def letter_card_values(card, player_vals):
    if card in ['J','Q','K']:
        player_vals.append(10)
    elif card == 'A' and 11 not in player_vals and sum(player_vals) < 21:
        player_vals.append(11)
    elif card == 'A':
        player_vals.append(1)
    else:
        player_vals.append(int(card))

# Assuming multiple decks in play
deck = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
player_vals = []
dealer_vals = []

# Start game
print("\n-------------------------------------")
print("              Blackjack")
print("-------------------------------------\n")
game = True

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
print("Dealer's hand: " + dealer[0] + ", *")

# Show user their current hand
print("Your hand: " + ", ".join(str(card) for card in cards))
print("Card value total = " + str(sum(player_vals)) + "\n")
if sum(player_vals) == 21:
    print("You win!")

hit_or_stay = input("(H)it or (S)tay? ")

while game == True:
    if hit_or_stay.upper() == "H":
        cards.append(random.choice(deck))

        print("Your hand: " + ", ".join(str(card) for card in cards))
        
        letter_card_values(cards[-1], player_vals)

        print("Card value total = " + str(sum(player_vals)))

        if sum(player_vals) == 21:
            print("You win!")
            break
        elif sum(player_vals) > 21:
            print("You bust!")
            break
        else:
            hit_or_stay = input("(H)it or (S)tay? ")
    else:
        while sum(dealer_vals) < 17:
            print("Dealer's hand: " + ", ".join(str(card) for card in dealer))
            dealer.append(random.choice(deck))
            letter_card_values(dealer[-1], dealer_vals)
        # infinite loop right now
        print("Dealer card value total: " + str(sum(dealer_vals))) 