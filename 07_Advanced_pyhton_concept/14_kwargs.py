#kwargs 

def marks(**kwargs):
    for item in kwargs.keys():
       print(f"The marks of {item} are {kwargs[item]}")

marks(shubham = 34, vishal = 45)