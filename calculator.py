def add(a,b):
    r = a+b
    print("result",r)
def sub(a,b):
    r=a-b
    print("result",r)
def mul(a,b):
    r=a*b
    print("result",r)
def div(a,b):
    r=a/b
    print("result",r)
def mod(a,b):
    r=a%b
    print("result",r)
def power(a,b):
    r=a**b
    print("result",r)
op1 = int(input("enter the the first operand"))
op2 = int(input("enter the second operand"))
opr = input("enter the operation u want to perform")
if(opr=="add"):
    add(op1,op2)
elif(opr=="subtract"):
    sub(op1,op2)
elif(opr=="multiply"):
    mul(op1,op2)
elif(opr=="divide"):
    div(op1,op2)
elif(opr=="modulo"):
    mod(op1,op2)
elif(opr=="power"):
    power(op1,op2)   
    

