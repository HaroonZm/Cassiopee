str_in = input()
str_out = ""
for c in str_in:
    if c.islower():
        str_out += c.upper()
    elif c.isupper():
        str_out += c.lower()
    else:
        str_out += c
print(str_out)