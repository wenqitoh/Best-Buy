"""Assembled Program Best-Buy 5 final program
post usability testing - improvements based on feedback
editing, removing unnecessary lines of code
created by Wen-Qi Toh
5/9/21"""


# functions
# number checking function
def num_check(question):
    error = "You must enter a number, greater or equal to 5."
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
    error = "ERROR: Your category/unit is blank or has a number in it! " \
            "Please try again."
    valid = False   # to create loop

    while not valid:    # while valid still = false
        number = False  # assumption that name contains no digits - initially
        response = input(question)

        for letter in response:  # Check for digits in response-category/input
            if letter.isdigit():  # Tests for True - by default
                number = True  # sets true if any digit found
        # Generate error for blank name or digit
        if not response or number is True:
            print(error)

        else:  # no error found
            return response


# checking one number func
def single_num_check(test):
    number = ""
    while not number:
        try:
            number = float(test)
            return number
        except ValueError:
            return 0.0


# to print list info out nicely
def list_output(a_list):
    for s in a_list:
        print(" | ".join(str(e) for e in s))


def instructions():
    print("\n* * * * * * * * * * INSTRUCTIONS * * * * * * * * * *\n")
    print("* This program finds the unit price of your products, the cheapest "
          "and costliest products,\nand recommends a best buy from the "
          "products you've entered *")
    print(" - This program will ask for your budget, and will calculate the"
          " best buy based off the budget.")
    print(" - The product will also ask you to enter your product information"
          " line by line.\nPlease ensure that you enter your "
          "product information on one line\nas mass, name, price, separated "
          "by forward slashes (eg. 250/pr1/12.5).")
    print(" - If you make an error while entering your information, an error"
          " message will appear,\n and you can try enter the information again"
          " correctly.")
    print(" !!! Remember to read the prompts carefully before typing :) !!!\n")


# main routine
# providing option for new user to get instructions
print("* * * * * * * * * * Welcome to the Best Buy Program! * * * * *"
      " * * * * *\n")
get_instructions = input("Press <enter> to get instructions, or any other key "
                         "+ <enter>\n if you are familiar with this program: ")
if not get_instructions:
    instructions()
else:
    print()

# component 1 - get budget amount
budget = num_check("What is your budget? (must be higher than or equal "
                   "to $5): $")
print("Your budget is ${}.".format(budget))
# component 2 - get category and unit
category = not_blank("What is your product category? (eg. cheese, meat, "
                     "etc.): ")
print("Your product category is {}.".format(category))
unit = not_blank("What is your product unit? (eg. pounds, ml, grams, etc.): ")
print("Your product unit for {} is {}.".format(category, unit))

# component 7 - get product info, split, get unit price and av. UP
# lists and variables
product_info = []
line_num = 1
valid_list = False
error_msg = "\nERROR: You have entered your product information incorrectly." \
            "\nPlease try again, using a forward slash ('/') to " \
            "separate your product\ninformation of mass, name, price " \
             "(with mass and price as numbers)."

while not valid_list:
    # calling not blank function and providing question
    products = input("\nPlease enter the product's 'mass/name/price' in that "
                     "exact format on the line below\n- separate product info"
                     " using a forward slash ('/').\nEnter 'X' + <enter> to "
                     "exit.\nProduct info {}: ".format(line_num)).capitalize()

    if products != "X":
        products = products.split("/")

        for line in products:
            try:    # splitting product info into their diff. variables
                mass = single_num_check(products[0])
                products.remove(products[0])
                price = single_num_check(products[-1])
                products.remove(products[-1])
                name = " ".join([str(word) for word in products])
                # testing if user entered the numbers correctly
                # if both num are entered incorrectly
                if price == 0.0 and mass == 0.0:
                    unit_price = 0.0
                    print(error_msg)
                # if one num is entered incorrectly
                elif price == 0.0 or mass == 0.0:
                    unit_price = 0.0
                    print(error_msg)
                elif name == "":
                    unit_price = 0.0
                    print(error_msg)
                else:
                    unit_price = round(price / mass, 4)
                    line_num = line_num + 1
                    product_info.append([mass, name, price, unit_price])
                    print("\n* Product added to product list! *")
            except IndexError:
                print(error_msg)
    # making sure list has at least 2 products to compare
    elif len(product_info) < 2:
        print("\nERROR: Please enter at least 2 products to compare.")
    else:
        valid_list = True   # break out of loop if list contains 2+ items
        print("\n* * * * * * * * END PROGRAM * * * * * * * *")
        print("\nYou have chosen to end the product loop. Below is the "
              "product list,\nunit price list, cheapest & costliest product/s,"
              " and the recommended best buy.\n")
        break

# Final outputs
# variables and lists
count = 0
total_unit_price = 0.0
cheapest = []
costliest = []

print("* * * * PRODUCT LIST:")
print("(read the following information as: mass({})| product name | price($)| "
      "unit price($))".format(unit))
list_output(product_info)

print("\n* * * UNIT PRICE LIST:")
print("(Unit prices are calculated by price divided by mass)")
# print out unit prices
for item in product_info:
    print(f"The unit price of {item[1]} is ${item[2]}/{item[0]} = $"
          f"{round(item[3],4)}")
    count += 1
    total_unit_price += round(item[3], 4)

# component 5 - revised
    # this line account for an empty list OR a lower price
    if not cheapest or item[2] < cheapest[0][1]:
        cheapest = [(item[1], item[2])]
    elif item[2] == cheapest[0][1]:
        cheapest.append((item[1], item[2]))
    # this line account for an empty list OR a higher price
    if not costliest or item[2] > costliest[0][1]:
        costliest = [(item[1], item[2])]
    elif item[2] == costliest[0][1]:
        costliest.append((item[1], item[2]))

# display min/max
print("\n* * CHEAPEST PRODUCT (product name | price($)):")
list_output(cheapest)
print("\n* * COSTLIEST PRODUCT (product name | price($)):")
list_output(costliest)

# component 6 - best buy recommendation
best_buy = []
new_product_list = []
# reprint budget for user
print("\n* Your budget entered was ${} *".format(budget))

for product in product_info:
    if product[2] > budget:  # remove over budget products
        print("\n - Product '{}' exceeded budget.".format(product[1]))
    elif product[2] <= budget:   # add within budget products to new list
        new_product_list.append(product)

for new_product in new_product_list:
    # this line account for an empty list OR a lower price
    if not best_buy or new_product[3] < best_buy[0][3]:
        best_buy = [new_product]
    elif new_product[3] == best_buy[0][3]:
        best_buy.append(new_product)

print("\nThe recommended best buy for the category of {},"
      " measured in {} is:".format(category, unit))
print("(read the following information as: mass({})| product name | price($)| "
      "unit price($))\n".format(unit))

print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
list_output(best_buy)
print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * ")

if not best_buy:
    best_buy = ["No best buy :("]
    print(*best_buy, sep=", ")

# msg for multiple best buys
if len(best_buy) > 1:
    print("\nWARNING: The best buy has been calculated based off the product "
          "price and the lowest\nunit price, so it is possible to have "
          "multiple recommended best buys, like now.\nThe products above are "
          "within your budget and are the most 'worth it'.")

print("\nThank you for playing!")
