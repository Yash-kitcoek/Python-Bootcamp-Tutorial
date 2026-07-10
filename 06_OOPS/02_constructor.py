#Constructor

class Employee:
    def __init__(self,name, salary,age):
        self.name = name
        self.salary = salary
        self.age = age

    def get_salary(self):
        return self.salary 

    def get_info(self):
        print(f"the name of the employees is {self.name}. Salary is {self.salary} and the age is {self.age}")

e1 = Employee('Yash',45000,21)

e1.get_info()