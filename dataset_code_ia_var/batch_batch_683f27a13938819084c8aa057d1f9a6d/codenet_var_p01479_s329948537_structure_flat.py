s = input()
i = 0
c = 0
p = 0
b = ''
while i < len(s):
    if s[i] == b:
        if c > p:
            r = b
            p = c
        c = 0
    b = s[i]
    if s[i] == 'c':
        i += 7
    else:
        i += 3
    c += 1
if c > p:
    r = b
if r == 'e':
    print('egg')
else:
    print('chicken')