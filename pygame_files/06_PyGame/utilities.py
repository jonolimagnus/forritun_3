import random
# notice we do not need PyGame for this since the two classes constructed here
# are independent of the library and can therefor be used without it!


# A simple class in Python.
# the __init__(self) is the class constructor and within it all member
# variables are declared and initialised if needed.
class Dice:
    def __init__(self):
        self.number = 0

    # this is the classes only function. it randomizes a number
    # from 1 up to but NOT including 6 and returns that number to the calling program.
    def throw(self):
        self.number = random.randint(1,6)
        return self.number

# slightly more complicated class.
# the constructor has one parameter(apart for the obligatory self) how_many.
# should the user of the class not provide how many dice he/she wants to work
# with, the default is set at 5.
class DiceThrower:
    def __init__(self, how_many=5):
        self.number_of_dice = how_many
        self.dice = Dice()
        # a 5 element list is created and initialized to -1
        self.dice_list = [-1 for i in range(self.number_of_dice)]
    # the throw function calls upon the dice object to produce a number
    # that is then added to the dice_list.
    # when the list is full it is returned
    def throw(self):
        for x in range(0, self.number_of_dice):
            self.dice_list[x] = self.dice.throw()
        return self.dice_list

    # the rethrow function as the name suggests, throws some or all
    # dice again.  It requires a list of those dice to rethrow.
    # it the list is not of the right length, all of the dice are thrown.
    def rethrow(self, rethrow_list=[]):
        # the number of elements in the list must be between 0 and number of
        # elements in self.dice_list
        if 0 < len(rethrow_list) <= self.number_of_dice:
            # another check is performed to verify that the numbers in the
            # rethrow list are valid.  If they are, the corresponding dice are thrown.
            # otherwise all dice are thrown.
            if min(rethrow_list) >= 0 and max(rethrow_list) <= self.number_of_dice - 1:
                for item in rethrow_list:
                    self.dice_list[item] = self.dice.throw()
            return self.dice_list
        else:
            return self.throw()
