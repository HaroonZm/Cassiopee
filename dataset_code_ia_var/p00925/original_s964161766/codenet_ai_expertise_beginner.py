s = input()
c = int(input())
a = eval(s)
b = int(s[0])
i = 1
while i < len(s):
    if s[i] == '+':
        b = b + int(s[i+1])
    else:
        b = b * int(s[i+1])
    i = i + 2
if a == b and b == c:
    e = 'U'
elif a == c:
    e = 'M'
elif b == c:
    e = 'L'
else:
    e = 'I'
print(e)