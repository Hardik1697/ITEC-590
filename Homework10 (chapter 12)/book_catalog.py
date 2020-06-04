#!/usr/bin/env python3
# Copyright 2020
# Written By Hardik Anand

def show_book(book_catalog):
    title = input("Title: ")
    if title in book_catalog:
        book = book_catalog[title]
        print("Title:    " + title)
        print("Author:   " + book["author"])
        print("Pub year: " + book["pubyear"])
    else:
        print("Sorry, " + title + " doesn't exist in the catalog.")

def add_edit_book(book_catalog, mode):
    title = input("Title: ")
    if mode == "add" and title in book_catalog:
        print(title + " already exists in the catalog.")
        response = input ("Would you like to edit it? (y/n): ").lower()
        if(response != "y"):
            return
    elif mode == "edit" and title not in book_catalog:
        print(title + " doesn't exist in the catalog.")
        response = input("Would you like to add it? (y/n): ").lower()
        if (response != "y"):
            return

    author = input("Author name: ")
    pubyear = input("Publication year: ")
    
    # Create a dictionary for the book data
    book = {"author": author,
            "pubyear": pubyear}

    # Add the book data to the catalog using title as key
    book_catalog[title] = book

def delete_book(book_catalog):
    title = input("Title: ")
    if title in book_catalog:
        del book_catalog[title]
        print(title + " removed from catalog.")
    else:
        print(title + " doesn't exist in the catalog.")


def display(books):
    j = 1
    print()
    for i in books:
        book = books[i]
        print("Book " + str(j) + ":")
        print("Title:    " + str(i))
        print("Author:   " + book["author"])
        print("Pub year: " + book["pubyear"])
        print()
        j += 1


def count(books):
    j = 0
    for i in books:
        j += 1
    print("\nThe number of Books in this dictionary is/are: " + str(j))


def display_menu():
    print("The Book Catalog program")
    print()
    print("COMMAND MENU")
    print("disp - Displays all books")
    print("count - Counts all the books")
    print("show - Show book info")
    print("add -  Add book")
    print("edit - Edit book")
    print("del -  Delete book")
    print("exit - Exit program")

def main():
    display_menu()
    book_catalog = {
        "Moby Dick":
            {"author" : "Herman Melville",
             "pubyear" : "1851"},
        "The Hobbit":
            {"author" : "J. R. R. Tolkien",
             "pubyear" : "1937"},
        "Slaughterhouse Five":
            {"author" : "Kurt Vonnegut",
             "pubyear" : "1969"}
        }
    while True:
        print()
        command = input("Command: ").lower()
        if command == "show":
            show_book(book_catalog)
        elif command == "disp":
            display(book_catalog)
        elif command == "count":
            count(book_catalog)
        elif command == "add":
            add_edit_book(book_catalog, mode="add")
        elif command == "edit":
            add_edit_book(book_catalog, mode="edit")
        elif command == "del":
            delete_book(book_catalog)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
