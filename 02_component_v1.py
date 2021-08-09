""" Component 2 v1 - get category and unit name, produce error message if
category/unit is blank or number
Created by Wen-Qi Toh
8/8/21"""

category = str(input("What is your product category? "))
unit = str(input("What is your product unit? "))
error = "Your category/unit is blank or has a number in it! Please try again."

contains_number = False

for letter in category:
    if letter.isdigit():
        contains_number = True
# print error message if category name has digits/blank
if not category or contains_number:
    print(error)


for letter in unit:
    if letter.isdigit():
        contains_number = True

# print error message if unit name has digits/blank
if not unit or contains_number:
    print(error)
