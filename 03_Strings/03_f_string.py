# string formatting

template = "Dear {}, You are very lucky you got {}$ package"

a = "Yash"
a1 = 5000

s1 = template.format(a, a1)
print(s1)

print(f"{a}, You are very lucky you fcgot {a1}$ package")