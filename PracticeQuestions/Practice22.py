#WAP to find the factorial of n numbers using for loop
n = int(input("enter a number"))
mult = 1
for i in range( 1, n+1):
    if n == 0 or n == 1:
        print("1")
    mult = mult * i
    i += 1
print("the factorial of" , n , "is" , mult)