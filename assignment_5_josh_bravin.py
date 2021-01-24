"""
This is a program that of a simple game of Blackjack or 21

"""

import random
import sys

player_cards = []
dealer_cards = []

# Dealing initial cards to player and dealer
while len(dealer_cards) < 2:
    dealer_cards.append(random.randint(1, 10))
    if len(dealer_cards) == 2:
        print(f"The dealer has {dealer_cards[1]} and an hidden card")

while len(player_cards) < 2:
    player_cards.append(random.randint(1, 10))
    if len(player_cards) == 2:
        print(f"You have {player_cards[0]} and {player_cards[1]}")

#function to sum the total value of each persons cards
def total(*cards):
    return sum(*cards)

# Asking the player to Hit or stand. Ending the program if they bust.
while total(player_cards) < 21:
    decision_made = str(input("Would you like to Hit or Stand? (h/s)"))
    if decision_made == "h":
        player_cards.append(random.randint(1, 10))
        print(f"Your new total is: {total(player_cards)}")
    else:
        print(f"Your final total is: {total(player_cards)}")
        break

    if total(player_cards) > 21:
        print(f"You have {total(player_cards)} and Bust, Dealer wins! Play again?")
        sys.exit()
    elif total(player_cards) == 21:
        print(f"You have 21!")

#Once the players turn is done, reveal the dealers hidden card, and if they have not already won, hit until they win or bust.

print(f"The dealer reveals their hidden card to show they have a {dealer_cards[0]} and a {dealer_cards[1]}")

while total(dealer_cards) <= 21 and total(dealer_cards) < total(player_cards):
    dealer_cards.append(random.randint(1, 10))
    print(f"The dealer draws another card and their new total is: {total(dealer_cards)}")
    if total(dealer_cards) > 21:
        print(f"The dealer has {total(dealer_cards)} and Busts")


if (total(dealer_cards) >= total(player_cards)) and total(dealer_cards) <= 21:
    print("Dealer Wins! Would you like to play again?")
else:
    print("You Win! Would you like to play again?")
