#WAP to find the factorial of n using function

def fact( n ):
    mult = 1
    for i in range(1,n+1):
        mult *= i
    print(mult)
fact(5)

# WAP to convert usd to inr
# 1 usd = 83 ruppes
def usd(n):
    x = n * 83
    print("the indian ruppee are",x)
usd(2)

# WAP to find odd and even using function
def odd_even(num):
    if num % 2 == 0:
        print("EVEN")
    else:
        print("ODD")

odd_even(3)
odd_even(6)