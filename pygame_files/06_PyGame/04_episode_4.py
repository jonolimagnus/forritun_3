import random


# the function now prints out five random numbers between 1 and 6
def first_function():
    for num in range(0, 5):
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
