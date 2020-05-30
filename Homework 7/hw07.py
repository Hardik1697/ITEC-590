# Copyright 2020
# Written by Hardik Anand

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
        print("Error! File by tha name of " + file + " does not exist, please try again\n")
    # Exception if the file is found, but there was an error reading from it
    except OSError:
        print("File found - error reading from file\n")
    # Exception if an unexpected error occurs
    except Exception as e:
        print(type(e), e)
        print()
    except IOError:
        print("Either File does not exist or there is a permission error\n")


# This function displays all the items stored in the parameter item_list,
# which we created from the read_items function
def Display_items():
    # Prompt the user for filename
    filename = input("Enter the name of the csv file without extension (E.g., filenname): ")
    # Add the .csv extension to the name variable, so that it can be written to
    filename = filename + ".csv"
    # Call the read_items function on contents to store the data from the file into contents
    contents = read_items(filename)
    # Check if contents is not of type None (If nothing was read from the file,
    # or the file was not found)
    if not contents is None:
        # If contents if of type None, call the main function recursively
        # Declare i as 1, will be helpful printing the contents of the list
        i = 1
        # Use a for loop to print out the contents of the list
        for row in contents:
            # if condition is used for proper formatting, so that the output
            # looks neater on the console
            if i < 9:
                print(str(i) + ".  Name: " + row[0] + "\n    Artist: " + row[1] + "\n    Album: " + row[2]
                      + "\n    Year: " + str(row[3]) + "\n    Rank: " + str(row[4]) + "\n")
            else:
                print(str(i) + ". Name: " + row[0] + "\n    Artist: " + row[1] + "\n    Album: " + row[2]
                      + "\n    Year: " + str(row[3]) + "\n    Rank: " + str(row[4]) + "\n")
            # Increment i by 1
            i += 1
    else:
        print("The file is empty\n")
    return filename

# This function writes the data stored in the items_list to a new file
def write_items(item_list, filename):
    # Prompt the user for a filename to write the data of the item_list to
    name = input("Enter the new file name you wish to store the contents listed above to without extension"
                 "(E.g., newFile): ")
    # Add the .csv extension to the name variable, so that it can be written to
    name = name + ".csv"
    # Check if the new name provided by the user is not the same as the file we read the data from
    if not os.path.exists(name):
        # Open the file for writing
        file = open(name, 'w', newline='')
        with file:
            write = csv.writer(file)
            write.writerows(item_list)
    # If the name is same, print an error message and call the
    # write_items function recursively
    else:
        print("This file already exists. Please use a different name\n")
        write_items(item_list, filename)


def remove_file(filename):
    while True:
        name = input("Please enter the name of the file you want to remove, if you wish to view the files, enter view: ")
        if name == "view" or name == "VIEW":
            list_csv_files()
        else:
            if name == filename:
                print("This is the original file, please enter a new file name: ")
            else:
                os.remove(name)
                break


def list_csv_files():
    file_list = [f for f in os.listdir('.') if os.path.isfile(os.path.join('.', f)) and f.endswith('.csv')]
    for i in file_list:
        print("File: " + i + "\n")


def exit_program():
    sys.exit()


# Main function
def main():
    while True:
        filename = "hanand.csv"
        choice = int(input("Welcome to the CSV file program. Please Select one of the following\n1. Display Contents of the file\n2. List all the"
            " .Csv files\n3 Write content to a new file\n 4. Remove a file\n5. Exit Program\n"))
        if choice == 1:
            filename = Display_items()
        elif choice == 2:
            list_csv_files()
        elif choice == 3:
            remove_file(filename)
        elif choice == 4:
            write_items()
        elif choice == 5:
            exit_program()


# Run the main function
if __name__ == '__main__':
    main()
