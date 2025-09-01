# Prints all letters except "s" and "e"
i =0
a= "students"
while i < len(a):
    if a[i] == "s" or a[i] == "e":
        i += 1
        continue
    print(a[i])
    i += 1


