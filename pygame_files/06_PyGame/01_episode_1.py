continue_program = True

while continue_program:
    print("now the program is running")
    print("Upon finishing it asks if the user wants to continue")

    # the code below is to get info from the user if he/she wants to continue
    # to run the code above.
    user_decision = input("Do you want to do this again (Y/N)")

    # the user input is inspected and the "continue_program" variable is
    # set to false if he user types N
    if user_decision != 'Y':
        print ("I'm quitting")
        continue_program = False

print ("It's all over")
