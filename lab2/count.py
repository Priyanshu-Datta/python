s = "I am Priyanshu Datta 21"
vowels = "aeiouAEIOU"

v=c=d=sp=0

for ch in s:
    if ch in vowels:
        v += 1
    elif ch.isalpha():
        c += 1
    elif '0' <= ch <='9':
        d += 1
    else:
        sp += 1

print("Vowels:",v)
print("Alphabet:",c)
print("digits:",d)
print("spaces:",sp)