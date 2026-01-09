s = " I am learning python Programing"

word = ""
longest= ""

for ch in s:
    if ch != " ":
        word += ch
    else:
        if len(word) > len(longest):
            longest = word
        word = ""

if len(word) > len(longest):
    longest = word
print(longest)