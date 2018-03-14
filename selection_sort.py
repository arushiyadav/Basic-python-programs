from arrayinput import array,x
for i in range(0,x-1):
    small=array[i]
    for j in range(i+1,x):
        if (small>array[j]):
            small=array[j]
            temp=array[i]
            array[i]=array[j]
            array[j]=temp
    array[i]=small
    print("sorted array:",array) 