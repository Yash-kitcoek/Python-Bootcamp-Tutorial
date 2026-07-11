class Employee:
    companny = "Asus"
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary

    #instances variable(default)
    def print_info(self):
        info = f"The name of employee is {self.name} and the salary is {self.salary}"
        print(info)

    #static Method
    @staticmethod
    def sum(a, b) :
        return a + b

    #class Method
    @classmethod
    def print_company(cls):
        print(cls.companny)

    @classmethod
    def change_company(cls, new_coompany):
        cls.companny = new_coompany

e1 = Employee("John", 35000)
e2 = Employee("jane", 45000)

e1.print_info()
e2.print_info()

print(e2.sum(5,5))

e1.print_company()

e1.change_company("microsoft")
e1.print_company()

# print(Employee.companny)