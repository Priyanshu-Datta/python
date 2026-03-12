import math 

dic = {"a": 5, "b": 7, "c": 4, "d": 6}

for k in dic:
    dic[k] = math.factorial(dic[k])

print(dic)