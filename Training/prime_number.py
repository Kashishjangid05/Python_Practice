num = 11
i = 2
count1 = 0
# normal approach, this loop occur 9 times
while i < num:
    if(num %i ==0):
        print("not a prime number")
        break
    i += 1
    count1 += 1
else:
    print("prime number")
print(count1)

# optimum approach as this loop will occur only 2 times
j = 2
count2 = 0
while j < num ** 0.5:    #any number will be divisible to its half only. For ex. 10 is completely divisible by 5 only(largest)
    if(num %j ==0):
        print("not a prime number")
        break
    j += 1
    count2 += 1
else:
    print("prime number")
print(count2)