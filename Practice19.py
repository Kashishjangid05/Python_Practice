#WAP to print list elements using for loop
list = [1,4,9,16,25,36,49,64,81,100]
for val in list:
    print(val)

#WAP to search for a number in tuple
tuple = (1,4,9,16,25,36,49,64,81,100)
x = int(input("enter"))
index = 0
for val in tuple:
    if (val == x):
        print("found at index",index)
    index += 1