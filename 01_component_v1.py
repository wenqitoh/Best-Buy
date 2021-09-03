""" Component 1 v1 - get budget amount (2 methods)
created by Wen-Qi Toh
3/8/21"""

# main routine - Method 1
budget = input("What is your budget? (you must have at least $5 or more): ")
# error message - if budget is blank or has letters
error = "Your budget is blank! Please try again."

# check each character in the budget for letters
contains_letter = False
# if budget has letters:
if budget.isalpha():
    contains_letter = True
elif int(budget) < 5:
    print(error)

# print error message if budget has letters
if not budget or contains_letter:
    print(error)


# main routine - Method 2
# error message - if budget is blank or has letters
error = "Your budget is blank! Please try again."

# set up while loop
contains_letter = False
while not contains_letter:
    try:    # try-except loop for errors
        response = int(input("What is your budget? (you must have at least $5 or more): "))
        if response < 5:
            print(error)
        else:
            print(response) # print response if >=5
    except ValueError:
        print(error)
