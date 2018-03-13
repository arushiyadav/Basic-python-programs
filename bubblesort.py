from arrayinput import array,x
print("**bubble sort**")
for i in range(0,x):
    i=0
    j=0
    for j in range(i+1,x):
        if(array[i]>array[j]):
            temp=array[i]
            array[i]=array[j]
            array[j]=temp
        j+=1
        i+=1
print("sorted array is:",array)