# create student class and add arguments in constructor of name and marks and use methods to print average
class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("student name:" , self.name , "average marks:" , sum/3)

s1 = student("Bittu" , [99,98,97])
s1.get_avg()

s1.name = "Naresh"
s1.get_avg()

