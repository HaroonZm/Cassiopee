a = input()
b = input()
s = "NYOE S"
if a[0] == b[2] and a[1] == b[1] and a[2] == b[0]:
    print(s[0::2])
else:
    print(s[1::2])