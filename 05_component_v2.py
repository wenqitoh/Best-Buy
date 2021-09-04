"""Component 5 v2 - allow for multiple min/max values,
output the multiple values not just pick one
Created by Wen-Qi Toh
16/8/21"""


# for testing purposes, will be using sample data, not user input for list
unit_price_list = [10.81, 10.00, 17.37, 15.96, 11.76, 16.50]
cheapest = []
costliest = []

for price in unit_price_list:
    # this line account for an empty list OR a lower price
    if not cheapest or price < cheapest[0]:
        cheapest = [price]

    elif price == cheapest[0]:
        cheapest.append(price)

    # this line account for an empty list OR a higher price
    elif not costliest or price > costliest[0]:
        costliest = [price]

    elif price == costliest[0]:
        costliest.append(price)

# display min/max
print(f"cheapest: {cheapest}")
print(f"costliest: {costliest}")
