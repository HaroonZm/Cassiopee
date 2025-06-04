x = str(input())
x_upper = ""
for c in x:
    if 'a' <= c <= 'z':
        x_upper += chr(ord(c) - 32)
    else:
        x_upper += c
print(x_upper)