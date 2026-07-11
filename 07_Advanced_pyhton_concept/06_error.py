# while True:
#   try:
#     a = int(input("Enter a  : "))
#     b = int(input("Enter b :  "))

#     print(f"the sum is {a + b}")

#   except ZeroDivisionError:
#     print("Division by zero not possible")


#   except Exception as e:
#     print("Some error occured",e)


a = int(input("Enter a : "))
b = int(input("Enter b : "))

if b == 0:
    raise ValueError("Please dont divide by 0")

print(f"the division is {a / b}")