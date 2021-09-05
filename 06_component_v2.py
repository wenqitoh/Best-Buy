"""Component 6 v1 - calculate best-buy, output, using method 2
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
                [350, 'ch2.5', 12, 0.05],
                [110, 'ch3', 5, 0.05],
                [112, 'ch3.5', 4.5, 0.01],
                [200, 'ch4', 3.99, 0.02],
                [230, 'ch5', 2.45, 0.01],
                [230, 'ch5', 2.45, 0.01],
                [250, 'ch6', 6, 0.02]]    # set data for testing purposes only

best_buy = []
new_product_list = []
new_upl = []

for product in product_list:
    if product[2] > 5:  # step 1
        # product_list.remove(product)
        print("The product '{}' has been removed from product list as "
              "the price exceeds the budget.\n".format(product[1]))

    elif product[2] <= 5:   # step 2
        print("\nproduct {} accepted".format(product[1]))
        new_product_list.append(product)
        new_upl.append(product[3])
        print("new product list:{}".format(new_product_list))
        print("new unit price list: {}".format(new_upl))

for nproduct in new_product_list:
    # this line account for an empty list OR a lower price
    if not best_buy or nproduct[3] < best_buy[0][3]:
        best_buy = [nproduct]
    elif nproduct[3] == best_buy[0][3]:
        best_buy.append(nproduct)

count = 0
# final output
print("The recommended best buy/s for you is:\n{}\n".format(best_buy))

# print(*best_buy, sep = "\n")
for item in best_buy:
    print(' '.join(str(x) for x in item))

for number, letter in enumerate(best_buy):
    print(number, ' '.split(letter))

        # if product[3] < new_upl[0]:
        #     best_buy.clear()
        #     best_buy.append(product)
        #     new_upl.remove(new_upl[0])
        #     print("best buy for if stmnt: {}".format(best_buy))
        #     print("new upl removed: {}".format(new_upl))
        #     # best_buy = product
        #
        # elif product[3] == min(new_upl):
        #     index = new_upl.index(min(new_upl))
        #     print(index)
        #     new_upl.remove(index)
        #     new_upl.append(product[3])
        #     new_upl.append(product[3])
        #     best_buy.append(product)
        #     print("best buy so far: {}".format(best_buy))





