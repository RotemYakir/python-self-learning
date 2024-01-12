import os

path = "C:\\Python\\self learning youtub\\test.txt"  # one backslash needs to be turned to double backslash

try:
    with open(path) as file:  # using with open will close files automatically
        print(file.read())
except FileNotFoundError as e:
    print("That file was not found: "+str(e))
except Exception as e:
    print(e)
