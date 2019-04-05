import utilities

# we create an DiceThrower object and call it dt.
dt = utilities.DiceThrower()
# we have the object throw dice and put the numbers in the my_dice list
my_dice = dt.throw()

# print the numbers out
print (my_dice)
print('------------------------------------------------')

# prompt the user.
s = input("Enter the dices you want to rethrow(0 - 4) space between please: ")
# split the user input to create an array(items)
items = s.split()
rethrow_dice = [eval(x) for x in items]

# print that list of dice indexes the user supplied
print(rethrow_dice)

# call the rethrow function and store the results in the rethrow_dice list
my_dices = dt.rethrow(rethrow_dice)
# print out the "updated" dice list
print(my_dice)
print('------------------------------------------------')

# let the program execution continue until the user supplies something
x = input("Enter something to exit:")
