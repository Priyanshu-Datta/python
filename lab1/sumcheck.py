lst=[1,3,2,4,5,9,6,7,8]

target= int(input("enter the no "))

for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i] +lst[j] ==target:
            print(lst[i],lst[j])
            