# 5. Count frequency of each character in a string
text = "banana"
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1
print(freq)

# 6. Write & read from a file
with open("example.txt", "w") as f:
    f.write("Hello Python!\nSecond line.")
with open("example.txt", "r") as f:
    print(f.read())

# 7. Fibonacci sequence up to n terms
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(10)
