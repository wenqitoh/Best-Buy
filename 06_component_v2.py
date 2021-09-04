"""Component 6 v1 - calculate best-buy, output, using method 2
2 steps - 1) filter by price, removing if over-budget
          2) then filter by unit price, lowest UP for remaining products = BB
Created by Wen-Qi Toh
4/9/21"""

# main routine - Method 2 - removing over budget prices & calc. BB at end of...
# ...program, after user has entered 'X'

budget = 5.00  # set data for testing purposes only
unit_price_list = [0.05, 0.05, 0.05, 0.02, 0.01, 0.02]
# no need to check these lists are correct, as any errors would have alr...
# ...been filtered out by the earlier parts of the program
product_list = [[250, 'ch1', 12, 0.05],
                [350, 'ch2.5', 12, 0.05],
                [110, 'ch3', 5, 0.05],
                [200, 'ch4', 3.99, 0.02],
                [230, 'ch5', 2.45, 0.01],
                [250, 'ch6', 6, 0.02]]    # set data for testing purposes only

best_buy = []

for product in product_list:    # so basically my issue is that when u run this prg,
            # it doesn't print out if ch2 is accepted or not? I've tried with different numbers and everything like that,
            # but this prg always skips the 2nd value in the product list. also it does it sometimes w/ the last value, idk why
    if product[2] > 5:  # step 1
        product_list.remove(product)
        unit_price_list.remove(product[3])

        print("The product '{}' has been removed from product list as "
              "the price exceeds the budget.\n".format(product[1]))

    elif product[2] <= 5:   # step 2
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
