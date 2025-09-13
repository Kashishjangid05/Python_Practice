# f = open("demo.txt","r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# f = open("demo.txt","w")
# data = f.write("new line")
# print(data)

# f = open("demo.txt","a")
# data = f.write("\nnew line added")
# print(data)

# with syntax
with open("demo.txt" , "r") as f:
    data = f.read()
    print(data)

with open("demo.txt" , "w") as f:
    f.write("Kashish Jangid")
    
