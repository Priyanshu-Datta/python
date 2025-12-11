lst =[1,2,2,1,3,4,3,4]
unique=[]

for i in lst:
    if i not in unique:
        unique.append(i)

print("unique numbers ",unique)
