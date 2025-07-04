# waf to print the length of list (list  is parameter)
# def length_list(a):
#     print(len(a))
#     return a
# list = [1,2,3,4,5,6,7,8,9]
# length_list(list)


# -----> waf to print the element of list in single line (list is parameter)<-------

def length_list(a):
    
    for i in range(0,len(a),1):
        print(list[i], end= " ")

    return a
list = [1,2,3,4,5,6,7,8,9]
length_list(list)
