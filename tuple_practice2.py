# wap to check if a list contain a plaindrome of elements.
list1 =[1,2,3,2,1]
# list_copy =list1.copy()

list_reverse =list1
list_reverse.reverse()
if(list1 == list_reverse):
    print("this is plindrome")
else:
    print("this is not")


    # we can use copy() method also