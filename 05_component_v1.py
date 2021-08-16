"""Component 5 v1 - calculate least + most expensive product
then output
Created by Wen-Qi Toh
11/8/21"""


# for testing purposes, will be using sample data, not user input for list
unit_price_list = [10.81, 10.00, 17.37, 15.96, 11.76, 16.50]

# max/min
cheapest = min(unit_price_list)
costliest = max(unit_price_list)

# output info
print("Cheapest item is: {}".format(cheapest))
print("Most expensive item is: {}".format(costliest))

