lst = [9,7,4,6,3,2,8]
reversed_list = []

for i in range(len(lst)-1, -1, -1):
    reversed_list.append(lst[i])

print(reversed_list)
