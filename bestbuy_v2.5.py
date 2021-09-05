"""Assembled Program Best-Buy 2.5
add revised C5 to best-buy 1
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
print("cheapest product:")
for s in cheapest:
    print(", ".join(str(e) for e in s))
print("\ncostliest product:")
for s in costliest:
    print(", ".join(str(e) for e in s))


