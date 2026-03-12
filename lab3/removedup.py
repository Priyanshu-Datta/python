def remove_duplicates(lst):
    lst2 = []
    for item in lst:
        if item not in lst2:
            lst2.append(item)
    print(lst2)

lst = [1,2,3,4,3,2,1,5,6,7,8,7,6,5]
remove_duplicates(lst)