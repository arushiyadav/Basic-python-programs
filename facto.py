n = int(input("enter a number"))
if(n<0):
    print("factorial of negative numbers does not exists")
    exit()
elif(n<1):
    fact=1
else:
    fact=1
    for i in range(1,n+1):
        fact=fact*i
print("factorial of %d is %d" %(n,fact))