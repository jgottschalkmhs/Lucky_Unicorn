# functions go here
import random


#number checking function goes here
def intcheck(question, low, high):
    valid = False
    error = "please enter an intgeer between {} and {}".format(low, high)
    while not valid:
        try:
            response = int(input(question))
            if low <= response <= high:
                return response
            else:
                print(error)
                print()
        except ValueError:
            print(error)


# function to print out token statements. Takes in message and then applies decoration to top
# and bottom of message based on a specific character
# Function to easily generate winning statement...

def token_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print

# Main routine

COST = 1   #cost per round
UNICORN = 5    # unicorn wins $5
ZEB_HOR = 0.5   # Zebra / horse wins 50c
DONKEY = 0     # donkey does not win anything

# Start of Main Routine

# set up list of tokens, adjust amount of donkeys etc so that house has advantage
tokens = ["horse", "horse", "horse",
          "zebra", "zebra", "zebra",
          "donkey", "donkey", "donkey", "unicorn"]
# Ask how much they want to play with

print("RULES:  *Enter how much you want to play with")
print(        "*Press enter to continue and press any letter to quit")
print(        "*Dont spend all your money at once 🤑"    )
print()
total = intcheck("How much would you like to play with? ", 0, 10)

keep_going = ""
while keep_going == "":

    # randomly choose a token from our list above
    chosen = random.choice(tokens)
    print()
    # print("You got a {}".format(chosen))

    # Adjust total correctly for a given token
    if chosen == "unicorn":
        total += 5                  #wins $5
        decoration = "⭐"
        feedback = "Congrats you got a unicorn and won $5.00"
    elif chosen == "donkey":
        total -= 1                      # does not win anything
        decoration = "-"
        feedback = "sorry, you got a donkey and did not win anything this round"
    else:
        total -= 0.5                    #wins 50c, paid $1 so loses 50c
        feedback = "Congrats you got a {} and won 50c".format(chosen)
        decoration = "^"

    print()
    token_statement(feedback, decoration)

    print("You have {:.2f} to play with".format(total))

    if total < 1:
        print("Sorry you don't have enough money to continue.  Game over")
        keep_going = "end"
    else:
        keep_going = input("Press <enter> to play again or any key to quit")
    #faerrwell for user at the end of the game.
print("Thanks for playing. ")                                                                               #




