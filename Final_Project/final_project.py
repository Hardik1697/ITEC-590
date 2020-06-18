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
        time.sleep(0.016)


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
# which has the average times for all the sorting algorithms
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
    # call list printer function to print out the unsorted and sorted list
    list_printer(data, new_list)
    # tot is end - start, this computes the total time taken by the algorithm
    tot = end - start
    # return tot
    return tot


# This function prints out the steps of selection sort
def step_print_ss(data):
    typewriter("Steps for Selection Sort:\nOld list: " + str(data) + "\n")
    # create new_list to opy data from param
    new_list = copy.copy(data)
    # declare start as time.time(), this notes the internal clock's time at the current moment
    # for loop to iterate through till the length of the new list
    for i in range(len(new_list)):
        typewriter("Iteration: " + str(i + 1) + "\n")
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
    # call list printer function to print out the unsorted and sorted list
    list_printer(data, new_list)
    # tot is end - start, this computes the total time taken by the algorithm
    tot = end - start
    # return tot
    return tot


# This function prints out the steps of bubble sort
def step_print_bs(data):
    typewriter("Steps for Bubble Sort: \nOld list: " + str(data) + "\n")
    # create new_list to opy data from param
    new_list = copy.copy(data)
    # for loop to iterate through till the length of the new list
    for i in range(len(new_list) - 1):
        typewriter("Iteration: " + str(i + 1) + "\n")
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
    # A for loop to iterate through till the length of the new list
    for i in range(1, len(new_list)):
        # Define k as new list at index i
        k = new_list[i]
        # Define j as i - 1
        j = i - 1
        # Check using a while loop, that while j is more than equal to 0 and
        # K is less than new list at j
        while j >= 0 and k < new_list[j]:
            # We assign new list at j + 1 to new list at j
            new_list[j + 1] = new_list[j]
            # Decrement j by 1
            j -= 1
        # Moving k to it's correct position
        new_list[j + 1] = k

    # set end as time.time(), this notes the internal clock's time at the current moment
    end = time.time()
    # call list printer function to print out the unsorted and sorted list
    list_printer(data, new_list)
    tot = end - start
    return tot


