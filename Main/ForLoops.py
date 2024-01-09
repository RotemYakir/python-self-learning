# for loop = a statement that will execute it's block of code a limited amount of times
import time

for i in range(10):
    print(i + 1)

print()

for i in range(50, 101, 2):
    print(i)

print()

for i in "Rotem Yakir":
    print(i)

print()

for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)
print("Happy new year!")
