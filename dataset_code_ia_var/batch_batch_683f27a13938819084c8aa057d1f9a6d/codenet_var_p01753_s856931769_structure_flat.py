NQ = input().split()
N = int(NQ[0])
Q = int(NQ[1])
x = [None] * N
y = [None] * N
z = [None] * N
r = [None] * N
l = [None] * N
i = 0
while i < N:
    arr = input().split()
    x[i] = int(arr[0])
    y[i] = int(arr[1])
    z[i] = int(arr[2])
    r[i] = int(arr[3])
    l[i] = int(arr[4])
    i += 1
q_iter = 0
while q_iter < Q:
    ans = 0
    arr = input().split()
    sx = int(arr[0])
    sy = int(arr[1])
    sz = int(arr[2])
    dx = int(arr[3])
    dy = int(arr[4])
    dz = int(arr[5])
    vx = dx - sx
    vy = dy - sy
    vz = dz - sz
    i = 0
    while i < N:
        t = 0
        t += vx * (x[i] - sx)
        t += vy * (y[i] - sy)
        t += vz * (z[i] - sz)
        denom = vx**2 + vy**2 + vz**2
        if denom != 0:
            t /= denom
        else:
            t = 0
        lx = sx + vx * t - x[i]
        ly = sy + vy * t - y[i]
        lz = sz + vz * t - z[i]
        len2 = 0
        len2 += lx**2
        len2 += ly**2
        len2 += lz**2
        if t > 0 and t < 1 and len2 <= r[i]**2 + 1e-9:
            ans += l[i]
        i += 1
    print(ans)
    q_iter += 1