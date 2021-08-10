"""Component 3 v1 - get list of products till user enters X then output
Created by Wen-Qi Toh
9/8/21"""


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
product_names = []   # create blank product list

valid_list = False
while not valid_list:
    product = not_blank("Please enter product name and enter 'X' to exit: ")\
                        .capitalize()    # calling not blank function and providing question

    if product != "X":
        product_names.append(product)   # adding ingred to list if no exit code
    else:
        if len(product_names) < 2:
            print("ERROR: Please enter at least 2 products to compare.")
        else:
            valid_list = True   # break out of loop if list contains 2+ items
            print("Here are your products: \n{}".format(product_names))
