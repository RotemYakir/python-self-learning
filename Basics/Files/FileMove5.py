import os

source = "C:\\Python\\self learning youtube\\copy.txt"  # one backslash needs to be turned to double backslash
destination = "C:\\Users\\ryaki\\OneDrive\\Desktop\\copy.txt"

try:
    if os.path.exists(destination):
        print("The name of the file is already taken at your destination")
    else:
        os.replace(source, destination)
        print(source + " was moved to: " + destination)
except FileNotFoundError:
    print(source + " was not found")  # for practicing: if this error occurs - run FileCopy4.py first
