# Copyright 2020
# Written by Hardik Aannd

# import random
import random
# imports os
import os
# import sys
import sys


# this function populates a list with random numbers whose range is taken from input in the main function
def pop(lst, ran, numbers):
    # use sample functionality of random to populate the list with random numbers
    lst = random.sample(range(ran), numbers)
    # return lst
    return lst


# this function writes to a file
def write_to_file(name, lst):
    # check if the file already exists
    if os.path.exists(name):
        print("This file already exists please try again")
        sys.exit()
    # else
    else:
        # try and except block to write to file
        try:
            # open file for writing
            f = open(name, 'w')
            # write lines from lst
            f.writelines("%s\n" % i for i in lst)
            # close file
            f.close()
        # 3 Exceptions -
        except FileNotFoundError as e:
            print(e)
        except OSError as e:
            print(e)
        except Exception as e:
            print(e)


def main():
    # declare lst as an empty list
    lst = []
    # take input and store in name
    name = input("Enter the name of the new file you want to create, without extension (E.g., fileName): ")
    # append '.txt' to name
    name += ".txt"
    # take input as an int and store it in ran, this corresponds to the range from 0 to input, where a
    # random number can be between 0 and input - 1
    ran = int(input("Enter the range of the numbers. E.g., if you want a range of numbers between 0 and 100 (0 is "
                    "included and 100 is not), enter 100: "))
    # input how many numbers we want to populate the file with
    numbers = int(input("Enter the number of integers you want to populate the text file with: "))
    # call the pop function
    lst = pop(lst, ran, numbers)
    # call the write_to_file function
    write_to_file(name, lst)


if __name__ == '__main__':
    main()
