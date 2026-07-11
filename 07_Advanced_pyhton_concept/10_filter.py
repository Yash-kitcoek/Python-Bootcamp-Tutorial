#filter

def is_greater_than_9(x):
    if x > 9:
        return True
    else :
        return False


a = [1,5,6,89,2,1,23,4]

new = list(filter(is_greater_than_9,a))
print(new)

new = list(filter(lambda x : x > 9, a))
print(new)