# This function prints out the steps of insertion sort
def step_print_is(data):
    typewriter("Steps for Insertion Sort: \nOld list: " + str(data) + "\n")
    new_list = copy.copy(data)
    start = time.time()
    # Traverse through 1 to len(arr)
    for i in range(1, len(new_list)):
        typewriter("Iteration: " + str(i) + "\n")
        key = new_list[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0:
            if key < new_list[j]:
                typewriter("Key is: " + str(key))
                new_list[j + 1] = new_list[j]
                new_list[j] = key
                print_new_list(data, new_list)
                j -= 1
            else:
                typewriter("Key: " + str(key) + " is at it's correct place. Nothing to the left is bigger than it.\n")
                break
    list_printer(data, new_list)


# this function prints out the sorted and unsorted list
def list_printer(data, new_list):
    # Call the typewriter function print out the lists, if the length
    # of the list is less than 30, because it does not take too much time
    # to print out the list less than 30 elements, using the typewriter function
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


# this function prints out just the sorted list
# this is used to print out the list after every iteration,
# used in step print functions above.
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
    # declare name as an empty string
    name = ""
    # declare contents as an empty list
    contents = []
    # declare val as false
    val = False
    # store variables returned from read_file in contents, val and name
    [contents, val, name] = read_file()
    # Check if val is True and contents is not None
    if val and contents is not None:
        # Print out an empty line
        typewriter("\n")
        # Declare 3 empty lists to compute average times for each algorithm
        avg_time_s = []
        avg_time_b = []
        avg_time_i = []
        # Declare 3 variables to see how many times each algorithm has been run
        s_count = 0
        b_count = 0
        i_count = 0
        # Declare 3 total variables to get the total time of an algorithm
        tot_s = 0
        tot_b = 0
        tot_i = 0
        # Declare average time variables to compute the average time taken by each algorithm
        avg_s = 0
        avg_b = 0
        avg_i = 0
        # Declare rounded variables to get the rounded average time for each algorithm
        r_tot_s = 0
        r_tot_b = 0
        r_tot_i = 0
        # Declare a dictionary dict to store the name of the sorting algorithm as the key and 0.0 as the value.
        # Value's will be updated once the algorithm has been run 3 times.
        dict = {"Selection Sort": 0.0, "Bubble Sort": 0.0, "Insertion Sort": 0.0}
        # while loop, which will run till sys.exit() is called
        while True:
            # Call the typewriter function to print out text
            typewriter("\nMenu\n1. Selection Sort\n2. Bubble Sort\n3. Insertion "
                       "Sort\n4. Print out the average time for "
                       "all the algorithms\n5. Print out all the steps for each "
                       "algorithm\n6. Change the file (Current file: " + str(name) + ")\n0. Exit\n")
            # get input and store it in the variable choice
            choice = input("")
            # If choice is 1, run the selection sort algorithm
            if choice == "1":
                # Call the typewriter function to print out text
                typewriter("\nPerforming Selection Sort...\n")
                # increment s_count by 1 every time choice is 1
                s_count += 1
                # call the selection_sort function on tot_s variable to get the total time
                tot_s = selection_sort(contents)
                # compute the rounded time from total time
                r_tot_s = round(tot_s * 1000, 4)
                # append the rounded time, in the avg_time_s list
                avg_time_s.append(r_tot_s)
                # compute the avg time from calling the avg_time_taken function
                avg_s = avg_time_taken(avg_time_s)
                # store the rounded avg time to the same variable
                avg_s = round(avg_s, 4)
                # Call the typewriter function to print out text
                typewriter("\nTime Taken for this iteration: " + str(r_tot_s) + " Milliseconds\n")
                # Call the typewriter function to print out text
                typewriter("Average Time for " + str(s_count) + " iterations: " + str(avg_s) + " Milliseconds\n\n")
                # check if s_count is more than equal than 3
                if s_count >= 3:
                    # update the dictionary's, key: Selection Sort's value with the avg_s variable
                    dict = update_dict(dict, "Selection Sort", avg_s)
            # if choice is 2
            elif choice == "2":
                # Call the typewriter function to print out text
                typewriter("\nPerforming Bubble Sort...\n")
                # increment b_count by 1 every time choice is 1
                b_count += 1
                # call the selection_sort function on tot_b variable to get the total time
                tot_b = bubble_sort(contents)
                # compute the rounded time from total time
                r_tot_b = round(tot_b * 1000, 4)
                # append the rounded time, in the avg_time_b list
                avg_time_b.append(r_tot_b)
                # compute the avg time from calling the avg_time_taken function
                avg_b = avg_time_taken(avg_time_b)
                # store the rounded avg time to the same variable
                avg_b = round(avg_b, 4)
                # Call the typewriter function to print out text
                typewriter("\nTime Taken for this iteration: " + str(r_tot_b) + " Milliseconds\n")
                # Call the typewriter function to print out text
                typewriter("Average Time for " + str(b_count) + " iterations: " + str(avg_b) + " Milliseconds\n\n")
                # check if b_count is more than equal than 3
                if b_count >= 3:
                    # update the dictionary's, key: Bubble Sort's value with the avg_s variable
                    dict = update_dict(dict, "Bubble Sort", avg_b)
            # if choice is 3
            elif choice == "3":
                # Call the typewriter function to print out text
                typewriter("\nPerforming Insertion Sort...\n")
                # increment i_count by 1 every time choice is 1
                i_count += 1
                # call the selection_sort function on tot_i variable to get the total time
                tot_i = insertion_sort(contents)
                # compute the rounded time from total time
                r_tot_i = round(tot_i * 1000, 4)
                # append the rounded time, in the avg_time_i list
                avg_time_i.append(r_tot_i)
                # compute the avg time from calling the avg_time_taken function
                avg_i = avg_time_taken(avg_time_i)
                # store the rounded avg time to the same variable
                avg_i = round(avg_i, 4)
                # Call the typewriter function to print out text
                typewriter("\nTime Taken for this iteration: " + str(r_tot_i) + " Milliseconds\n")
                # Call the typewriter function to print out text
                typewriter("Average Time for " + str(i_count) + " iterations: " + str(avg_i) + " Milliseconds\n\n")
                # check if i_count is more than equal than 3
                if i_count >= 3:
                    # update the dictionary's, key: Insertion Sort's value with the avg_s variable
                    dict = update_dict(dict, "Insertion Sort", avg_i)
            # if choice is 0
            elif choice == "0":
                # Call the typewriter function to print out text
                typewriter("\nBye...")
                # call the sys.exit() functionality
                sys.exit()
            # if choice is 5
            elif choice == "5":
                # Call the typewriter function to print out text
                typewriter("\n1. Selection Sort\n2. Bubble Sort\n3. Insertion Sort\n\n")
                # take input and store it in step
                step = input("")
                # if step is 1
                if step == "1":
                    # call the step_print_ss function
                    step_print_ss(contents)
                # if step is 2
                elif step == "2":
                    # call the step_print_ss function
                    step_print_bs(contents)
                # if step is 1
                elif step == "3":
                    # call the step_print_ss function
                    step_print_is(contents)
                # else not a valid option
                else:
                    typewriter("\nThis is not a valid option\n")
            # if choice is 4
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
                # for loop to iterate till the end of dict
                for i in dict:
                    # Call the typewriter function to print out text
                    typewriter("\n" + str(i) + ": " + str(dict[i]))
                # Call the typewriter function to print out text
                typewriter("\n\n")
            # if choice is 6
            elif choice == "6":
                # reset all variables created in the main function's start to change the file being used to run the
                # program
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
            # else not a valid option
            else:
                # Call the typewriter function to print out text
                typewriter("\nThis is not a valid option, please try again...\n")
    # if val is false, print out error message
    elif not val:
        # Call the typewriter function to print out text
        typewriter("The File Does Not exist, please try again\n")
    # if contents is of type None, print out error message
    elif contents is None:
        # Call the typewriter function to print out text
        typewriter("The file is empty, please try again\n")
    # else print out error message
    else:
        # Call the typewriter function to print out text
        typewriter("An unexpected error occurred\nExiting program")
        sys.exit()


# Run the main function
if __name__ == '__main__':
    main()
