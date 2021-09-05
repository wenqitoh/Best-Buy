"""Component 6 v1 - calculate best-buy, output (2 Methods)
Created by Wen-Qi Toh
11/8/21"""


# num-check function to check price is number,
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


# main routine - Method 1 - removing over budget prices to calculate BB...
# ...while program is still running and user hasn't entered 'X' yet

budget = 10.00  # set data for testing purposes only
price_list = [3, 5.99, 6.45, 2.98]  # set data for testing purposes only

valid = False
while not valid:

    # continuing from Component 4:
    price = num_check("What is your product price? ")

    price_list.append(price)    # initial assumption - price is <= budget

    # to add to component 4 underneath price things
    if price > budget:
        price_list.remove(price)
        print("Price exceeded budget so it has been removed from the list.")
    else:
        print(price_list)
        print("Price added to shopping cart!")

    print("Here is the price list so far!", price_list)


# main routine - Method 2 - removing over budget prices & calc. BB at end of...
# ...program, after user has entered 'X'

budget = 5.00  # set data for testing purposes only
unit_price_list = [0.05, 0.04, 0.05, 0.02, 0.01, 0.02]
# no need to check these lists are correct, as any errors would have alr...
# ...been filtered out by the earlier parts of the program
product_list = [[250, 'ch1', 12, 0.05],
                [300, 'ch2', 11.99, 0.04],
                [110, 'ch3', 5, 0.05],
                [200, 'ch4', 3.99, 0.02],
                [230, 'ch5', 2.45, 0.01],
                [250, 'ch6', 6, 0.02]]    # set data for testing purposes only

best_buy = []

for product in product_list:
    if product[2] > 5:
        product_list.remove(product)
        unit_price_list.remove(product[3])

        print("The product '{}' has been removed from product list as the price exceeds the"
              " budget.\n".format(product[1]))
        print(unit_price_list)
    elif product[2] <= 5:
        print("product {} accepted\n".format(product[1]))
        if product[3] < min(unit_price_list):
            best_buy = product
            print("if {}".format(best_buy))
        elif product[3] == min(unit_price_list):
            best_buy.append(product)
            print("product {} accepted".format(product[1]))
            print("best buy so far: {}\n".format(best_buy))

# final output
print("The recommended best buy/s for you is: {}".format(best_buy))
