#!/usr/bin/env python3
# Copyright 2020
# Written by Hardik Anand


# This function displays all the movies stored in the movie_list.
def list(movie_list):
    # Checks if the length of the movie_list = 0, then it prints out that there are no movies stored
    if len(movie_list) == 0:
        print("There are no movies in the list.\n")
        return
    else:
        # Declare i as 1, so that we can use it later on to print the movie number in the for loop,
        # by incrementing i after each iteration
        i = 1
        for row in movie_list:
            # Prints out all the movie stored in movie_list, by declaring row as variable in the list,
            # which will iterate through every row in the list and print out the respective values from respective
            # fields. For e.g., over here name is index 0, in the row of the list, year is index 1, price is index 2
            # and rating is index 3
            print(str(i) + ". Name: " + row[0] + "\n   Year: " + str(row[1]) + "\n   Price: $" + str(
                row[2]) + "\n   Rating: " + str(row[3]))
            print()
            i += 1


# This function lets the user add a movie to the movie list (Note that the added movie from this function will only
# be in the memory, until the program is being run).
def add(movie_list):
    # Take input from the user for name
    name = input("Name: ")

    # execute loop until condition is met
    while True:
        year = input("Year: ")
        year_len = len(year)
        # Checks if the input for year contains only numbers
        if not year.isdigit():
            # Display error message if year does not contain only digits
            print("Please enter a number (E.g., 1997, 2019)")
        # Checks if the there are 4 digits in the year
        elif not year_len == 4:
            # Display error message
            print("Please enter a valid year (E.g., 1997, 2019)")
        else:
            # Breaks out of loop and converts year to an int
            year = int(year)
            break

    # execute loop until condition is met
    while True:
        price = input("Price: ")
        # Checks if the input is of type float
        try:
            float(price)
            break
        # Display error message if not of type float
        except:
            print("Please enter a valid value (Possibly a float or an int)")

    # execute loop until condition is met
    while True:
        rating = input("Rating: ")
        # Checks if the rating is a digit
        if rating.isdigit():
            # Displays error message if condition is true
            print("Please enter a valid rating (E.g., G, PG, R)")
        else:
            # Break out of loop if the rating does not contain any digits
            break

    # Create list movie and add items to it
    movie = []
    movie.append(name)
    movie.append(year)
    movie.append(price)
    # Convert the rating to uppercase for better appearance
    movie.append(rating.upper())
    # Add the list we just created to the movie_list (Parameter of this function)
    movie_list.append(movie)
    # Print out that the 'name of the movie' was added
    print(movie[0] + " was added.\n")


# This function deletes a specific movie's information by asking
# the user for the movie number
def delete(movie_list):
    # execute loop until condition is met
    while True:
        # Take input
        number = input("Number: ")
        # Check if number is not a digit
        if not number.isdigit():
            # Display error message
            print("Please enter a Number")
        else:
            # Convert number to an integer
            number = int(number)
            # Check if number is less than 1 or more than the length of the movie_list
            if number < 1 or number > len(movie_list):
                # Display error message
                print("Invalid movie number.\n")
            else:
                # Use the pop functionality to remove the movie from movie_list
                # We use number - 1, because that is how data is stored in the movie_list.
                # For e.g., when we display the movies we start from 1, instead of 0
                # so that it looks appealing, but the data stored in the movie_list, starts
                # from 0 instead of 1.
                movie = movie_list.pop(number - 1)
                # Print that the 'name of the movie' was deleted
                print(movie[0] + " was deleted.\n")
                break


# This function finds all the movies and displays them using
# the user's input of the rating.
def find_movie(movie_list, rating):
    # Declare i as 1, so that we can use it later on to print the movie number in the for loop,
    # by incrementing i after each match
    i = 1
    print("Movies with the Rating " + rating + ":")
    for row in movie_list:
        # We check if the rating provided by the user matches the rating stored in the movie_list
        if row[3] == rating:
            # Prints out all the movie stored in movie_list, which match the rating provided by the user
            print(str(i) + ". Name: " + row[0] + "\n   Year: " + str(row[1]) + "\n   Price: $" + str(row[2]))
            # Increment i after each match
            i += 1
    # Display a blank line for better appearance
    print()


# This function displays the menu
def display_menu():
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("find - Find a movie by rating")
    print("exit - Exit program")
    print()


# Main function
def main():
    # Declare the movie_list
    movie_list = [["Monty Python and the Holy Grail", 1975, 10.5, "R"],
                  ["On the Waterfront", 1954, 11, "R"],
                  ["Cat on a Hot Tin Roof", 1958, 10, "PG"]]

    while True:
        display_menu()
        command = input("Command: ")
        if command == "list":
            print()
            list(movie_list)
        elif command == "add":
            print()
            add(movie_list)
        elif command == "del":
            print()
            delete(movie_list)
        elif command == "find":
            print()
            rating = input("Enter the rating: ")
            find_movie(movie_list, rating)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")


if __name__ == "__main__":
    main()
