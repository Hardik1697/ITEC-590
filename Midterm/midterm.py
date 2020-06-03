# Copyright 2020
# Written by Hardik Anand

# Import statements to use the functionality of the csv, os and sys
import csv
import os
import sys


# This function takes in parameter file and reads data from the csv file into a list
def read_items(file):
    # Try and except block to catch any exceptions
    try:
        # Open the file with the parameter
        with open(file, newline='') as f:
            # Create a reader type variable that will iterate through the file
            reader = csv.reader(f)
            # Store the data from the file into the list called data
            data = list(reader)
            # Return the list data
            return data
    # Exception if the file is not found
    except FileNotFoundError:
        print("\nError! File by tha name of " + file + " does not exist, please try again")
    # Exception if the file is found, but there was an error reading from it
    except OSError:
        print("\nFile found - error reading from file")
    # Exception if an unexpected error occurs
    except Exception as e:
        print(type(e), e)
        exit_program()
    except IOError:
        print("\nEither File does not exist or there is a permission error")


# This function displays all the items stored in the parameter item_list,
# which we created from the read_items function
def Display_items():
    empty_str = ""
    # Prompt the user for filename
    filename = input("\nEnter the name of the csv file without extension (E.g., filenname): ")
    # Add the .csv extension to the name variable, so that it can be written to
    filename = filename + ".csv"
    # Call the read_items function on contents to store the data from the file into contents
    contents = read_items(filename)
    # Check if contents is not of type None (If nothing was read from the file,
    # or the file was not found)
    if not contents is None:
        # Declare i as 0 to be later used in the for loop ahead
        i = 0
        # Print statement
        print("\nDisplaying contents from " + filename, "\n")
        # Print an empty string justified left 137 characters filled with '*'
        print(empty_str.ljust(137, "*"))
        # Print statement using multiple left justified statements of different length
        # NAME is justified left with 28 characters
        # ARTIST is justified left with 29 characters
        # ALBUM is justified left with 39 characters
        # YEAR is justified left with 29 characters
        # RANK is justified left with 0 characters
        # '\033[1m' is used to make everything bold, and '\033[0m' is used to stop making the text bold
        # '|' is printed out last
        print('\033[1m', "NAME".ljust(28), "ARTIST".ljust(29), "ALBUM".ljust(39), "YEAR".ljust(29),
              "RANK".ljust(0), '\033[0m', "|")
        # Print an empty string justified left 135 characters filled with '-' and '|' is printed out last
        print(empty_str.ljust(135, "-"), "|")
        # Use a for loop to print out the contents of the list
        for row in contents:
            # If i is not equal to length of the contents - 1, print the following stuff
            if i != len(contents) - 1:
                # row[0] is justified left with 30 characters and is converted to uppercase using .upper()
                # row[1] is justified left with 30 characters and is converted to uppercase using .upper()
                # row[2] is justified left with 40 characters and is converted to uppercase using .upper()
                # row[3] is converted to a string and justified left with 31 characters and is converted
                # to uppercase using .upper()
                # row[4] is converted to a string and justified left with 4 characters and is converted
                # to uppercase using .upper()
                # '|' is printed out last
                # Increment the value of i by 1
                print(row[0].upper().ljust(30) + row[1].upper().ljust(30) + row[2].upper().ljust(40)
                      + str(row[3]).ljust(31) + str(row[4]).ljust(4), "|")
                print(empty_str.rjust(135, "-"), "|")
                i += 1
            # If i is equal to the length of the contents - 1
            else:
                # row[0] is justified left with 30 characters and is converted to uppercase using .upper()
                # row[1] is justified left with 30 characters and is converted to uppercase using .upper()
                # row[2] is justified left with 40 characters and is converted to uppercase using .upper()
                # row[3] is converted to a string and justified left with 31 characters and is converted
                # to uppercase using .upper()
                # row[4] is converted to a string and justified left with 4 characters and is converted
                # to uppercase using .upper()
                # '|' is printed out last
                # Print an empty string justified left 137 characters filled with '*', and print a new line after that
                print(row[0].upper().ljust(30) + row[1].upper().ljust(30) + row[2].upper().ljust(40)
                      + str(row[3]).ljust(31) + str(row[4]).ljust(4), "|")
                print(empty_str.rjust(137, "*"), "\n")
    # Print out error message if the contents is of type none
    else:
        print("There is nothing to display here\n")
    # Return contents and filename to be used later in the main function
    return [contents, filename]


