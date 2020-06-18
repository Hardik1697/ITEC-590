# Copyright 2020
# Written by Hardik Aannd


# Imported various libraries for implementation later on.
# copy is used to copy a list to another list
import copy
# os is used to check if the file exists in the working directory
import os
# sys is used to exit the program
import sys
# time is used to compute the total time taken by every algorithm
import time


# This function takes in a param message and gives the text a typewriter effect
def typewriter(message):
    # For loop to iterate over every character in the string message
    for char in message:
        # write the character to the console
        sys.stdout.write(char)
        # Flush the buffer
        sys.stdout.flush()
        # Sleep for 0.016 ms - this gives the effect of a typewriter
        time.sleep(0)


# This function reads the text file and stores it's contents into a list
def read_file():
    # While loop to run infinitely until an integer list is returned
    while True:
        # Call the typewriter function to print out text
        typewriter("Please enter the file name you want to use without extension (E.g., FileName): ")
        # ask for the name of the file
        name = input("")
        # append name with .txt
        name += ".txt"
        # check if the file does not exist in the working directory
        if not os.path.exists(name):
            # Call the typewriter function to print out text
            typewriter("This file does not exist, please try again\n")
        else:
            # set exists to true
            exists = True
            # try and except block for exception handling
            try:
                # open file for reading
                file = open(name, "r")
            # os error
            except OSError:
                # Call the typewriter function to print out text
                typewriter("File found - error reading file\n")
                # exit program
                sys.exit()
            # unexpected exception
            except Exception:
                # Call the typewriter function to print out text
                typewriter("An unexpected error occurred\n")
                # exit program
                sys.exit()
            # create a list and read the lines from the file to it
            str_list = file.readlines()
            # create a new list
            str_list1 = []
            # for loop for each line in the list
            for line in str_list:
                # the line is appended without the '\n' character in the new list
                # this is done for error checking later on, so that we can check if all
                # values in the list are of type int
                str_list1.append(line.strip())
            # create an int list
            int_list = []
            # for loop to iterate through every line
            for line in str_list1:
                # check if the line is a digit
                if line.isdigit():
                    # append int casted line to the int list
                    int_list.append(int(line))
                else:
                    # Call the typewriter function to print out text
                    typewriter("The value is not an integer, please use a different file, or modify the file to make "
                               "it "
                               "full of integers\n")
                    # exit program
                    sys.exit()
            # check if int list is not of type None
            if int_list is not None:
                # return the int list, exists and the name variables
                return int_list, exists, name
                # break out of loop
                break
            else:
                # call the read_file function recursively if the file does not exist in the working directory
                read_file()
    # return None, None, and name
    return None, None, name


# this function computes the average time taken by a sorting algorithm
def avg_time_taken(data):
    # declare sum and avg as 0.0
    sum = 0.0
    avg = 0.0
    # for loop to iterate till the end of data
    for i in data:
        # add i to sum
        sum += i
    # compute avg using sum and the length of the data list
    avg = sum / len(data)
    # return avg
    return avg


# this function updates the dictionary created in the main function
# which has the average times for all the sortign algorithms
def update_dict(dict, key, val):
    # update the value
    dict[key] = val
    # return the dictionary dict
    return dict


# this function performs selection sort
def selection_sort(data):
    # create new_list to opy data from param
    new_list = copy.copy(data)
    # declare start as time.time(), this notes the internal clock's time at the current moment
    start = time.time()
    # for loop to iterate through till the length of the new list
    for i in range(len(new_list)):
        # set min as i
        min = i
        # for loop to iterate from i + 1'th position to the length of the new list
        for j in range(i + 1, len(new_list)):
            # check if new list at min index is greater than new list at j'th index
            # basically checks if i > i + 1
            if new_list[min] > new_list[j]:
                # set min as j
                min = j
        # swap respective elements
        # new list at i with new list at min
        # new list at min with new list at i
        new_list[i], new_list[min] = new_list[min], new_list[i]

    # set end as time.time(), this notes the internal clock's time at the current moment
    end = time.time()
    # check if the length of the list is less than 30
    # we call the typewriter function if the condition is met
    list_printer(data, new_list)
    # tot is end - start, this computes the total time taken by the algorithm
    tot = end - start
    # return tot
    return tot


def step_print_ss(data):
    typewriter("\nOld list: " + str(data) + "\n")
    # create new_list to opy data from param
    new_list = copy.copy(data)
    # declare start as time.time(), this notes the internal clock's time at the current moment
    # for loop to iterate through till the length of the new list
    for i in range(len(new_list)):
        print('\033[1m' + "Iteration: " + str(i + 1) + '\033[0m')
        # set min as i
        min = i
        # for loop to iterate from i + 1'th position to the length of the new list
        for j in range(i + 1, len(new_list)):
            # check if new list at min index is greater than new list at j'th index
            # basically checks if i > i + 1
            if new_list[min] > new_list[j]:
                # set min as j
                min = j
        # swap respective elements
        # new list at i with new list at min
        # new list at min with new list at i
        if new_list[i] != new_list[min]:
            typewriter("Swapping: " + str(new_list[i]) + " ---> " + str(new_list[min]) + "\n")
        else:
            typewriter("Nothing to swap " + str(new_list[i]) + " is the min value\n")
        new_list[i], new_list[min] = new_list[min], new_list[i]
        print_new_list(data, new_list)
    list_printer(data, new_list)
    typewriter("\n")


