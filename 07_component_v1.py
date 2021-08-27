"""Component 7 v1 - allowing product name, mass/volume, and price to be entered
on one line by user - more accessible/functional
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
                continue
        except ValueError:
            print(error)


# main routine
unit_price_list = []
product_info = []

valid_list = False
while not valid_list:
    # calling not blank function and providing question
    products = not_blank("Please enter product mass, name, then price. "
                         "(or enter 'X' to exit): ")\
                        .capitalize()
    if products != "X":
        products = products.split()
        print(products)
        for line in products:

            if products[0][0].isdigit():
                mass = float(products[0])   #product mass
                products.remove(products[0])

            if products[-1][0].isdigit() and float(products[-1]) > 0:
                price = float(products[-1]) # product price
                products.remove(products[-1])
                name = " ".join(products)   # product name
            # calculating unit price per product
                unit_price = round(price / mass, 2)
                product_info.append([mass, name, price, unit_price])

            unit_price_list.append(unit_price)

        # making sure list has at least 2 products to compare
    elif len(product_info) < 2:
        print("ERROR: Please enter at least 2 products to compare.")
    else:
        valid_list = True   # break out of loop if list contains 2+ items
        print("\nYou have chosen to end the product loop. Product unit prices"
              " as follows:\n")
        break

    # adding the unit ppp number to unit price list to print 2gether
print("Product list: {}".format(product_info))
print("Unit price list: {}".format(unit_price_list))

count = 0
total_unit_price = 0.0

# printing final statements, unit prices
for item in product_info:
    print(f"The unit price of {item[1]} is ${item[2]}/{item[0]} = "
          f"{round(item[3],4)}")
    count += 1
    total_unit_price += round(item[3],4)
av_unit_price = sum(unit_price_list) / len(unit_price_list)
print("Average unit price: ${}".format(round(av_unit_price, 2)))
