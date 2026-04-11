# x = 100
# def change_x():
#     global x
#     x += 10          #unboundLocalError as global variable cant be changed or updated
#     print(f"{x}")
# print(f"{x}")
# change_x()
# print(f"{x}")
# 


x = 200              #global variable
def change_x():
    x = 300          #local variable
    print(f"{x}")    #will print local variable(300)

print(f"{x}")        #will print global variable as it cant be updated(200)
change_x()
print(f"{x}")        #will also print global variable(200)
