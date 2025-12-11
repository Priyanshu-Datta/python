lst = [5,10,15,20]
largest =second= lst[0]


for i in lst:
    if i>largest:
        second = largest
        largest = i
    elif i>second and i!= largest:
        second = i
print("the second largest elment ",second )

