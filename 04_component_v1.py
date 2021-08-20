"""Component 4 v1 - Calculate product unit price and average unit price ($/m)
by making a mass list, price list and adding for loop.
Created by Wen-Qi Toh
11/8/21"""


def not_blank(question):
    error = "ERROR: Please enter in the name of your product (cannot be blank)"
    valid = False   # to create loop

    while not valid:
        response = input(question)

        if not response:  # checks if product name has been entered
            print(error)
        else:  # no error found
            return response


# int check function to check product mass is number,
# also acting as not blank, taken from recipe moderniser 3 v3

def num_check(question):
    error = "You must enter a number, and must be more than 0"
    valid = False
    while not valid:
        try:
            response = float(input(question))
            if response <= 0:
                print(error)
            else:
                return response
        except ValueError:
            print(error)


# main routine
catalogue = []
mass_list = []
price_list = []

valid_list = False

while not valid_list:
    # calling not blank function and providing question
    name = not_blank("Please enter product name and enter 'X' to exit: ")\
                        .capitalize()

    product_information = []   # create blank product list
    unit_price_list = []

    if name != "X":
        # adding name to product info list if no exit code
        product_information.append(name)
        mass = num_check("What is your product mass? ")
        product_information.append(mass)
        mass_list.append(mass)
        price = num_check("What is your product price? ")
        product_information.append(price)
        price_list.append(price)

        catalogue.append(product_information)
    else:
        # making sure list has at least 2 products to compare
        if len(catalogue) < 2:
            print("ERROR: Please enter at least 2 products to compare.")
        else:
            valid_list = True   # break out of loop if list contains 2+ items
            # user receipt
            print("Here are your products: \n{}".format(catalogue))
            print()

        # for loop to reference each sublist and their contents in catalogue
            for row in catalogue:
                name2 = row[0]
                mass2 = row[1]
                price2 = row[2]

                # calculating unit price per product
                product_unit_price = round(price2 / mass2, 2)
                print("Product individual unit price for {}: ${}"
                      .format(name2, product_unit_price))

            # adding the unit ppp number to unit price list to print 2gether
                unit_price_list.append(product_unit_price)
            print()
            print("Product unit price list: {}".format(unit_price_list))

            av_unit_price = sum(unit_price_list) / len(unit_price_list)
            print("Average unit price: ${}".format(round(av_unit_price, 2)))
