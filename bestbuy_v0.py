"""Assembled Program Best-Buy v0 - combine component 1 & 2
(get budget & category & unit)
v0 combines the 2 smallest components to make it easier to add to program
Created by Wen-Qi Toh
4/9/21"""


# functions
# number checking function
def num_check(question):
    error = "You must enter in a number. " \
            "(if entering budget, must be greater than 5.)"
    valid = False
    while not valid:
        try:
            response = float(input(question))
            if response < 5:
                print(error)
            else:
                return response
        except ValueError:
            print(error)


# checking for blanks function
def not_blank(question):
    error = "ERROR: Your category/unit is blank or has a number in it! Please try again."
    valid = False   # to create loop

    while not valid:    # while valid still = false
        number = False  # assumption that name contains no digits - initially
        response = input(question)

        for letter in response:  # Check for digits in response - category/input
            if letter.isdigit():  # Tests for True - by default
                number = True  # sets true if any digit found

        if not response or number == True:  # Generate error for blank name or digit
            print(error)

        else:  # no error found
            valid = True    # breaks out of valid loop bc now...
            return response # ...valid = True bc there is a response, not empty


# main routine
# get budget amount
budget = num_check("What is your budget? (must be higher than $5): ")
# get category and unit
category = not_blank("What is your product category? ")
print("Your product category is {}.".format(category))
unit = not_blank("What is your product unit? ")
print("Your product unit for {} is {}.".format(category, unit))

