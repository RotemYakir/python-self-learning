# reduce() = apply a function to an iterable and reduce it to a single cumulative (מצטבר) value.
#            performs function on first tw elements and repeats process until 1 value remains.

#  https://youtu.be/XKHEtdqhLK8?t=18141

import functools

# reduce(function,iterable)

letters = ["H", "E", "L", "L", "O"]
word = functools.reduce(lambda x, y,: x + y, letters)
print(word)

factorial = [5,4,3,2,1]
result = functools.reduce(lambda x,y,:x*y,factorial)
print(result)