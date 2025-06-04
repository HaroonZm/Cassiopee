a = input()
b = ""
for c in a:
    if c.islower():
        b += c.upper()
    elif c.isupper():
        b += c.lower()
    else:
        b += c
print(b)