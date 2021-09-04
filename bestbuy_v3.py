"""Assembled Program Best-Buy 3
add C6 to best-buy 2
created by Wen-Qi Toh
1/9/21"""


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
            valid = True    # breaks out of valid loop bc now valid = True bc there is a response, not empty
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


# main routine
# get budget amount - component 1
budget = num_check("What is your budget? (must be higher than $5): ")
# get category and unit - component 2
category = not_blank("What is your product category? ")
print("Your product category is {}.".format(category))
unit = not_blank("What is your product unit? ")
print("Your product unit for {} is {}.".format(category, unit))

# component 7
# lists and variables
unit_price_list = []
product_info = []
name_unit_price = []

valid_list = False
error_msg = "ERROR: you have entered your product information incorrectly. " \
            "Please try again, using commas to separate product information."

while not valid_list:
    # calling not blank function and providing question
    products = input("Please enter product mass, name, then price - please"
                         " separate using commas. (or enter 'X' to exit): ")\
                        .capitalize()

    if products != "X":
        products = products.split(",")
        print(products)
        for line in products:
            try:
                mass = single_num_check(products[0])
                products.remove(products[0])
                price = single_num_check(products[-1])
                products.remove(products[-1])
                name = " ".join([str(word) for word in products])
                # testing if user entered the numbers correctly
                # if both num are entered incorrectly
                if price == 0.0 and mass == 0.0:
                    unit_price = 0.0
                    print(unit_price)
                    print(error_msg)
                # if one num is entered incorrectly
                elif price == 0.0 or mass == 0.0:
                    unit_price = 0.0
                    print(unit_price)
                    print(error_msg)
                else:
                    unit_price = round(price / mass, 2)
                    product_info.append([mass, name, price, unit_price])
                    name_unit_price.append([name, unit_price])
                    print(name_unit_price)
                    unit_price_list.append(unit_price)
                    print(unit_price_list)

            except IndexError:
                print(error_msg)
    # making sure list has at least 2 products to compare
    elif len(product_info) < 2:
        print("ERROR: Please enter at least 2 products to compare.")
    else:
        valid_list = True   # break out of loop if list contains 2+ items
        print("\nYou have chosen to end the product loop. Product unit prices"
              " as follows:\n")
        break

# Final outputs
print("Product list: {}".format(product_info))
print("Unit price list: {}".format(unit_price_list))

count = 0
total_unit_price = 0.0
cheapest = []
costliest = []
for item in product_info:
    print(f"The unit price of {item[1]} is ${item[2]}/{item[0]} = {round(item[3],4)}")
    count += 1
    total_unit_price += round(item[3], 4)

# component 5
# this line account for an empty list OR a lower price
    if not cheapest or item[2] < cheapest[0]:
        cheapest = [item[2]]

    elif item[2] == cheapest[0]:
        cheapest.append(item[2])

# this line account for an empty list OR a higher price
    elif not costliest or item[2] > costliest[0]:
        costliest = [item[2]]

    elif item[2] == costliest[0]:
        costliest.append(item[2])

av_unit_price = sum(unit_price_list) / len(unit_price_list)
print("Average unit price: ${}".format(round(av_unit_price, 2)))

# display min/max
print(f"cheapest: {cheapest}")
print(f"costliest: {costliest}")

# component 6 - best buy recommendation
best_buy = []
print("Your budget is ${}".format(budget))
for product in product_info:
    if product[2] > 5:  # step 1
        product_info.remove(product)
        unit_price_list.remove(product[3])

        print("The product '{}' has been removed from product list as "
              "the price exceeds the budget.".format(product[1]))

    elif product[2] <= 5:   # step 2
        print("product {} accepted".format(product[1]))
        if product[3] < min(unit_price_list):
            best_buy = product
            print("if {}".format(best_buy))
        elif product[3] == min(unit_price_list):
            best_buy.append(product)
            print("product {} accepted".format(product[1]))
            print("best buy so far: {}".format(best_buy))

# final output
print("\nThe recommended best buy/s for you is: {}".format(best_buy))
