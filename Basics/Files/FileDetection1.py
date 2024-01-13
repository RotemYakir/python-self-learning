import os

path = "C:\\Python\\self learning youtube\\test.txt" # one backslash needs to be turned to double backslash

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory!")
else:
    print("That location doesn't exist.")
