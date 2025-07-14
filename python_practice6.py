# 7. Find factorial of a number using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

# 8. Create a simple counter using a generator
def counter():
    n = 0
    while True:
        yield n
        n += 1

c = counter()
for _ in range(5):
    print(next(c))
