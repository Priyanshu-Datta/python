def total(tup):
    s = 0
    for t in tup:
        s += t
    return s

def avg(tup):
    s = total(tup)
    a = s/len(tup)
    print("Average:",a)

tup =(2,4,3,6,4,7,9,5,7,1)
print("Sum:",total(tup))
avg(tup)