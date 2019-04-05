import random


# we now declare a function that does "all" the work.
# all the work is simply to print one integer between a and 6
# It is a good idea to declare all functions in one place.
def first_function():
    print(random.randint(1, 6))

continue_program = True

while continue_program:
    # call to the first_function
    first_function()
    # and again check if the user wants to "have another round".
    user_decision = input("Do you want to do this again (Y/N)")

    # get the usual response from the user
    if user_decision == 'N':
        print("I'm quitting")
        continue_program = False
    elif user_decision == 'Y':
        print('Lets have another round')

print("Game Over")

# if you feel like reading about random numbers in Python:
# https://docs.python.org/3.1/library/random.html#random.randint
