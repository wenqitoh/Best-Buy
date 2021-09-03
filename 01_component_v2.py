"""Component 1 v2 - continuing with method 2 from v1 (try-except loop)
change get budget amount into num checker function so it can be reused later
with other components
created by Wen-Qi Toh
3/8/21"""


# number checking function
def num_check(question):
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
budget = num_check("What is your budget? (must be higher than $5): ")
