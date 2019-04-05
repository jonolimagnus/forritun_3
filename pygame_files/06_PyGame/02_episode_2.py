continue_program = True

# this text has been moved so it's only displayed at the start.
print ("Now the program is running")
print ("Upon finishing, it will ask if the user wants to continue")

while continue_program:
    # as before, see if the user wants to "have another round".
    user_decision = input("Do you want to do this again (Y/N)")

    # now we will handle the Y response from the user
    if user_decision == 'N':
        print("I'm quitting")
        continue_program = False
    elif user_decision == 'Y':
        print('Lets have another round')
    # WHAT HAPPENS IF THE USER DOES NOT ENTER N OR Y ??????
print("It's all over")
