"""Component 7 v3 - allowing product name, mass/volume, and price to be entered
on one line by user - more accessible/functional
v3 = improving on v2
Created by Wen-Qi Toh
16/8/21"""


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
        except ValueError or IndexError:
            return None


# main routine
unit_price_list = []
product_info = []
valid_list = False
while not valid_list:
    # calling not blank function and providing question
    products = not_blank("Please enter product mass, name, then price - "
                         "separated by commas. (or enter 'X' to exit): ")\
                        .capitalize()

    if products != "X":
        products = products.split(",")
        print(products)
        if products == IndexError:
            print("Error - Index Error. Try again.")
        for line in products:
            price = single_num_check(products[-1])
            products.remove(products[-1])
            print(price)

            mass = single_num_check(products[0])
            products.remove(products[0])
            print(mass)
            name = " ".join(products)
            print(name)

            if price is None:
                unit_price = None
                print(unit_price)
                print("Error in entering mass/price. Try again."
                      " Please enter number value.")
            elif mass is None:
                unit_price = None
                print(unit_price)
                print("Error in entering mass/price. Try again."
                      " Please enter number value.")
            elif price and mass is None:
                unit_price = None
                print(unit_price)
                print("Error in entering mass/price. Try again."
                      " Please enter number value.")
            else:
                unit_price = round(price / mass, 2)
                product_info.append([mass, name, price, unit_price])
                unit_price_list.append(unit_price)
                print(unit_price)

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
    total_unit_price += round(item[3],4)
av_unit_price = sum(unit_price_list) / len(unit_price_list)
print("Average unit price: ${}".format(round(av_unit_price, 2)))
