"""Component 7 v2 - allowing product name, mass/volume, and price to be entered
on one line by user
version 2 = allow for user input errors
Created by Wen-Qi Toh
26/8/21"""


def not_blank(question):
    error = "ERROR: Please enter in the name of your product (cannot be blank)"
    valid = False   # to create loop

    while not valid:
        response = input(question)

        if not response:  # checks if product name has been entered
            print(error)
        else:  # no error found
            return response


def number_checker(test):
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
valid_list = False
while not valid_list:
    # calling not blank function and providing question
    products = not_blank("Please enter product mass, name, then price. "
                         "(or enter 'X' to exit): ").capitalize()

    if products != "X":
        products = products.split()
        print(products)

        for line in products:
            price = number_checker(products[-1])
            products.remove(products[-1])
            print(price)

            mass = number_checker(products[0])
            products.remove(products[0])
            print(mass)
            name = " ".join(products)
            print(name)

            try:
                unit_price = round(price / mass, 2)
                product_info.append([mass, name, price, unit_price])
                unit_price_list.append(unit_price)
                print(unit_price)

            except ZeroDivisionError:
                unit_price = None
                print(unit_price)
                print("No unit price as mass/price entered incorrectly.")

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
