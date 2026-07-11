#args

def  sum(*args):
    total = 0
    for item in args:
        total += item
    return total


print(sum(45,45,90))