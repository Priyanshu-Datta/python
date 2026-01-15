t = (2,4,3,6,5,1,9,8)

s =0
for i in t:
    s += i

avg = s/len(t)

largest = largest2 = t[0]
for i in t:
    if i > largest:
        largest2 = largest
        largest = i
    elif i > largest2:
        largest2 = i

print("SUM: ",s)
print("Average:",avg)
print("Second largest:", largest2)
