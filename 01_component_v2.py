"""Component 1 v2 - change get budget amount into num checker function
using a try/except loop
created by Wen-Qi Toh
3/8/21"""


# number checking function
def num_checker(question):
    error = "You must enter in a number greater than 5."
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


# main routine
# get budget amount
budget = num_checker("What is your budget? (must be higher than $5): ")
