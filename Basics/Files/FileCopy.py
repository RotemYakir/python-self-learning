# copyfile() = copies contents of a file
# copy()     = copyfile() + permission mode + destination can be a directory
# copy2()    = copy() + copies metadata (file's creation and modification times)

import shutil

path = "C:\\Python\\self learning youtube\\test.txt" # one backslash needs to be turned to double backslash
path_of_copy = "C:\\Python\\self learning youtube\\copy.txt" # one backslash needs to be turned to double backslash

shutil.copyfile(path,path_of_copy) # source , destination