from itertools import accumulate

N, C = map(int, input().split())
xs = [0]
ys = [0]
vs = [0]
us = [0]
ws = [0]

for i in range(N):
    x, v = map(int, input().split())
    us.append(us[-1] + v - x + xs[-1])
    vs.append(v)
    xs.append(x)

for i in range(N, 0, -1):
    y = C - xs[i]
    ws.append(ws[-1] + vs[i] - y + ys[-1])
    ys.append(y)

zs = [0] * (N + 1)
c = 0
r = 0
for i, u in enumerate(us):
    if c <= u:
        c, ci = u, i
        r = max(r, c)
    zs[i] = (c, ci)

zs2 = [0] * (N + 1)
c = 0
for i, u in enumerate(ws):
    if c <= u:
        c, ci = u, i
        r = max(r, c)
    zs2[i] = (c, ci)

for z, zi in zs:
    c = z + zs2[N - zi][0] - xs[zi]
    r = max(r, c)

for z, zi in zs2:
    c = z + zs[N - zi][0] - ys[zi]
    r = max(r, c)

print(r)