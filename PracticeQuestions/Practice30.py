# define employee class with attributes role , department , salary. it also has showDetails() method.
# then add engineer class which inherits properties from employee ad has name and age attribute
class employee:
    def __init__(self ,role , department , salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print("name= ", self.name)
        print("age=" , self.age)
        print("role= " , self.role)
        print("department= ", self.department)
        print("salary= ", self.salary)

class engineer(employee):
    def __init__(self , name , age):
        self.name = name
        self.age = age
        super().__init__("engineer" , "IT" , "70000")

eng1 = engineer("bittu " , "19")
eng1.showDetails()
