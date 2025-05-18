n = int(input())
a = [tuple(map(int, input().split())) for i in range(n)]
t = set(a)
assert len(t) == len(a)
minans = 1000000000000
for i in range(n):
    for j in range(i + 1, n):
        r = t.copy()
        p = a[i][0] - a[j][0]
        q = a[i][1] - a[j][1]
        curans = 0
        while r:
            curans += 1
            m = r.pop()
            z = m
            while (m[0] + p, m[1] + q) in r:
                m = (m[0] + p, m[1] + q)
                r.remove(m)
            m = z
            while (m[0] - p, m[1] - q) in r:
                m = (m[0] - p, m[1] - q)
                r.remove(m)
        minans = min(minans, curans)
if minans == 1000000000000:
    print(1)
else:
    print(minans)