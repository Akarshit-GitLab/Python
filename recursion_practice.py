# write a recursive function to calculate the sum of first n natural numbers 

def sum_cal(n):
    if(n == 0):
        return 0
    return sum_cal(n-1) + n
sum = sum_cal(5)
print(sum)

# write a recursive function to print all elements in a list 

def print_list(list,idx =0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
list= [1,2,3,4,5,6,7,8,9]
print_list(list)



