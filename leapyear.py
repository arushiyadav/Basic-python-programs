n = int(input("enter a year"))
if((n%4==0 or n%400==0)):
    print("%d is a leap year" % n)
elif(n%100==0):
    print("%d is not a leap year" % n)
else:
    print("%d is not a leap year" % n)