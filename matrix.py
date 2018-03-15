m1=[[1,2,3], [4,5,4],[1,2,3]]
m2=[[3,2,4], [6,5,4],[1,2,3]]
print(m1)
print(m2)
print("**ADDITION**")
s=[[0,0,0], [0,0,0],[0,0,0]]
for i in range(len(m1)):
    for j in range(len(m2)):
        s[i][j] = m1[i][j] + m2[i][j]
print(s)
print("**SUBTRACTION**")
s=[[0,0,0], [0,0,0],[0,0,0]]
for i in range(len(m1)):
    for j in range(len(m2)):
        s[i][j]=m1[i][j]-m2[i][j]
print(s)
print("MULTIPLICATION")
s=[[0,0,0], [0,0,0],[0,0,0]]
for i in range(len(m1)):
    for j in range(len(m2)):
        for k in range(len(m2)):
            s[i][j] = s[i][j] + (m1[i][k] * m2[k][j]) 
print(s)