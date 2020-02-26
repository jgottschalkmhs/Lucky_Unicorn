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

    #########################

    print()
    print(feedback)
    print("You have {} to play with".format(total))

    if total < 1:
        print("Sorry you dont have enough money to continue.  Game over")
        keep_going = "end"
    else:
        keep_going = input("Press <enter> to play again or any key to quit")

print("Thanks for playing. ")