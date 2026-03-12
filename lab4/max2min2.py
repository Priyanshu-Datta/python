dic = {"a": 10, "b": 40, "c": 30, "d": 20}
values = sorted(dic.values())
second_min = values[1]
second_max = values[-2]

print("Second Minimum Value:", second_min)
print("key:",[k for k, v in dic.items() if v == second_min])
print("Second Maximum Value:", second_max)
print("key:",[k for k, v in dic.items() if v == second_max])
