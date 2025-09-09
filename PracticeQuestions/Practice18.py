#WAP to find element from tuple
nums = (1,4,9,16,25,36,49,64,81,100)
x = int(input("enter number to be found"))

i=0
while i<=len(nums)-1:
    if(nums[i] == x):
        print("found at index " , i)
        break
    else:
        print("not found")
    i += 1