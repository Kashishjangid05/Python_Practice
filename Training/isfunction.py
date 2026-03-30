s = "124helloworld"
print(s.isalnum())

a = 'he    llo'
print(a.isspace())
b = " "
print(b.isspace())
c = "1234"
print(c.isdecimal())
print(c.isdigit())
print(c.isnumeric())
print(c.isspace())

z = "HELLO"
print(s.isupper())
print(z.isupper())

print('-'.join(s))

lis = ['hello','world','python']
print(" ".join(lis))