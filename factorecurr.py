def fact(n):
    if(n<0):
        print("factorial of negative numbers does not exists")
        exit()
    if(n<1):
        return 1
    else:
        return n*fact(n-1)
n = int(input("enter number"))
facto=fact(n)
print("factorial of %d is: %d" % (n,facto))