# class is the blueprint or template 

# Object is the specific instance created from the class


class Employee:
    company = "Hp"

    def get_salary(self): #a self is important  here because self is a way to reference the object of the class which is being created
        return 35000


e = Employee()

print(e.get_salary()) 

###############################

class Animal:
    def sleep(self):
        print("Animal can sleep")

a = Animal()
print(a.sleep())    