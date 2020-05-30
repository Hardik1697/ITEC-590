#!/usr/bin/env python
__author__ = "Hardik Anand"
__copyright__ = "Copyright 2020, Homework 04"

# A function that checks if a number is even or odd
# If the number is even, it prints number // 2 and returns number // 2
# If the number is odd, it prints 3 * number + 1 and returns 3 * number + 1
def collconject(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3*number + 1)
        return 3*number + 1
# the main function is used to test the other functions
# this code isn't run if this module isn't the main module
def main():
    while True:
        num = int(input("Enter a number: "))
        num = collconject(num)
        if num == 1:
            break
# if this module is the main module, call the main function
# to test the other functions
if __name__ == "__main__":
    main()
