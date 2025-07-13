# 1. Print a triangle pattern of stars
for i in range(1, 6):
    print('*' * i)

# 2. Reverse a string
s = "hello"
print(s[::-1])

# 3. Sum of all elements in a list

numbers = [1, 2, 3, 4, 5]
print(sum(numbers))

# 4. Check if a number is prime
n = 29
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} is not prime")
            break
    else:
        print(f"{n} is prime")
