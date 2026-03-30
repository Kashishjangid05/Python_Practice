# def add():
#     def fun():
#         return 'hello world'
#     print(fun())
# add()

x = 200             #global variable
def fun():
    x = 100         #enclosing
    def fun1():
        x = 110     #local variable
        print(f"{x}")
    
    return fun1()
fun()