# Higher Order Function =  a function that either:
#                          1. accepts a function as an argument
#                             or
#                          2. returns a function
#                          (In Python, functions are also treated as objects)
# https://www.youtube.com/watch?v=XKHEtdqhLK8&t=16521s


# dividend/divisor=quotient
def divisor(x):
    def dividend(y):
        return y / x

    return dividend

divide = divisor(2)
print(divide(10))


