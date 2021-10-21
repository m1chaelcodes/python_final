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
    print("Card value total = " + str(sum(vals)))

# Check if user's cards make blackjack
def check_blackjack(vals):
    if sum(vals) == 21:
        print("Blackjack! You win!")
        return True

# Check if user picked "hit" or "stay", if not, clarify options and prompt again
def check_input(hit_or_stay):
    if hit_or_stay.lower() != "h" and hit_or_stay.lower() != "s":
        while hit_or_stay.lower() != "h" and hit_or_stay.lower() != "s":
            hit_or_stay = input("Options are 'h' for Hit or 's' for Stay\n:")
            if hit_or_stay.lower() == "h" or hit_or_stay.lower() == "s":
                return hit_or_stay
    else:
        return hit_or_stay

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
    print("Dealer's hand: " + dealer_cards[0] + ", *")

    # Show user their current hand and check if hit blackjack
    # If blackjack, ask user to play again
    show_hand("Your", player_cards, player_vals)
    if check_blackjack(player_vals):
        play_again = input("\nPlay again? (y/n)\n:")
        if play_again == "y":
            continue
        else:
            break

    # Prompt user to hit or stay and check input
    hit_or_stay = input("\nHit or Stay? (h/s)\n:")
    hit_or_stay = check_input(hit_or_stay)

    # Each time user hits, provide a new card if card value total is less than 21
    # Game won if 21 reached, game over if player's card total is over 21
    while hit_or_stay.lower() == "h":
        player_cards.append(random.choice(deck))

        letter_card_values(player_cards[-1], player_vals)
    
        show_hand("Your", player_cards, player_vals)

        if check_blackjack(player_vals):
            break
        elif sum(player_vals) > 21:
            print("\nYou bust!\n")
            break
        else:
            hit_or_stay = input("\nHit or Stay? (h/s)\n:")
            hit_or_stay = check_input(hit_or_stay)

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
                print("\nDealer has blackjack! Better luck next time!")       
            elif sum(dealer_vals) > 21:
                print("\nDealer busts! You win!")
            elif sum(dealer_vals) > sum(player_vals):
                print("\nDealer wins!")
            elif sum(dealer_vals) == sum(player_vals):
                print("\nPush! No winner.")
            else:
                print("\nYou win!")
            dealer_hit = False

    # Ask user if they want to play again
    play_again = input("\nPlay again? (y/n)\n:")