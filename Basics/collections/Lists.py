# list = used to store multiple items in a single variable

food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]

food.pop()
food.append("ice cream")
food.remove("hotdog")
food.insert(0, "cake")
food.sort()  # sorts the list alphabetically
# food.clear() # removes all the items in the list

# food[0] = "sushi"
# print(food[0])

for x in food:
    print(x)
