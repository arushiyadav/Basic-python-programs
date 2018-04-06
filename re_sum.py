import re
count = 0
s = 0
n = "text.txt"
txt = open(n,'r')
t = txt.read()
li = re.findall("[0-9]+", t)
for no in li:
    print(no,end = " ")
    count=count+1
print("\n total numbers",count)
for n in li:
    i = int(n)
    s = s + i
print("\n sum is :",s)    
    

