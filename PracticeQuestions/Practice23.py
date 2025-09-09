#WAP to find average of 3 numbers using function
def average(a,b,c):
    return (a+b+c)/3
avg = average(1,2,3)
print(avg)

# WAP to print length of the list (list is the parameter)
nums = [1,2,3,4,5,6,7,8]
def print_len(list):
    print(len(list))

print_len(nums)
# WAP to print elements of list in a single line
print(nums[0],end=" ")
print(nums[1],end=" ")  #end = " "means space will be there and no next line, output will be in same line
print(nums[2],end=" ")
print(nums[3],end=" ")
print(nums[4],end=" ")
print(nums[5],end=" ")
print(nums[6],end=" ")
print(nums[7],end=" ")