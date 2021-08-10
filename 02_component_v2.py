""" Component 2 v2 - turn into loop, create function to check not blank
Created by Wen-Qi Toh
8/8/21"""


# not blank function
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
            valid = True    # breaks out of valid loop bc now valid = True bc there is a response, not empty
            return response


# main routine
category = not_blank("What is your product category? ")
print("Your product category is {}.\n".format(category))
unit = not_blank("What is your product unit? ")
print("Your product unit is {}.".format(unit))
