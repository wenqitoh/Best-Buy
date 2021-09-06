"""Assembled Program Best-Buy 4
improving readability
created by Wen-Qi Toh
5/9/21"""


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
        if not response or number == True:
            print(error)

        else:  # no error found
            valid = True
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


def list_output(list):
    for s in list:
        print(" - ".join(str(e) for e in s))

def instructions():
    print("\n* * * * * * * * * * INSTRUCTIONS * * * * * * * * * *\n")
    print("This program finds the unit price of your products, the cheapest "
          "and costliest products,\nand recommends a best buy from the products"
          " you've entered.")
    print(" - This program will ask for your budget, and will calculate the"
          " best buy based off the budget.")
    print(" - The product will also ask you to enter your product information"
          " line by line.\nPlease ensure that you enter your "
          "product information on one line\nas mass, name, price, separated "
          "by commas (eg. 250, pr1, 12.5).")
    print(" - If you make an error while entering your information, an error"
          " message will appear,\nand you can try enter the information "
          "correctly again.\n")


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

# get budget amount - component 1
budget = num_check("What is your budget? (must be higher than or equal "
                   "to $5): ")
# get category and unit - component 2
category = not_blank("What is your product category? ")
print("Your product category is {}.".format(category))
unit = not_blank("What is your product unit? ")
print("Your product unit for {} is {}.".format(category, unit))

# component 7
# lists and variables
unit_price_list = []
product_info = []

line_num = 1
valid_list = False
error_msg = "ERROR: you have entered your product information incorrectly. " \
            "Please try again, using commas to separate product information.\n"

while not valid_list:
    # calling not blank function and providing question
    products = input("Please enter product mass, name, then price - please"
                     " separate using commas. (or enter 'X' to exit)\n"
                     "Product info {}: ".format(line_num))

    if products != "X":
        products = products.split(",")

        for line in products:
            try:    # splitting product info into their diff. variables
                mass = single_num_check(products[0])
                products.remove(products[0])
                price = single_num_check(products[-1])
                products.remove(products[-1])
                name = " ".join([str(word) for word in products])
                # testing if user entered the numbers correctly
                # if both num are entered incorrectly
                if len(products) != 1:
                    unit_price = 0.0
                    print(error_msg)
                elif price == 0.0 and mass == 0.0:
                    unit_price = 0.0
                    print(error_msg)
                # if one num is entered incorrectly
                elif price == 0.0 or mass == 0.0:
                    unit_price = 0.0
                    print(error_msg)
                else:
                    unit_price = round(price / mass, 2)
                    line_num = line_num + 1
                    product_info.append([mass, name, price, unit_price])
                    unit_price_list.append(unit_price)
                    print("Product added to product list!\n")
            except IndexError:
                print(error_msg)
    # making sure list has at least 2 products to compare
    elif len(product_info) < 2:
        print("ERROR: Please enter at least 2 products to compare.")
    else:
        valid_list = True   # break out of loop if list contains 2+ items
        print("* * * * * * * * END PROGRAM * * * * * * * *")
        print("\nYou have chosen to end the product loop. Product unit prices"
              " as follows:\n")
        break

# Final outputs
print("Product list:")
list_output(product_info)

count = 0
total_unit_price = 0.0
cheapest = []
costliest = []
print("\nUnit prices per product:")
for item in product_info:
    print(f"The unit price of {item[1]} is ${item[2]}/{item[0]} = "
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
print("\ncheapest product:")
list_output(cheapest)
print("costliest product:")
list_output(costliest)

# component 6 - best buy recommendation
best_buy = []
print("\n* * * Your budget is ${} * * *\n".format(budget))

new_product_list = []
new_upl = []

for product in product_info:
    if product[2] > budget:  # step 1
        # product_list.remove(product)
        print("The product '{}' has been removed from product list as "
              "the price exceeds the budget.".format(product[1]))

    elif product[2] <= budget:   # step 2
        new_product_list.append(product)
        new_upl.append(product[3])

for new_product in new_product_list:
    # this line account for an empty list OR a lower price
    if not best_buy or new_product[3] < best_buy[0][3]:
        best_buy = [new_product]
    elif new_product[3] == best_buy[0][3]:
        best_buy.append(new_product)

print("\nThe recommended best buy/s for measured in {} you is:".format(unit))
list_output(best_buy)
