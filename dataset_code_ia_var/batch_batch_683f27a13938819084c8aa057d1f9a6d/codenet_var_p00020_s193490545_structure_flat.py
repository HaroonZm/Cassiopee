import sys
a = 'abcdefghijklmnopqrstuvwxyz'
b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for s in sys.stdin:
    t = ''
    for c in s[:-1]:
        if c in a:
            t += b[a.index(c)]
        else:
            t += c
    print(t)