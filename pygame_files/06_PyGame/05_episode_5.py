import random


# the function now returns five random numbers between 1 and 6 as a list elements
def first_function():
    # declaring the list
    the_numbers = []
    #add five numbers each between 1 and 6
    for num in range(0, 5):
        the_numbers.append(random.randint(1, 6))
    #returning the numbers
    return the_numbers


# second_function takes a list as an argument and prints its contents.
def second_function(my_list):
    for num in my_list:
        print(num)

# remember this one
continue_program = True

while continue_program:
    # call to the first_function
    list_of_numbers = first_function()
    second_function(list_of_numbers)
    # and again check if the user wants to "have another round".
    user_decision =input("Do you want to do this again (Y/N)")

    # get the usual response from the user, slightly modified
    if user_decision == 'N':
        continue_program = False
    elif user_decision == 'Y':
        print('Lets have another round')

print("That's it I'm outta here")

