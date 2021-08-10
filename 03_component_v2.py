"""Component 3 v2 - get list of products and mass/volume and price - storing
in a list - till user enters X then output
Created by Wen-Qi Toh
10/8/21"""


def not_blank(question):
    error = "ERROR: Please enter in the name of your product (cannot be blank)"
    valid = False   # to create loop

    while not valid:
        response = input(question)

        if not response:  # checks if product name has been entered
            print(error)
        else:  # no error found
            return response


# int check function to check product mass & price is number,
# also acting as not blank, taken from Best-Buy component 1 v2
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
catalogue = []  # list to put product info list into, so that information is
                # grouped by the products, and each different product+info
                # is in its own nested list

valid_list = False  # loop
while not valid_list:
    name = not_blank("Please enter product name and enter 'X' to exit: ")\
                        .capitalize()    # checking name input is not blank

    product_information = []   # create blank product list

    if name != "X":
        # adding name to product info list if no exit code
        product_information.append(name)
        # adding mass to product info list if it passes num_check func
        mass = num_check("What is your product mass? ")
        product_information.append(mass)
        # adding price to product info list if it passes num_check func
        price = num_check("What is your product price? ")
        product_information.append(price)
        # adding product info list to catalogue to become a nested list,
        # stored with all the other separate product infos
        catalogue.append(product_information)
    else:
        # making sure list has at least 2 products to compare
        if len(catalogue) < 2:
            print("ERROR: Please enter at least 2 products to compare.")
        else:
            valid_list = True   # break out of loop if list contains 2+ items
            print("Here are your products: \n{}".format(catalogue))
