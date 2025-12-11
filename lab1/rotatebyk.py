lst = [2,4,1,5,3,6,7,3]

k = int(input("enter a position "))
rotated = []

for i in range(k,len(lst)):
    rotated.append(lst[i])

for i in range(k):
    rotated.append(lst[i])

print(rotated)