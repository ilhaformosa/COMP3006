#%% Game description
# This script running a single round of card game: Black Jack. Participants includes: a dealer and a player.
# Each round, both participant draw one card from the deck.
# A participant who gets total card value equal to 21 wins,
# and game continue unless any player reach or pass 21 in total card value.
# Total 52 cards in this game, four suits: Clubs, Diamonds, Hearts, Spades,
# and 13 faces of cards ranging from 1 to 10. Card 'J', 'Q', 'K' are  card "Ace(A)" valued at 1 or 11 at the player's decision.

import random

#%% this class to set up cards used in the game, including cards' suits and values,  total 52 (13x4) cards
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return self.value + " , " + self.suit

class Deck:
    def __init__(self):
        self.cards = [Card(suits, values) for suits in ["Clubs", "Diamonds", "Hearts", "Spades"] for values in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]]

    def shuffle(self): # shuffled cards for the game
        if len(self.cards) >= 2:
            random.shuffle(self.cards) # shuffle the shallow copy of self.cards

    def draw(self): # draw a card from the card pool
        if len(self.cards) >= 2:
            return self.cards.pop()

#%% this class to keep track of cards at hand
class Hand:
    def __init__(self, dealer = False):
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def add_card(self, card):
        self.cards.append(card)

    def calculate_value(self):
        self.value = 0
        card_ace = False

        for card in self.cards: # alias used for value calculation
            if card.value.isnumeric(): # add numerical value of cards
                self.value += int(card.value)
            elif card.value == "A": # add 11 to total value when have an 'ace'
                card_ace = True
                self.value += 11
            else: # add 10 to total value when have 'J', 'Q', 'K'
                self.value += 10
        if card_ace and self.value > 21: # set 'ace' value to 1 when total value exceed 21
            self.value -= 10

    def show_card(self):
        if self.dealer:
            print(self.cards[1])
        else:
            for card in self.cards:
                print(card)
            print("Value:", self.calculate_value())

#%% function to use in game operation
def check_blackjack():
    player = False
    dealer = False
    if player_hand.calculate_value() == 21:
        player = True
    if dealer_hand.calculate_value() == 21:
        dealer = True

    return player, dealer

#%% game operation begins here
playing = True
while playing:
    card = Deck() # deep copy
    card.shuffle() # shuffle cards
    player_hand = Hand() # deep copy
    dealer_hand = Hand(dealer=True) # deep copy

    for i in range(2): # start the game, and draw two cards for both players
        player_hand.add_card(card.draw())
        dealer_hand.add_card(card.draw())

    print("Your cards:")
    player_hand.show_card()
    print("Dealer's cards:")
    dealer_hand.show_card()

    game_over = False

    while not game_over:
        player_blackjack, dealer_blackjack = check_blackjack()

        player_hand_value = player_hand.calculate_value()
        dealer_hand_value = dealer_hand.calculate_value()

        if player_blackjack and dealer_blackjack:
            print("Both players have blackjack")
            game_over = True
            continue
        elif player_blackjack:
            print("You have blackjack")
            game_over = True
            continue
        elif dealer_blackjack:
            print("Dealer has blackjack")
            game_over = True
            continue

        next = input("Please choose hit or stick [ h / s ] ")

        if next == "h": # choose hit to get another card
            player_hand.add_card(card.draw())
            player_hand.show_card()
            if player_hand_value > 21:
                print("Card value exceed 21, you lose the game")
                game_over = True
        elif next == "s": # show hands and get the result
            print("Your hand:", player_hand_value)
            print("Dealer's hand:", dealer_hand_value)

            if player_hand_value > dealer_hand_value:
                print("You win the game")
            elif player_hand_value == dealer_hand_value:
                print("Tie")
            else:
                print("Dealer wins the game")
            game_over = True

    play_again = input("Play Again? [y/n] ") # ask user if want to play another around
    if play_again == "n":
        print("End of Game.")
        playing = False
    else:
        game_over = False
