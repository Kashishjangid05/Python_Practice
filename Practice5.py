#WAP to input user name and print its length as well as perform some string functions
name = input ("enter name")
print("the name is:", name)

print("The length of name is:",len(name))
print("the name ends with 'id':",name.endswith("id"))
print("The capitalize format of name is:",name.capitalize())
print("The name replacement of 'i' with 'e'",name.replace("i","e"))
print("The index of 'a' in name is:",name.find("a"))
print("the name contains total 'h':",name.count("h"))