# 8. Squares of even numbers from 1 to 10
evens = [x**2 for x in range(1, 11) if x % 2 == 0]
print(evens)

# 9. Simple class
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")

p = Person("Alice")
p.greet()


# 10. Handle division by zero
try:
    x = 5 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
