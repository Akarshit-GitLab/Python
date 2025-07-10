# Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.
class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum =0
        for val in self.marks:
            sum += val
        print("hi",self.name,"you marks avg = ",sum/3)

s1 =student("akarshit",[94,95,99])
s1.get_avg()