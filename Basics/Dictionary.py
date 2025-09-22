# # dictionary concepts
# dict = { 
#     "name" : "Kashish" ,
#     "age" : 19 , 
#     "rollno" : 15 , 
#     "marks" : 94.4 , 
#     "subject" : ["python" , " C" , "Java"], 
#     "topics" :("dictionary" , "sets"),
#     "is_adult": True,
#     12 : "yes"
# }
# print(dict)
# print(dict["name"])
# dict["rollno"] = 20
# dict["surname"] = "Jangid"
# print(dict)

# nested disctionary

student = {
    "name" : 'Kashish',
    "rollno" : 20,
    "subject-marks" : {
        "phy" : 94,
        "chem" : 98,
        "maths" : 90,
    }
}
# print(student)
# print(student["subject-marks"])
# print(student["subject-marks"]["chem"])

# dictionary methods
# keys function
print(student.keys())
print(len(student))
print(len(list(student.keys())))
print(list(student.keys()))

# values function
print(student.values())
print(list(student.values()))

# item function
print(student.items())
print(list(student.items()))
pair = list(student.items())
print(pair[1])

# get function
print(student["name"])
print(student.get("name"))
print(student.get("name2"))#this did not give error but the same thing in student["name"] cant be happen it will provide error

# update function
student.update({"city":"delhi"})
print(student)

new_dict = { "branch":"ai"}
student.update(new_dict)
print(student)

# 
