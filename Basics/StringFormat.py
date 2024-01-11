# str.format() =     optional method that gives users
#                    more control when displaying output

animal = "cow"
item = "moon"
# print("The " + animal + " jumped over the " + item)
print("The {} jumped over the {}".format(animal,item))
print("The {0} jumped over the {1}".format(animal,item)) # positional argument
print("The {1} jumped over the {0}".format(item,animal)) # positional argument
print("The {animal} jumped over the {item}".format(animal="cow",item="moon")) # keyword argument

text= "The {} jumped over the {}"
print(text.format(animal,item))

print()

name = "Rotem"
print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name)) # adds padding to the argument
print("Hello, my name is {:<10}. Nice to meet you".format(name)) # left align the argument within the inserted padding
print("Hello, my name is {:>10}. Nice to meet you".format(name)) # right align the argument within the inserted padding
print("Hello, my name is {:^10}. Nice to meet you".format(name)) # center align the argument within the inserted padding

print()

number = 3.14159
number2 = 1000

print("The number pi is {:.3f}".format(number)) #displays only the first x (3) digits after the decimal
print("The number is {:,}".format(number2)) # automatically add coma to all 1000s places
print("The number is {:b}".format(number2)) # displays a binary representation of the number
print("The number is {:o}".format(number2)) # displays an octal representation of the number
print("The number is {:X}".format(number2)) # displays a hexadecimal representation of the number
print("The number is {:E}".format(number2)) # displays a scientific notation representation of the number
