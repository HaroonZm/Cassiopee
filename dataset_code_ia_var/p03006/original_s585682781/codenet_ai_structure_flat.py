n = int(input())
a = []
for i in range(n):
    x, y = map(int, input().split())
    a.append((x, y))
t = set(a)
assert len(t) == len(a)
minans = 1000000000000
i = 0
while i < n:
    j = i + 1
    while j < n:
        r = set(t)
        p = a[i][0] - a[j][0]
        q = a[i][1] - a[j][1]
        curans = 0
        while r:
            curans += 1
            m = r.pop()
            z0, z1 = m[0], m[1]
            m0, m1 = z0, z1
            while (m0 + p, m1 + q) in r:
                m0 += p
                m1 += q
                r.remove((m0, m1))
            m0, m1 = z0, z1
            while (m0 - p, m1 - q) in r:
                m0 -= p
                m1 -= q
                r.remove((m0, m1))
        if curans < minans:
            minans = curans
        j += 1
    i += 1
if minans == 1000000000000:
    print(1)
else:
    print(minans)