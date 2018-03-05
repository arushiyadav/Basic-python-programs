x = int(input('enter a number'))
r = 0
for value in range(2,x):
    r = x%value
    if(r==0):
        break
else:
    print("prime")
    exit()    
print("not prime")        