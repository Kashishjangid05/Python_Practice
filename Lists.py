<<<<<<< HEAD
#lists concept
marks = [89, 78,69,98,82,79]#same elements
print(marks)
print("the length of marks is:",len(marks))
marks[2] = 99
print("the new list or updated list " ,marks)#mutable
print(type(marks))


student = ["Kashish",19,97,"ai"]#different elements
print("the students details: ", student)
print("the length of student is :" , len(student))
student[0] = "Kashish Jangid"
print("the updated list is :" , student)

#slicing
print(marks[1:4])
print(marks[0:3])
print(marks[:3])
print(marks[2:6])
print(marks[2:len(marks)])
print(marks[2:])
print(marks[-4:-2])

#methods
list= [2,1,3,1,8]
list.append(4)
print(list)
list.sort()
print(list)
list.sort(reverse = True)
print(list)
list.reverse()
print(list)
list.insert(3,7)
print(list)
list.remove(2)
print(list)
list.pop(4)
=======
#lists concept
marks = [89, 78,69,98,82,79]#same elements
print(marks)
print("the length of marks is:",len(marks))
marks[2] = 99
print("the new list or updated list " ,marks)#mutable
print(type(marks))


student = ["Kashish",19,97,"ai"]#different elements
print("the students details: ", student)
print("the length of student is :" , len(student))
student[0] = "Kashish Jangid"
print("the updated list is :" , student)

#slicing
print(marks[1:4])
print(marks[0:3])
print(marks[:3])
print(marks[2:6])
print(marks[2:len(marks)])
print(marks[2:])
print(marks[-4:-2])

#methods
list= [2,1,3,1,8]
list.append(4)
print(list)
list.sort()
print(list)
list.sort(reverse = True)
print(list)
list.reverse()
print(list)
list.insert(3,7)
print(list)
list.remove(2)
print(list)
list.pop(4)
>>>>>>> c3eef04 (Your commit message)
print(list)