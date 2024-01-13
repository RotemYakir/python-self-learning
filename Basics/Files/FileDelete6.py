import os
import shutil

path = "C:\\Python\\self learning youtube\\test.txt"

try:
    os.remove(path)  # deletes a file
    # os.rmdir(path) # deletes a file or empty folder
    # shutil.rmtree(path) # deletes folders and all files contained within (rmtree - remove tree)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError as e:
    print("That folder contains files: " + str(e))
else:
    print("The file was deletes successfully")
