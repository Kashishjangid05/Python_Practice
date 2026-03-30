num = int(input("Enter the number:"))

temp = num
sum = 0
count = len(str(num))

while temp > 0:
    rem = temp % 10
    sum = sum + rem**count
    temp //= 10

if sum == num:
    print("Armstrong number")
else:
    print("Not a armstrong number")