student = {
    "maths": 85,
    "Physics": 90,
    "Chemistry": 78,
    "computer": 92
}
print("Original Dictionary:")
for key, value in student.items():
    print(f"{key}: {value}")

total = sum(student.values())
avg = total / len(student)
print("total:", total)
print("average:", avg)