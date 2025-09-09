#WAP to print sum of n numbers using while loop
n = int(input("enter number"))
sum = 0
i = 1
while i<=n:
    sum += i
    i += 1
print("the sum of first", n ,"numbers is:" , sum)