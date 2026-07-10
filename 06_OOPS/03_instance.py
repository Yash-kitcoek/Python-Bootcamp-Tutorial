#INSTANCE

class Employee:
    company = "J P Morgan" #this is class Attribute

    def __init__(self,name, salary,age,company):
        self.name = name
        self.salary = salary
        self.age = age
        self.company = company

    def get_salary(self):
        return self.salary 

    def get_info(self):
        print(f"the name of the employees is {self.name}. Salary is {self.salary} and the age is {self.age}")

e1 = Employee('Yash',45000,21, "Deloitte")

e1.get_info()
print(e1.company) #always print instatnce attribute
print(Employee.company)

# Object Interospection
# print(dir(e1))