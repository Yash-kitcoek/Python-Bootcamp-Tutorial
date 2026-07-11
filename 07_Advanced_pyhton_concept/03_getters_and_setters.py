class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def first_name(self):
        l = self.name.split(" ")
        return l[0]

    @first_name.setter
    def first_name(self, first):
        l = self.name.split(" ")
        self.name = f"{first} {l[1]}"


e = Employee("John Doe", 45000)

print(e.first_name)   # John
print(e.name)         # John Doe

e.first_name = "Jane"

print(e.first_name)   # Jane
print(e.name)         # Jane Doe