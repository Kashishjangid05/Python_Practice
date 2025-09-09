#sets concepts
set1 = {1,2,3,4,5,"hello"}
print(set1)
print(type(set1))
print(len(set1))

set2 = {1,2,3,2,4,3,2,"world"}#set remove the duplicate values
print(set2)
print(type(set2))
print(len(set2))

set3 = {}#to create empty set this is not correct it will treated as dictionary
set4 = set()#correct way of creating empty set
print(type(set3))
print(type(set4))

#methods
set4.add(1)
set4.add(2)
set4.add(3)
set4.add(3)
set4.add((8,7,9))#can add tuples but not lists
print(set4)

set4.remove(1)
print(set4)

print(len(set4))
set4.clear()
print(len(set4))

print(set1.pop())#pop delete element randomly on its own
print(set1)
print(set1.pop())
print(set1)

set5 = {1,2,3}
set6 = {2,3,4}
print(set5.union(set6))
print(set5.intersection(set6))