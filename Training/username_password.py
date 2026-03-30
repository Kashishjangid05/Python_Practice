username = 'arya@123'
password = 'arya1234'

x = input("Enter username")
y = input("Enter password")

# if-elif-else conditional statement
# if(x == username and y == password):
#     print("Both are correct")
# elif(x != username and y != password):
#     print("Both are invalid")
# elif(x == username and y!= password):
#     print("Password is incorrect")
# else:
#     print("username is incorrect")

# nested if-else conditional statement
if(x == username):
    if(y == password):
        print("Both are correct")
    else:
        print("Password is incorrect")
else:
    if(y==password):
        print("Username is incorrect")
    else:
        print("Both are invalid")