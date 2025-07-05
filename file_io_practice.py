# create a new file using python and write into it 
# with open("practice.txt","w") as f:
#     f.write("hi Everyone \nwe are learning java File i/o")
#     f.write("using java \ni like programming in java")



# now replace all occurance of java in python 
with open("practice.txt","r") as f:
    data = f.read()
new_data = data.replace("java","python")

print(new_data)
with open("practice.txt","w") as f:
    f.write(new_data)