"""v2
Fixes second problem

"""


def not_blank(question):
    error = "ERROR: Please enter in the name of your product (cannot be blank)"
    valid = False   # to create loop

    while not valid:
        response = input(question)

        if not response:  # checks if product name has been entered
            print(error)
        else:  # no error found
            return response


# main routine
unit_price_list = []
product_info = []
valid_list = False
while not valid_list:
    # calling not blank function and providing question
    products = not_blank("Please enter product mass, name, then price. (or enter 'X' to exit): ")\
                        .capitalize()
    print(products)

    if products != "X":
        if products[0].isdigit() and products[-1].isdigit():
            product_info.append(products)
            print(product_info)
        else:
            print("Error entering data. Try again")
            continue

        # making sure list has at least 2 products to compare
    elif len(product_info) < 2:
        print("ERROR: Please enter at least 2 products to compare.")
    else:
        valid_list = True   # break out of loop if list contains 2+ items
        print("\nYou have chosen to end the product loop. Product unit prices"
              " as follows:\n")

        for line in product_info:
            line = line.split()

            mass = float(line[0])
            line.remove(line[0])

            price = float(line[-1])
            line.remove(line[-1])

            name = " ".join([str(word) for word in line])

            unit_price = round(price / mass, 3)
            unit_price_list.append([mass, name, price, unit_price, unit_price])

            print(f"mass: {mass}, price: ${price}, name: {name}, unit price: ${unit_price}")


# Final outputs
print("Product list: {}".format(product_info))
print("Unit price list: {}".format(unit_price_list))

count = 0
total_unit_price = 0.0

for item in unit_price_list:
    print(f"The unit price of {item[1]} is ${item[2]}/{item[0]} = {round(item[3],4)}")
    count += 1
    total_unit_price += item[3]

av_unit_price = total_unit_price / count
print("Average unit price: ${}".format(round(av_unit_price, 2)))
