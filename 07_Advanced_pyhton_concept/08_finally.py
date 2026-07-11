a = int(input("Enter a : "))
b = int(input("Enter b : "))

try:
    c = a/ b
    print(c)

except Exception as e :
    print(e)

finally: 
    print("The final block always excectes")