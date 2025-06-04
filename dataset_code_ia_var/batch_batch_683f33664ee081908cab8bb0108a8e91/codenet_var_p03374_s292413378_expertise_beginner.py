N, C = map(int, input().split())
xs = [0]
ys = [0]
vs = [0]
us = [0]
ws = [0]

for i in range(N):
    x, v = map(int, input().split())
    prev_us = us[-1]
    prev_x = xs[-1]
    us.append(prev_us + v - x + prev_x)
    vs.append(v)
    xs.append(x)

for i in range(N, 0, -1):
    y = C - xs[i]
    prev_ws = ws[-1]
    prev_vs = vs[i]
    prev_ys = ys[-1]
    ws.append(prev_ws + prev_vs - y + prev_ys)
    ys.append(y)

zs = [0]*(N+1)
c = 0
r = 0
for i in range(len(us)):
    if c <= us[i]:
        c = us[i]
        ci = i
        if r < c:
            r = c
    zs[i] = (c, ci)

zs2 = [0]*(N+1)
c = 0
for i in range(len(ws)):
    if c <= ws[i]:
        c = ws[i]
        ci = i
        if r < c:
            r = c
    zs2[i] = (c, ci)

for z, zi in zs:
    idx = N - zi
    if 0 <= idx < len(zs2):
        c = z + zs2[idx][0] - xs[zi]
        if r < c:
            r = c

for z, zi in zs2:
    idx = N - zi
    if 0 <= idx < len(zs):
        c = z + zs[idx][0] - ys[zi]
        if r < c:
            r = c

print(r)