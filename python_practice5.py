# 4. Remove duplicates from a list
lst = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(lst))
print(unique)

# 5. Check if a string contains all vowels
text = "education"
vowels = set('aeiou')
if vowels.issubset(set(text)):
    print("All vowels are present")
else:
    print("Not all vowels")
    

# 6. Find all even numbers between 1 and 100
evens = [x for x in range(1, 101) if x % 2 == 0]
print(evens)
