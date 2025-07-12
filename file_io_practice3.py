# from a file conataining number seprated by comma, print th count of even numbers

count =0
with open("practice.txt" ,"r") as f:
    data = f.read()
    nums =data.split(",")
    for val in nums:
        if(int(val) %2 == 0):
            count += 1

            print("hello")
print(count)