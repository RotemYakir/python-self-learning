# scope = The region that a variable is recognized.
#         A variable is only available from inside the region it is created.
#         A global and locally scoped versioned of a variable can be created.

name = "Rotem"  # global scope (available inside & outside functions)


def display_name():
    name = "Yakir" # local scope (available only inside this function)
    print(name)

display_name()
print(name)