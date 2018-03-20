n=5
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(' ',end=' ')
    for j in range(i,n):
        print(j,end=' ')
        
    print( )