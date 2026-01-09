lst = [3,8,4,8,5,8,6,7,8]

mx = lst[0]

for i in lst:
    if i> mx :
        mx = i

count =0

for i in lst:
    if i == mx:
        count += 1

print("Maximum:",mx)
print("Count:", count)