"""Component 7 v4 - allowing product name, mass/volume, and price to be entered
on one line by user
version 4 = split var. products by ',' not ' '.
debug code, if any errors when user enters info, print error msg and re-loop q.
use try/except loop to account for error of not using commas when entering info
31/8/21"""


# functions
def not_blank(question):
    error = "ERROR: Please enter in the name of your product (cannot be blank)"
    valid = False   # to create loop

    while not valid:
        response = input(question)

        if not response:  # checks if product name has been entered
            print(error)
        else:  # no error found
            return response


def single_num_check(test):
    number = ""
    while not number:
        try:
            number = float(test)
            return number
        except ValueError:
            return 0.0


# main routine
unit_price_list = []
product_info = []
error_msg = "ERROR: you have entered your product information incorrectly. " \
            "Please try again, using commas to separate product information."
valid_list = False
while not valid_list:
    # calling not blank function and providing question
    products = not_blank("Please enter product mass, name, then price - please"
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
                    unit_price_list.append(unit_price)
                    print(unit_price)
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

for item in product_info:
    print(f"The unit price of {item[1]} is ${item[2]}/{item[0]} = {round(item[3],4)}")
    count += 1
    total_unit_price += round(item[3], 4)
av_unit_price = sum(unit_price_list) / len(unit_price_list)
print("Average unit price: ${}".format(round(av_unit_price, 2)))
