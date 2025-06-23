# write a program to find the maximum of the numbers in a list using the reduce function.
from functools import reduce 
a = [1, 2, 343, 455, 655, 432, 57]
def greater(a, b):
    if (a > b):
        return a
    return b 
print(reduce(greater, a))