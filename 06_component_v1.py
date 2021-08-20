"""Component 6 v1 - calculate best-buy, output
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

