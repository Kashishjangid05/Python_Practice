#WAP to print sum of first n natural numbers using recursion
def calc_sum(n):
    if(n==0):
        return 0
    return calc_sum(n-1) + n

sum = calc_sum(5)
print(sum)

#WAP to print elements of a list using index using recursive function
def calc_list(arr,index = 0):
    if( index == len(arr)):
        return
    # print(list)
    print("index:",index,"=",arr[index])
    calc_list(arr, index+1)

nums = [1,2,3,8]
print(calc_list(nums))