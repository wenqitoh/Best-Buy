""" Component 1 v1 - get budget amount
created by Wen-Qi Toh
3/8/21"""

# main routine
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
