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

# Show participant's dealt hand
def show_hand(name, cards, vals):
    print("\n" + name + " hand: " + ", ".join(str(card) for card in cards))
    print("Card value total = " + str(sum(vals)) + "\n")

# Check if cards make blackjack
def check_blackjack(vals):
    if sum(vals) == 21:
        print("You win!")

# Assuming multiple decks of cards in play
deck = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

# Start game
play_again = "y"
while play_again.lower() == "y":
    print("\n-------------------------------------")
    print("              Blackjack")
    print("-------------------------------------\n")

    # Declare player's deck, pick first two cards, and get values
    player_cards = [random.choice(deck)]
    player_cards.append(random.choice(deck))
    player_vals = []
    for card in player_cards:
        letter_card_values(card, player_vals)

    # Declare dealer's deck, pick first two cards, and get values
    dealer_cards = [random.choice(deck)]
    dealer_cards.append(random.choice(deck))
    dealer_vals = []
    for card in dealer_cards:
        letter_card_values(card, dealer_vals)

    # Show one of dealer's cards, obscure the other
    print("Dealer's hand: " + dealer_cards[0] + ", *\n")

    # Show user their current hand and check if hit blackjack
    show_hand("Your", player_cards, player_vals)
    check_blackjack(player_vals)

    # Prompt user to hit or stay
    hit_or_stay = input("Hit or Stay? (h/s)\n:")
    # Check if user picked "hit" or "stay", if not, clarify options and prompt again
    while hit_or_stay.lower() != "h" and hit_or_stay.lower() != "s":
        hit_or_stay = input("Options are 'h' for hit or 's' for Stay\n:")
        if hit_or_stay.lower == "h" or hit_or_stay.lower() == "s":
            break

    # Each time user hits, provide a new card if card value total is less than 21
    # Game won if 21 reached, game over if player's card total is over 21
    while hit_or_stay.lower() == "h":
        player_cards.append(random.choice(deck))

        letter_card_values(player_cards[-1], player_vals)
    
        show_hand("Your", player_cards, player_vals)

        if sum(player_vals) == 21:
            print("Blackjack! You win!")
            play_again = input("Play again? (y/n)\n:")
            break
        elif sum(player_vals) > 21:
            print("You bust!\n")
            play_again = input("Play again? (y/n)\n:")
            break
        else:
            hit_or_stay = input("Hit or Stay? (h/s)\n:")
            while hit_or_stay.lower() != "h" and hit_or_stay.lower() != "s":
                hit_or_stay = input("Options are 'h' for hit or 's' for Stay\n:")
                if hit_or_stay.lower == "h" or hit_or_stay.lower() == "s":
                    break

    # When user stays, dealer takes cards while dealer card total is less than 17
    # Once 17 is hit or exceeded, compare dealer's cards to player's and determine winner
    dealer_hit = True
    if hit_or_stay.lower() == "s":
        while dealer_hit:
            show_hand("Dealer's", dealer_cards, dealer_vals)   
            if sum(dealer_vals) < 17:
                dealer_cards.append(random.choice(deck))
                letter_card_values(dealer_cards[-1], dealer_vals)
                continue
            elif sum(dealer_vals) == 21:
                print("Dealer has blackjack! Better luck next time!")
                play_again = input("Play again? (y/n)\n:")        
            elif sum(dealer_vals) > 21:
                print("Dealer busts! You win!")
                play_again = input("Play again? (y/n)\n:")
            elif sum(dealer_vals) > sum(player_vals):
                print("Dealer wins!")
                play_again = input("Play again? (y/n)\n:")
            elif sum(dealer_vals) == sum(player_vals):
                print("Push! No winner.")
                play_again = input("Play again? (y/n)\n:")
            else:
                print("You win!")
                play_again = input("Play again? (y/n)\n:")
            dealer_hit = False