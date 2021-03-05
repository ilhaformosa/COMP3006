# Dice Rolling Game
# user input the number of dices to roll and the number of sides on dice
# roll dices in two cups, one for our user and one for the dealer
# player with greater total points win and get all bets on table

# Author: Hangyu Chen

import random

# all aspects of dices are defined here
class Dice:
    def __init__(self, edge):
        self.edge = edge
        self.score = random.randint(1, self.edge)

    # roll the dice defined
    def roll(self):
        self.score = random.randint(1, self.edge)

    def __str__(self):
        return self.score

    # add magic method
    def __add__(self, other):
        return self.score + other.score

    # six comparison magic methods
    def __eq__(self, other):  # equal
        if self.score == other.score:
            return True
        else:
            return False

    def __ne__(self, other):  # not equal
        if self.score != other.score:
            return True
        else:
            return False

    def __gt__(self, other):  # greater than
        if self.score > other.score:
            return True
        else:
            return False

    def __lt__(self, other):  # less than
        if self.score < other.score:
            return True
        else:
            return False

    def __ge__(self, other):  # greater than or equal to
        if self.score >= other.score:
            return True
        else:
            return False

    def __le__(self, other):  # less than or equal to
        if self.score <= other.score:
            return True
        else:
            return False


# cup of dice defined to keep track
class CupOfDice:
    def __init__(self, dice_num, dice_edge):
        self.score = 0
        self.dice_list = []
        # dice numbers calculated
        for i in range(dice_num):
            dice = Dice(dice_edge)
            self.dice_list.append(dice)
            self.score += dice.score

    def __str__(self):
        return self.score

    # add method
    def __add__(self, other):
        return self.score + other.score

    # all six comparison magic methods
    def __eq__(self, other):  # equal
        if self.score == other.score:
            return True
        else:
            return False

    def __ne__(self, other):  # not equal
        if self.score != other.score:
            return True
        else:
            return False

    def __gt__(self, other):  # greater than
        if self.score > other.score:
            return True
        else:
            return False

    def __lt__(self, other):  # less than
        if self.score < other.score:
            return True
        else:
            return False

    def __ge__(self, other):  # greater than or equal to
        if self.score >= other.score:
            return True
        else:
            return False

    def __le__(self, other):  # less than or equal to
        if self.score <= other.score:
            return True
        else:
            return False

    # rolling function for gameplay
    def roll(self):
        self.score = 0
        for dice in self.dice_list:
            dice.roll()
            self.score += dice.score


if __name__ == '__main__':
    account = 10000
    # ask player for input to engage the game
    while True:
        print("Welcome to dice rolling")
        input_str = input(" Input the number of dice and the number of sides on the dice, split with space(eg:2 4): ")
        input_arr = input_str.split(" ")
        if len(input_arr) != 2:  # check if input is correct for game play
            print("Form of input incorrect")
            print("Input the number of dices and the number of sides on the dice, split with space(eg:2 4): ")
            continue
        break

    # set up two cups for rolling dices
    cup1 = CupOfDice(int(input_arr[0]), int(input_arr[1]))
    cup2 = CupOfDice(int(input_arr[0]), int(input_arr[1]))

    # cup rolling here, and account balance update here
    while True:
        print("account balance:", account)
        input_str = input("Place your bet:")
        amount = int(input_str)
        print("Dice Rolling...")

        # roll dices in two cups
        cup1.roll()
        cup2.roll()
        print(cup1.score, ":", cup2.score)

        # total points comparison and update account balance
        if cup1 == cup2:
            print("In the draw")
        elif cup1 > cup2:
            print("You win")
            account += amount
        else:
            print("You lose")
            account -= amount

        # check account balance and insolvency
        if account <= 0:
            print("Insolvency, game stopped.")
            break
        again = input("Play again ? Yes or No (Y/N): ")

        # an option to cash out
        if again == "y" or "Y":
            print("Cash out amount:", account)
            break
