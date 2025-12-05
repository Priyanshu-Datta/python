lst = [1,2,1,2,3,4,3,4]

freq = {}

for i in lst:
    if i in freq:
        freq[i] += 1
    else:
        freq[i]=1

print("frequency",freq)
