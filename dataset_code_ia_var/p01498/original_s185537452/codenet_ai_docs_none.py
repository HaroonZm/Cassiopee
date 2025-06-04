from collections import defaultdict
N, W, H = map(int, input().split())
*p, = range(N)
def root(x):
    if x == p[x]:
        return x
    p[x] = y = root(p[x])
    return y
def unite(x, y):
    px = root(x); py = root(y)
    if px < py:
        p[py] = px
    else:
        p[px] = py
X = defaultdict(list)
Y = defaultdict(list)
for i in range(N):
    x, y = map(int, input().split())
    X[x].append(i)
    Y[y].append(i)
for x, vs in X.items():
    prv = vs[0]
    for v in vs[1:]:
        unite(prv, v)
        prv = v
for y, vs in Y.items():
    prv = vs[0]
    for v in vs[1:]:
        unite(prv, v)
        prv = v
cnt = 0
for i in range(N):
    pt = root(i)
    if pt == i:
        cnt += 1
ans = N-cnt + 2*(cnt-1)
if cnt > 1 and 1 not in X and W not in X and 1 not in Y and H not in Y:
    ans += 1
print(ans)