# this function performs bubble sort
def bubble_sort(data):
    # create new_list to opy data from param
    new_list = copy.copy(data)
    # declare start as time.time(), this notes the internal clock's time at the current moment
    start = time.time()
    # for loop to iterate through till the length of the new list
    for i in range(len(new_list) - 1):
        # for loop to iterate from 0'th index till the length - i - 1'th index
        for j in range(0, len(new_list) - i - 1):
            # check if the new list at j'th index is greater than the new list at j + 1'th index
            if new_list[j] > new_list[j + 1]:
                # swap new list at j with new list at j + 1
                # swap new list at j + 1 with new list at j
                new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]

    # set end as time.time(), this notes the internal clock's time at the current moment
    end = time.time()
    list_printer(data, new_list)
    # tot is end - start, this computes the total time taken by the algorithm
    tot = end - start
    # return tot
    return tot


# this function performs bubble sort
def step_print_bs(data):
    typewriter("\nOld list: " + str(data) + "\n")
    # create new_list to opy data from param
    new_list = copy.copy(data)
    # for loop to iterate through till the length of the new list
    for i in range(len(new_list) - 1):
        print('\033[1m' + "Iteration: " + str(i + 1) + '\033[0m')
        # for loop to iterate from 0'th index till the length - i - 1'th index
        for j in range(0, len(new_list) - i - 1):
            # check if the new list at j'th index is greater than the new list at j + 1'th index
            if new_list[j] > new_list[j + 1]:
                # swap new list at j with new list at j + 1
                # swap new list at j + 1 with new list at j
                if new_list[j] != new_list[j + 1]:
                    typewriter("Swapping: " + str(new_list[j]) + " ---> " + str(new_list[j + 1]) + "\n")
                new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]
                print_new_list(data, new_list)
            else:
                typewriter("Nothing to swap\n")
    list_printer(data, new_list)


