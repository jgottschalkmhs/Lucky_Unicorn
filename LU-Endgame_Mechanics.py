# LU   End Mechanics

#To Do
# Ask user how much they want to play with
# If the total is less that $1, quuit
# If the total is more than $1, ask user if they want to keep going

# Assume starting amount is $10

total = int(input("How much would you like to play with? "))

keep_going = ""
while keep_going == "":

    #allow manual token input for testing purposes
    token = input("Enter a token")

    # Adjust total correctly for a given token
    if token == "unicorn":
        total += 5
        feedback = "Congrats you won $5.00"
    elif token == "donkey":
        total -= 1
        feedback = "sorry, you did not win anything this round"
    else:
        total -= 0.5
        feedback = "Congrats you won 50c"

    print()
    print(feedback)
    print("You have {} to play with".format(total))

    if total < 1:
        print("Sorry you dont have enough money to continue.  Game over")
        keep_going = "end"
    else:
        keep_going = input("Press <enter> to play again or any key to quit")

print("Thanks for playing. ")


