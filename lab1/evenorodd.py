lst = [1,3,2,4,6,5,8,3,5,6,9,12]

even =[]
odd =[]

for i in lst:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("even numbers ",even)
print("odd numbers ",odd)
