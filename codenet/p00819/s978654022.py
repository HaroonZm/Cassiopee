funcs = {
    'J': lambda s: s[-1:]+s[:-1],
    'C': lambda s: s[1:]+s[0],
    'E': lambda s: s[(len(s)+1)//2:]+s[len(s)//2:(len(s)+1)//2]+s[:len(s)//2],
    'A': lambda s: s[::-1],
    'P': lambda s: s.translate(str.maketrans('0123456789', '9012345678')),
    'M': lambda s: s.translate(str.maketrans('0123456789', '1234567890')),
}
n = int(input())
for i in range(n):
    s, t = [input().strip() for j in '01']
    for c in s[::-1]:
        t = funcs[c](t)
    else:
        print(t)