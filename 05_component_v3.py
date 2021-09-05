"""Component 5 v3 - allow for multiple min/max values,
output the multiple values not just pick one
use a set, so that both name and price is printed not just price - more user
friendly
Created by Wen-Qi Toh
5/9/21"""

# for testing purposes, will be using sample data, not user input for list
product_list = [[500, 'Essentials Cheese Block Cheddar', 6.4, 0.01],
                [100, 'Galaxy Blue Cheese Creamy Blue Wedge', 4.7, 0.05],
                [125, 'Galaxy Soft White Cheese Brie Wheel', 4.3, 0.03],
                [125, 'Galaxy Soft White Cheese Camembert Wheel', 4.3, 0.03],
                [130, 'Meyer Semi Soft Cheese Cumin Gouda', 7.4, 0.06],
                [500, 'Countdown Cheese Block Colby', 8.2, 0.02]]


cheapest = []
costliest = []

for product in product_list:
    # this line account for an empty list OR a lower price
    if not cheapest or product[2] < cheapest[0][1]:
        cheapest = [(product[1], product[2])]
    elif product[2] == cheapest[0][1]:
        cheapest.append((product[1], product[2]))
    # this line account for an empty list OR a higher price
    if not costliest or product[2] > costliest[0][1]:
        costliest = [(product[1], product[2])]

    elif product[2] == costliest[0][1]:
        costliest.append((product[1], product[2]))

# display min/max
print("cheapest product:")
for s in cheapest:
    print(", ".join(str(e) for e in s))
print("\ncostliest product:")
for s in costliest:
    print(", ".join(str(e) for e in s))