# This function writes the data stored in the items_list to a new file
def write_items(item_list, filename):
    if not item_list is None:
        # Prompt the user for a filename to write the data of the item_list to
        name = input("\nEnter the new file name you wish to store the contents listed above to without extension"
                     "(E.g., newFile): ")
        # Add the .csv extension to the name variable, so that it can be written to
        name = name + ".csv"
        # Check if the new name provided by the user is not the same as the file we read the data from
        if not os.path.exists(name):
            # Open the file for writing with a try block
            try:
                file = open(name, 'w', newline='')
                # With file opened
                with file:
                    # Create write variable of writer type from csv file parameter file
                    write = csv.writer(file)
                    # Use writerows to write contents in the item_list to the newly created file
                    write.writerows(item_list)
                    # Print out a message after it's done
                print("\nDone! The contents from " + filename + " were written to " + name + "\n")
            # Catch and print the exception and call exit_program() function
            except Exception as e:
                print(type(e), e)
                exit_program()
        # If this file exits, print an error message
        else:
            print("\nThis file already exists. Please use a different name\n")
    # If the item_list parameter is empty, print the error message
    else:
        print("\nYou have nothing to write to the new file. Hint: Display the items from a file and then try"
              "this option\n")


# This function removes a file, if it exists in the working directory of this project
def remove_file():
    # Take input from user to remove the file (Only works for .Csv files)
    name = input("\nPlease enter the name of the file you want to remove without extension"
                 "(E.g., filename): ")
    name = name + ".csv"
    # If the file exists, remove it
    if os.path.exists(name):
        # Use os.remove(filename) to remove the file from current directory
        os.remove(name)
        print("\nDone! " + name + " was removed\n")
    # If not, print error message
    else:
        print("\nThis File does not exist. Please try again\n")


# This function lists all the .Csv files in the working directory
def list_csv_files():
    # Add the .Csv files to the file_list list
    file_list = [f for f in os.listdir('.') if os.path.isfile(os.path.join('.', f)) and f.endswith('.csv')]
    # Declare j as 1 to be used in for loop for formatting
    j = 1
    # Print out an empty line
    print()
    # Use a loop to iterate through the newly created list
    for i in file_list:
        # Print the contents in the list
        print(str(j) + ". " + i)
        # Increment j by 1
        j += 1
    # Print an empty line
    print()


# This function is used to terminate the program
def exit_program():
    # Print Bye!
    print("Bye!")
    # Use sys.exit() functionality from sys to exit the program
    sys.exit()


# This function gives the total of the items list
def total_function(items):
    # Check if items is not of type None
    if not items is None:
        # Declare total as 0
        total = 0
        # Iterate through items till the end
        for row in items:
            # Add the 4th index in the items list to the total
            total += int(row[4])
        # Create a string using the format method to fill the placeholders with appropriate values
        str_total_formatted = "\nThe total of ranks in this {name} is: {tot}".format(name="list", tot=total)
        # Print the formatted string
        print(str_total_formatted)
    # If items is of type None, print error message
    else:
        print("\nYou do not have a list to get a total of. Hint: Display the items from a file and then try this "
              "option to get the total of all the ranks provided in the list")


# Main function
def main():
    # Declare items as None and name as an empty string
    # This will be used for some error checking by the functions later in the while loop
    items = None
    name = ""
    # Execute loop till exit_program is called
    while True:
        choice = input(
            "Welcome to the CSV file program. Please Select one of the following\n1. Display Contents of the file\n2. "
            "List all the .Csv files\n3. Write content to a new file\n4. Remove a file\n5. Exit Program\n")
        # Call the Display_items function if choice is 1
        if choice == "1":
            # Use items and name (variables defined above while loop) to assign them values
            # from the Display_items function
            [items, name] = Display_items()
        # Call the list_items function if choice is 2
        elif choice == "2":
            list_csv_files()
        # Call the write_items function if choice is 3
        elif choice == "3":
            write_items(items, name)
        # Call the remove_file function if choice is 4
        elif choice == "4":
            remove_file()
        # Call the total_function and exit_program function if choice is 5
        elif choice == "5":
            total_function(items)
            exit_program()
        # If the choice does not match with the command menu, print error message
        else:
            print("\nThis is not a valid option, please try again...\n")


# Run the main function
if __name__ == '__main__':
    main()
