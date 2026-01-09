s = "madam"
rev = ""

for ch in s:
    rev = ch + rev

if s == rev:
    print("it is palindrome")
else:
    print("not a palindrome")
