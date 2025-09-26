# #class and object
# class student:
#     name = "Bittu"
#     course = "B.Tech"

# s1 = student()
# print(s1.name)
# print(s1.course)

# init function
# # ---Cnstructor---
# class student:

#     # default constructors
#     def __init__(self):
#         pass

#     # parameterized constructors
#     def __init__(self , name , marks):
#         self.name = name
#         self.marks = marks
#         print("Kashish")
    
# s1 = student("Bittu" , 98)
# print(s1.name , s1.marks)

# # methods
# class student:
#     def __init__(self,fullname):
#         self.name = fullname

#     def welcome(self):
#         print("welcome student")
#         print("welcome student",self.name)

# s1 = student("Bittu")
# s1.welcome()

# # static methods
# class student:
#     @staticmethod              #does not wrk staticmethod
#     def college():
#         print("abc college")

# class ABC:
#     def __init__(self , name):
#         self.name = name

# s1 = ABC("Bittu")
# print(s1.name)
# del s1.name
# print(s1.name)

# # ---private class and methods
# class person:
#     __name = "Bittu"      #private class

#     def __hello(self):    #private method
#         print("hello")

#     def welcome(self):    #public method
#         self.__hello
    
# p = person()
# print(p.welcome())        #this can access because welcome is public and is in class so it can access heello also
# # print(p.__hello())  will show error because cant access the private methods outside the class


#---Inheritance---
# ---------------Single Inheritance---------------------
# class Car:
#     color = "black"
#     @staticmethod
#     def start():
#         print("car started..")
#     @staticmethod
#     def stop():
#         print("car stopped..")

# class Carss(Car):
#     def __init__(self , name):
#         self.name = name
    
# c1 = Carss("fortuner")
# c2 = Carss("maruti")
# print(c1.name)
# c1.start()
# print(c1.start())
# print(c1.stop())
# print(c1.color)
# print(c2.name)
# print(c2.start())
# print(c2.stop())
# print(c2.color)


# ---------------Multilevel Inheritance---------------------
# class Car:
#     @staticmethod
#     def start():
#         print("car started..")
#     @staticmethod
#     def stop():
#         print("car stopped..")

# class Carss(Car):
#     def __init__(self , name):
#         self.name = name

# class fortuner(Carss):
#     def __init__(self,type):
#         self.type = type

# c1 = fortuner("diesel")
# c1.start()
# print(c1.type)


# ---------------Multiple Inheritance---------------------
# class A:
#     varA = "welcome to class A"
# class B:
#     varB = "welcome to class B"
# class C(A,B):
#     varC = "welcome to class C"

# c1 = C()

# print(c1.varC)
# print(c1.varB)
# print(c1.varA)


# -----Super Method---------
# class Car:
#     def __init__(self,type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("car started..")
#     @staticmethod
#     def stop():
#         print("car stopped..")

# class Carss(Car):
#     def __init__(self , name , type):
#         super(). __init__(type)
#         self.name = name
#         super().start()

# c1 = Carss("fortuner" , "diesel")
# c1.start()
# print(c1.name)
# print(c1.type)

# ----------class method--------------
# class Person:
#     name = "naresh"

#     @classmethod
#     def changeName(cls, name):
#         cls.name = name

# p1 = Person()
# p1.changeName("bittu")
# print(p1.name)
# print(Person.name)

# -----------@property method-----------
# class Student:
#     def __init__(self , phy , chem , maths):
#         self.phy = phy
#         self.chem = chem
#         self.maths = maths

#     @property
#     def cal_percentage(self):
#         return str((self.phy + self.chem + self.maths)/3) + "%"

# stu = Student(97 , 98 , 93)
# print(stu.cal_percentage)

# stu.phy = 88
# print(stu.cal_percentage)

# -----------Operator Overloading---------
class Complex:
    def __init__(self , real , img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real , "i +" , self.img , "j")

    def __add__(self , num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)

    def __sub__(self , num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal,newImg)


num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(2,6)
num2.showNumber()

num3 = num1+num2
num3.showNumber()

num4 = num1-num2
num4.showNumber()