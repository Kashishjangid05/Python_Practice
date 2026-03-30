# lambda,map,filter,reduce are the advance function
# def fun():print('hello world')
# fun()

# Lambda Function
add = lambda a,b:a+b
print(add(10,20))


# Map Function
listt = [1,2,3,4,5,6,7,8]
square = list(map(lambda x:x**2,listt))
print(square)


# Filter Function
lis = [1,2,3,4,5,6,7,8]
even = list(filter(lambda a:a%2==0,lis))
print(even)

# Reduce Function
from functools import reduce
compare = lambda a,b:(a)if a>b else (b)    #this is the method of writing the condition in one line statement
max = reduce(compare,lis)       #will return max from the list by applying the loop
print(max)


list1 = [1,2,3,4]
list2 = [2,4,6,8]

sum = list(map(lambda f,g:f+g,list1,list2))
print(sum)

