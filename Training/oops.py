# instance method (takes first argument)
class A:
    def hello(self):
        return "hii world"
x = A()
print(x.hello())

# classmethod (takes first argument)
class B:
    @classmethod
    def fun(cls):
        return "qwerty"
y = B()
print(y.fun())

# static method (does not take first argument)
class C:
    @staticmethod
    def func():
        return "abcd"
z = C()
print(z.func())

