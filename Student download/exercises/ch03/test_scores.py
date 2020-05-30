#!/usr/bin/env python3

# display a welcome message
print("The Test Scores program")

# initialize variables
choice = ''

while choice != 'n':
    # initialize variables insider outer for loop
    test_score = ''
    counter = 0
    score_total = 0
    average_score = 0
    # display a welcome message's part 2
    print()
    print("Enter test scores")
    print("Enter 'end' to end input")
    print("======================")
    while test_score != 'end':
        test_score = input("Enter test score: ")
        # break inner loop if test_score is "end"
        if test_score == 'end':
            print("======================")
            print("Total Score:", score_total,
                  "\nAverage Score:", average_score)
            print()
            choice = input("Enter another set of scores (y/n)?")
            # redo outer for loop if choice is y
            if choice == 'y':
                break
            # break out of every loop if choice is n and print "Bye"
            else:
                print()
                print("Bye")
                break
        else:
            t_score = int(test_score)
            if t_score >= 0 and t_score <= 100:
                score_total += t_score
                counter += 1
                average_score = round(score_total / counter)
            else:
                print("Test score must be from 0 through 100. Score discarded. Try again.")

                


