"""Component 6 v2 - calculate best-buy, output, using method 2
2 steps - 1) filter by price, removing if over-budget
          2) then filter by unit price, lowest UP for remaining products = BB
Created by Wen-Qi Toh
4/9/21"""

# main routine - Method 2 - removing over budget prices & calc. BB at end of...
# ...program, after user has entered 'X'

budget = 5.00  # set data for testing purposes only
unit_price_list = [0.01, 0.05, 0.05, 0.01, 0.02, 0.01, 0.02]
# no need to check these lists are correct, as any errors would have alr...
# ...been filtered out by the earlier parts of the program
product_list = [[250, 'ch1', 12, 0.01],
                [350, 'ch2', 11.99, 0.06],
                [110, 'ch3', 16, 0.05],
                [200, 'ch4', 7, 0.02],
                [230, 'ch5', 6.45, 0.01],
                [250, 'ch6', 6, 0.02]]    # set data for testing purposes only

best_buy = []
new_product_list = []
new_upl = []

for product in product_list:
    if product[2] > 5:  # step 1
        print("The product '{}' has been removed from product list as "
              "the price exceeds the budget.\n".format(product[1]))

    elif product[2] <= 5:   # step 2
        print("\nproduct {} accepted".format(product[1]))
        new_product_list.append(product)
        new_upl.append(product[3])
        print("new product list:{}".format(new_product_list))
        print("new unit price list: {}".format(new_upl))

for new_product in new_product_list:
    # this line account for an empty list OR a lower price
    if not best_buy or new_product[3] < best_buy[0][3]:
        best_buy = [new_product]
    elif new_product[3] == best_buy[0][3]:
        best_buy.append(new_product)

# final output
print("The recommended best buy/s for you is:")
for item in best_buy:
    print(' - '.join(str(x) for x in item))
