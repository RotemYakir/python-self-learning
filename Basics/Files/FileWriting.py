import os

path = "C:\\Python\\self learning youtube\\test.txt"  # one backslash needs to be turned to double backslash
text = "Hello!!!\nThis is some text\nHave a nice day!!!\n"
text_to_append = "this is new text i added."

try:
    with open(path, "w") as file:  # "w" - write
        file.write(text)
    with open(path, "a") as file:  # "a" = append
        file.write(text_to_append)
except FileNotFoundError as e:
    print("That file was not found: " + str(e))
except Exception as e:
    print("Something went wrong: " + str(e))
else:
    print("completed writing the file.")