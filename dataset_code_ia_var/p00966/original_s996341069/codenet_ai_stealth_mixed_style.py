from bisect import bisect as B

N, A, Bn, Q = [int(e) for e in input().split()]
W = []
for j in range(A):
    u = input().split()
    W.append(u)
xs, cs = [], []
for e in W:
    xs.append(int(e[0]))
    cs.append(e[1])

ps = []
for _ in range(Bn):
    ps.append(tuple(map(int, input().split())))

ys = [p[0] for p in ps]
ys.append(N + 1)

ds = [None] * Bn
for idx in range(Bn):
    y,h = ps[idx]; nxt = ys[idx+1]
    ds[idx] = min(y-h, nxt-y)

lookup = dict()
ct=0
while ct<A:
    x, c = xs[ct], cs[ct]
    lookup[x] = c
    if x < ys[0]:
        ct += 1
        continue
    u = 0
    while ys[u+1] <= x: u += 1
    v = u
    while ys[0] <= x:
        while x < ys[v]: v -= 1
        y0, h = ps[v]
        if not h: break
        x = h + ((x - y0) % ds[v])
        lookup[x] = c
    ct += 1

def solve(z):
    while True:
        if z in lookup: return lookup[z]
        i = B(ys, z) - 1
        while ys[0] <= z:
            while z < ys[i]: i -= 1
            y0, h = ps[i]
            if h == 0: break
            z = h + ((z - y0) % ds[i])
            if z in lookup: return lookup[z]
        return '?'

print(*(solve(int(input())) for _ in range(Q)), sep='')