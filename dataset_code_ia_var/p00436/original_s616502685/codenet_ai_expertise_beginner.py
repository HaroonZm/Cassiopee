n = int(input())
s = []
for i in range(1, 2 * n + 1):
    s.append(i)
m = int(input())
for k in range(m):
    a = int(input())
    if a != 0:
        t = []
        for i in range(a, 2 * n):
            t.append(s[i])
        for i in range(0, a):
            t.append(s[i])
        s = t
    else:
        t = []
        for i in range(n):
            t.append(s[i])
            t.append(s[i + n])
        s = t
for x in s:
    print(x)