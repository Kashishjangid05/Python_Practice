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

class ABC:
    def __init__(self , name):
        self.name = name

s1 = ABC("Bittu")
print(s1.name)
del s1.name
print(s1.name)