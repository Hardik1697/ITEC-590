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
    # Prompt the user for filename
    filename = input("\nEnter the name of the csv file without extension (E.g., filenname): ")
    # Add the .csv extension to the name variable, so that it can be written to
    filename = filename + ".csv"
    # Call the read_items function on contents to store the data from the file into contents
    contents = read_items(filename)
    # Check if contents is not of type None (If nothing was read from the file,
    # or the file was not found)
    if not contents is None:
        print("\nDisplaying contents from " + filename)
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
        print("There is nothing to display here\n")
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
                with file:
                    write = csv.writer(file)
                    write.writerows(item_list)
                print("\nDone! The contents from " + filename + " were written to " + name + "\n")
            # Catch and print the exception
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
    name = input("\nPlease enter the name of the file you want to remove without extenstion"
                 "(E.g., filename): ")
    name = name + ".csv"
    # If the file exists, remove it
    if os.path.exists(name):
        os.remove(name)
        print("\nDone! " + name + " was removed\n")
    # If not, print error message
    else:
        print("\nThis File does not exist. Please try again\n")


# This function lists all the .Csv files in the working directory
def list_csv_files():
    # Add the .Csv files to the file_list list
    file_list = [f for f in os.listdir('.') if os.path.isfile(os.path.join('.', f)) and f.endswith('.csv')]
    j = 1
    print()
    for i in file_list:
        print(str(j) + ". " + i)
        j += 1
    print()


# This function is used to terminate the program
def exit_program():
    print("\nTerminating Process...")
    sys.exit()


# Main function
def main():
    # Declare items as None and name as an empty string
    # This will be used for some error checking by the functions later in the while loop
    items = None
    name = ""
    # Execute loop till exit_program is called
    while True:
        choice = int(input(
            "Welcome to the CSV file program. Please Select one of the following\n1. Display Contents of the file\n2. "
            "List all the .Csv files\n3. Write content to a new file\n4. Remove a file\n5. Exit Program\n"))
        # Call the Display_items function if choice is 1
        if choice == 1:
            # Use items and name (variables defined above while loop) to assign them values
            # from the Display_items function
            [items, name] = Display_items()
        # Call the list_items function if choice is 2
        elif choice == 2:
            list_csv_files()
        # Call the write_items function if choice is 3
        elif choice == 3:
            write_items(items, name)
        # Call the remove_file function if choice is 4
        elif choice == 4:
            remove_file()
        # Call the exit_program function if choice is 5
        elif choice == 5:
            exit_program()
        else:
            print("\nThis is not a valid option, please try again...\n")


# Run the main function
if __name__ == '__main__':
    main()
