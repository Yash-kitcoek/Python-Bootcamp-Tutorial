# Variable

# 1) Local Variable
# 2)Global Variable

# def local():
#     print("Local Variable called")

# local()

# print("Global Variable called")


# Global Keyword

def add(a, b):
    print("sum of two numbers")
    c = a + b
    global z
    z = 0
    return c

z = 3
print(add(5,5))
print(z)