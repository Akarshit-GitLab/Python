# wap to find factorial of n number input by user 
n =int(input("enter the number : "))
fact =1
for i in range(1,n+1,1):
    fact = fact *i

print(fact)