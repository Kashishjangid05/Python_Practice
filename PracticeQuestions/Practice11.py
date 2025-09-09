#WAP to check if the list is pallindrome or not
list1 = [1 , 2 , 1]
list2 = [1 , 2 , 3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):{
    print("list1 is pallindrome")
}
else:{
    print("list 1 is not pallindrome")
}

copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list2 == list2):
    print("list2 is pallindrome")
else:
    print("list2 is not pallindrome")