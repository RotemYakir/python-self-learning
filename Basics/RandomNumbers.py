import random

x = random.randint(1, 6)
y = random.random()  # random number between 0-1
print("x = {}".format(x))
print("y = {}".format(y))

myList = ["rock", "paper", "scissors"]
z = random.choice(myList)
print("z = {}".format(z))

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
random.shuffle(cards)
print(cards)
