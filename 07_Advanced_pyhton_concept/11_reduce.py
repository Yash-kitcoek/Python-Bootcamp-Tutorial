from functools import reduce

numbers = [1,2,34,56,4]

def sum(a, b):
    return a + b

c= reduce(sum,numbers)
print(c)