# Lucky Unicorn - payment mechanics

# to do
# adjust total correctly for a given token
# - if its a unicorn, add $5
# - if its a zebra / horse, subtract 0.5
# - if its a donkey, subtract 1
# Give user feedback based on winnings..
# State new total

# assume starting amount in $10
total = int(input("how much would you like to play with? "))

keep_going = ""
while keep_going == "":


    #Allow manual token input for testing purposes
    token = input("enter a token: ")

    #adjust total correctly for a given token
    if token == "unicorn":
        total += 5
        feedback = "Congrats you won $5.00"
    elif token == "donkey":
        total -= 1
        feedback = "sorry, you did not win anything this round"
    else:
        total -= 0.5
        feedback = "congrats you won 50c"

    print()

    print(feedback)
    print("you have {} to play with".format(total))

    if total < 1:
        print("Sorry you don't have enough money to continue. Game over")
        keep_going = "end"
    else:
        keep_going = input("Press <enter> to play again or any key to quit")

print("Thank you for playing.")