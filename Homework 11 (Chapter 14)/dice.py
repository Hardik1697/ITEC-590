# Copyright 2020
# Written by Hardik Anand


import random


class Die:

    # Initializer for this class Checks if the value is of type None or not and constructs the object accordingly
    # This is used to overload the function to either construct the die's image in the start, from 1 - 6,
    # or construct the image from a random number
    def __init__(self, value):
        # If value is of type None, then it sets a random number to object's value by calling the roll method defined
        # in this class
        if value is None:
            self.__value = self.roll()
        # Else it sets the vale to the object's value
        else:
            self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value < 1:
            raise ValueError("Die can't be less than 1.")
        # If the value is more than 6, it displays error message
        elif value > 6:
            raise ValueError("Die can't be more than 6")
        else:
            self.__value = value

    def roll(self):
        self.__value = random.randrange(1, 7)
        return self.__value

    # This function prints an image of the die's value, according to the value
    @property
    def image(self):
        if self.value == 6:
            print(" _____ \n" + \
                  "|o   o|\n" + \
                  "|o   o|\n" + \
                  "|o___o|")
        elif self.value == 5:
            print(" _____ \n" + \
                  "|o   o|\n" + \
                  "|  o  |\n" + \
                  "|o___o|")
        elif self.value == 4:
            print(" _____ \n" + \
                  "|o   o|\n" + \
                  "|     |\n" + \
                  "|o___o|")
        elif self.value == 3:
            print(" _____ \n" + \
                  "|o    |\n" + \
                  "|  o  |\n" + \
                  "|____o|")
        elif self.value == 2:
            print(" _____ \n" + \
                  "|o    |\n" + \
                  "|     |\n" + \
                  "|____o|")
        elif self.value == 1:
            print(" _____ \n" + \
                  "|     |\n" + \
                  "|  o  |\n" + \
                  "|_____|")
        else:
            print("Not a valid value")


class Dice:
    def __init__(self):
        self.__list = []

    def addDie(self, die):
        self.__list.append(die)

    @property
    def list(self):
        dice_tuple = tuple(self.__list)
        return dice_tuple

    def rollAll(self):
        for die in self.__list:
            die.roll()

    # This function gets the total value of all the die's stored in the dice's list
    def getTotal(self):
        # Declare tot as 0
        tot = 0
        # Use a loop to iterate through all the die's in the list
        for die in self.__list:
            # Add the die's value to tot
            tot += die.value
        # Return tot
        return tot

    # This function gets the average value of all the die's stored in the dice's list
    def getAvg(self):
        # Declare tot and i as 0
        tot = 0
        i = 0
        # Use a loop to iterate through all the die's in the list
        for die in self.__list:
            # Increment i by 1 on each iteration
            i += 1
            # Add the die's value to tot
            tot += die.value
        # Check if tot / i is an integer
        if tot / i % 2 == 0:
            # Print tot / i
            return tot / i
        # Else round tot / i to 2 decimal values
        else:
            return round(tot / i, 2)