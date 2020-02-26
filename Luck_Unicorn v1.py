#Component 1: Ask user how much money
#  Check that amount is an integer that is more / than equal to 1 and less than 20

#number checking function goes here
def intcheck(question, low, high):
    valid = Falseerror = "please enter an intgeer between {} and {}".format(low, high)
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


# Main routine




keep_going = ""
while keep_going == "":
    how_much = intcheck("how much money would you like to play with? ", 1, 10)
    print("you have chosen to play with ${}".format(how_much))


    keep_going = input("Again? ")