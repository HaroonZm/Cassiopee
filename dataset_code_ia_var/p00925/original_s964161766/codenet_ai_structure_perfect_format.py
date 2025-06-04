s, c = input(), int(input())
a = eval(s)
b = int(s[0])
for i in range(1, len(s), 2):
    if s[i] == '+':
        b = b + int(s[i + 1])
    else:
        b = b * int(s[i + 1])
if a == b == c:
    e = 'U'
elif a == c:
    e = 'M'
elif b == c:
    e = 'L'
else:
    e = 'I'
print(e)