# this function performs insertion sort
def insertion_sort(data):
    new_list = copy.copy(data)
    start = time.time()
    # Traverse through 1 to len(arr)
    for i in range(1, len(new_list)):
        key = new_list[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0:
            if key < new_list[j]:
                new_list[j + 1] = new_list[j]
                new_list[j] = key
                j -= 1
            else:
                break

    end = time.time()
    list_printer(data, new_list)
    tot = end - start
    return tot


# this function performs insertion sort
def step_print_is(data):
    typewriter("\nOld list: " + str(data) + "\n")
    new_list = copy.copy(data)
    start = time.time()
    # Traverse through 1 to len(arr)
    for i in range(1, len(new_list)):
        print('\033[1m' + "Iteration: " + str(i) + '\033[0m')
        key = new_list[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0:
            if key < new_list[j]:
                print("Key is: " + str(key))
                new_list[j + 1] = new_list[j]
                new_list[j] = key
                print_new_list(data, new_list)
                j -= 1
            else:
                typewriter("Key: " + str(key) + " is at it's correct place. Nothing to the left is bigger than it.\n")
                break
    list_printer(data, new_list)


def list_printer(data, new_list):
    if len(data) < 30:
        # Call the typewriter function to print out text
        typewriter("\nUnsorted list:\n")
        typewriter(str(data) + "\n")
        typewriter("Sorted list:\n")
        typewriter(str(new_list) + "\n")
    else:
        print("\nUnsorted list:\n")
        print(str(data) + "\n")
        print("Sorted list:\n")
        print(str(new_list) + "\n")


def print_new_list(data, new_list):
    if len(data) < 30:
        # Call the typewriter function to print out text
        typewriter("List after this iteration:\n")
        typewriter(str(new_list) + "\n")
    else:
        print("List after this iteration:\n")
        print(str(new_list) + "\n")


def main():
    # Call the typewriter function to print out text
    typewriter("Welcome to the Sorting program!\n")
    name = ""
    contents = []
    val = False
    [contents, val, name] = read_file()
    if val and contents is not None:
        print()
        avg_time_s = []
        avg_time_b = []
        avg_time_i = []
        s_count = 0
        b_count = 0
        i_count = 0
        tot_s = 0
        tot_b = 0
        tot_i = 0
        avg_s = 0
        avg_b = 0
        avg_i = 0
        r_tot_s = 0
        r_tot_b = 0
        r_tot_i = 0
        dict = {"Selection Sort": 0.0, "Bubble Sort": 0.0, "Insertion Sort": 0.0}
        while True:
            tot = 0
            # Call the typewriter function to print out text
            typewriter("\nMenu\n1. Selection Sort\n2. Bubble Sort\n3. Insertion "
                       "Sort\n4. Print out the average time for "
                       "all the algorithms\n5. Print out all the steps for each "
                       "algorithm\n6. Change the file (Current file: " + str(name) + ")\n0. Exit\n")
            choice = input("")
            if choice == "1":
                # Call the typewriter function to print out text
                typewriter("\nPerforming Selection Sort...\n")
                s_count += 1
                tot_s = selection_sort(contents)
                r_tot_s = round(tot_s * 1000, 4)
                avg_time_s.append(r_tot_s)
                avg_s = avg_time_taken(avg_time_s)
                avg_s = round(avg_s, 4)
                # Call the typewriter function to print out text
                typewriter("\nTime Taken for this iteration: " + str(r_tot_s) + " Milliseconds\n")
                # Call the typewriter function to print out text
                typewriter("Average Time for " + str(s_count) + " iterations: " + str(avg_s) + " Milliseconds\n\n")
                if s_count >= 3:
                    dict = update_dict(dict, "Selection Sort", avg_s)
            elif choice == "2":
                # Call the typewriter function to print out text
                typewriter("\nPerforming Bubble Sort...\n")
                b_count += 1
                tot_b = bubble_sort(contents)
                r_tot_b = round(tot_b * 1000, 4)
                avg_time_b.append(r_tot_b)
                avg_b = avg_time_taken(avg_time_b)
                avg_b = round(avg_b, 4)
                # Call the typewriter function to print out text
                typewriter("\nTime Taken for this iteration: " + str(r_tot_b) + " Milliseconds\n")
                # Call the typewriter function to print out text
                typewriter("Average Time for " + str(b_count) + " iterations: " + str(avg_b) + " Milliseconds\n\n")
                if b_count >= 3:
                    dict = update_dict(dict, "Bubble Sort", avg_b)
            elif choice == "3":
                # Call the typewriter function to print out text
                typewriter("\nPerforming Insertion Sort...\n")
                i_count += 1
                tot_i = insertion_sort(contents)
                r_tot_i = round(tot_i * 1000, 4)
                avg_time_i.append(r_tot_i)
                avg_i = avg_time_taken(avg_time_i)
                avg_i = round(avg_i, 4)
                # Call the typewriter function to print out text
                typewriter("\nTime Taken for this iteration: " + str(r_tot_i) + " Milliseconds\n")
                # Call the typewriter function to print out text
                typewriter("Average Time for " + str(i_count) + " iterations: " + str(avg_i) + " Milliseconds\n\n")
                if i_count >= 3:
                    dict = update_dict(dict, "Insertion Sort", avg_i)
            elif choice == "0":
                # Call the typewriter function to print out text
                typewriter("\nBye...")
                sys.exit()
            elif choice == "5":
                typewriter("\n1. Selection Sort\n2. Bubble Sort\n3. Insertion Sort\n\n")
                step = input("")
                if step == "1":
                    step_print_ss(contents)
                elif step == "2":
                    step_print_bs(contents)
                elif step == "3":
                    step_print_is(contents)
            elif choice == "4":
                # Call the typewriter function to print out text
                typewriter("\nPrinting out the average times for all the algorithms\nThe average time for an "
                           "algorithm will be 0.0 if it has not been run 3 times\nThis is how the code is programmed "
                           "to run\n\n")
                # Call the typewriter function to print out text
                typewriter("Selection sort has run " + str(s_count) + " times\nBubble Sort has run " + str(
                    b_count) + " times"
                               "\nInsertion Sort has run " + str(i_count) + " times\n\n"
                                                                            "Following are the Average Times for the "
                                                                            "3 algorithms:")
                for i in dict:
                    # Call the typewriter function to print out text
                    typewriter("\n" + str(i) + ": " + str(dict[i]))
                # Call the typewriter function to print out text
                typewriter("\n\n")
            elif choice == "6":
                [contents, val, name] = read_file()
                avg_time_s = []
                avg_time_b = []
                avg_time_i = []
                s_count = 0
                b_count = 0
                i_count = 0
                tot_s = 0
                tot_b = 0
                tot_i = 0
                avg_s = 0
                avg_b = 0
                avg_i = 0
                r_tot_s = 0
                r_tot_b = 0
                r_tot_i = 0
                # Call the typewriter function to print out text
                typewriter("\n")
            else:
                # Call the typewriter function to print out text
                typewriter("\nThis is not a valid option, please try again...\n")
    elif not val:
        # Call the typewriter function to print out text
        typewriter("The File Does Not exist, please try again\n")
    elif contents is None:
        # Call the typewriter function to print out text
        typewriter("The file is empty, please try again\n")
    else:
        # Call the typewriter function to print out text
        typewriter("An unexpected error occurred\nExiting program")
        sys.exit()


# Run the main function
if __name__ == '__main__':
    main()
