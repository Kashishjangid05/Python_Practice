#WAP to print multiplication table of n
num = int(input("enter the number"))
print("the multiplication table of " ,num)

i = 1
while(i <= 10):
    print(num , "*" , i , "=" , num * i)
    i += 1
