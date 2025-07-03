# print the elements of the list using for loop
# [1,4,9,16,25,36,49,64,81,100]

list =[1,4,9,16,25,36,49,64,81,100]
val =0
for val in list :
    print(val)
    val =+1
else:
    print("end")

    #  search for x in tupple

tup = (1,4,9,16,25,36,49,64,81,100)
x = 36 
for i in tup:
    if( i == 36):
        print("x found")
        break
    print(i)
    i =+ 1
