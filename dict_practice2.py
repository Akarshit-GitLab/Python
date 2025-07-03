# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
# an empty dictionary & add one by one. Use subject name as key & marks as value.


dictionary = {}
chem = float(input("enter marks of chemistry : "))
dictionary.update({"chemistry " : chem})

phy = float(input("enter marks of physics : "))
dictionary.update({"physics " : phy})


math = float(input("enter marks of math : "))
dictionary.update({"mathematics " : math})

print(dictionary)
