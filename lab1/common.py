lst1 = [2,4,6,7,5,8]
lst2 =[3,2,4,2,9,7]

common =[]

for i in lst1:
    if i in lst2:
        common.append(i)

print(common)