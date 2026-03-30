# try:
#     name = input("Enter your name:")
#     age = int(input("Enter your age:"))

# except ValueError:
#     print("Give correct input")

# else:
#     print(f"My name is {name} and age is {age}")

# finally:
#     print("successfully executed")


num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))

try:
    res = num1/num2

except Exception as msg:
    print(msg)

else:
    print(f"The division value is {res}")

finally:
    print("successfully executed")
