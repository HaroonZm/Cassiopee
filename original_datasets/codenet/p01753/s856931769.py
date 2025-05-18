N, Q = map(int, input().split())
x = [None] * N
y = [None] * N
z = [None] * N
r = [None] * N
l = [None] * N
for i in range(N):
    x[i], y[i], z[i], r[i], l[i] = map(int, input().split())

for _ in range(Q):
    ans = 0
    sx, sy, sz, dx, dy, dz = map(int, input().split())
    vx = dx - sx
    vy = dy - sy
    vz = dz - sz
    for i in range(N):
        t = 0
        t += vx * (x[i] - sx)
        t += vy * (y[i] - sy)
        t += vz * (z[i] - sz)
        t /= vx**2 + vy**2 + vz**2
        len2 = 0
        len2 += (sx + vx * t - x[i])**2
        len2 += (sy + vy * t - y[i])**2
        len2 += (sz + vz * t - z[i])**2
        if 0 < t < 1 and len2 <= r[i]**2 + 1e-9:
            ans += l[i]
    print(ans)