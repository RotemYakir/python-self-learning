# walrus operator :=

# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# print(happy:=True)

foods = list()

# while True:
#     food = input("What food do you like?: ")
#     if food == "quit":
#         break
#     foods.append(food)

while food := input("What food do you like?: ") != "quit":
    foods.append(food)
