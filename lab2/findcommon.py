t1 = (1,2,3,4,5,6)
t2 =(2,4,6,7,8,9)
comm = []
for i in t1:
    if i in t2:
        comm.append(i)

print(comm)