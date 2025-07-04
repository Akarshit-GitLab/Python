# # waf to find the factorial of n 
def factorial(n):
    i =1
    fact =1
    while(i<=n):
        fact *= i
        i += 1
    print(fact)
    return fact
n = int(input("enter the number : "))
factorial(n)

# waf to convert usd to inr
def convert(us):
    us = 83* us
    # print(usd)
    return us
usd = int(input(" enter the us dollor : "))
print("rs",convert(usd))