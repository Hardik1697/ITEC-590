# Copyright 2020
# Written by Hardik Anand


from dice import Dice, Die

def main():
    print("The Dice Roller program")
    # Declare i as 6
    i = 6
    # Use a loop to create a Die object until i equals 0
    while i != 0:
        # Create a Die object by using i as the value
        d = Die(i)
        # Call the image function to draw the die's picture
        d.image
        # Decrement i byy 1
        i -= 1
    # Print an empty line
    print()
    # get number of dice from user
    count = int(input("Enter the number of dice to roll: "))

    # create Die objects and add to Dice object
    dice = Dice()
    for i in range(count):
        die = Die(None)
        dice.addDie(die)

    while True:        
        # roll the dice
        dice.rollAll()
        print("YOUR ROLL: ")
        for die in dice.list:
            # Call the image function from Die class to draw picture of the value
            die.image
        print("\n")
        # Call the getTotal function from the Dice class and assign it to tot
        tot = dice.getTotal()
        # print tot
        print("Total: " + str(tot))
        # Call the getAvg function from the Dice class and assign it to avg
        avg = dice.getAvg()
        # print avg
        print("Average: " + str(avg) + "\n")
        choice = input("Roll again? (y/n): ")
        if choice != "y":
            print("Bye!")
            break

if __name__ == "__main__":
    main()
