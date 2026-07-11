# magic/ dunder 

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"The name of employee is {self.name} and the salary is {self.salary}"

    def __repr__(self):
            return f"The name of employee is {self.name} and the salary is {self.salary}"
    


e = Employee("Ashish",45000) 
print(e.name, e.salary)

print(str(e))

print(repr(e))
