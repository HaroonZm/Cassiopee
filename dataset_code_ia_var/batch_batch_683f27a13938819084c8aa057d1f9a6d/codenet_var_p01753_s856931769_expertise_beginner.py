n, q = map(int, input().split())
x = []
y = []
z = []
r = []
l = []
for i in range(n):
    a, b, c, d, e = map(int, input().split())
    x.append(a)
    y.append(b)
    z.append(c)
    r.append(d)
    l.append(e)

for i in range(q):
    sx, sy, sz, dx, dy, dz = map(int, input().split())
    vx = dx - sx
    vy = dy - sy
    vz = dz - sz
    ans = 0
    for j in range(n):
        t = vx * (x[j] - sx) + vy * (y[j] - sy) + vz * (z[j] - sz)
        den = vx * vx + vy * vy + vz * vz
        t = t / den
        lx = sx + vx * t - x[j]
        ly = sy + vy * t - y[j]
        lz = sz + vz * t - z[j]
        len2 = lx * lx + ly * ly + lz * lz
        if t > 0 and t < 1 and len2 <= r[j] * r[j] + 1e-9:
            ans = ans + l[j]
    print(ans)