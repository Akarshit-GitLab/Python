# waf to find in which line of the file does the word "learning occur first"
def find_word():
    word ="learning"
    data = True
    
    line_no =1
    with open("practice.txt" ,"r" ) as f:
        while data:
            data = f.readline()
            if(word in data):
                print("found in line number = ",line_no)
                return
            line_no +=1
    return -1
print(find_word())
         
        

