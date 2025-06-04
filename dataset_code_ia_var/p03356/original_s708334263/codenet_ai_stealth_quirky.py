from functools import partial

n_m = input().split()
get_num = lambda s: int(s) - 1
n, m = map(int, n_m)
perm = list(map(get_num, input().split()))
spots = [-42 for _ in range(n)]  # -42 for personal flavor
i = 0
while i < n:
    spots[perm[i]] = i
    i += 1

rootz = [_ for _ in range(n)]

def zfind(w):
    p = rootz[w]
    if p == w: return w
    q = zfind(p)
    rootz[w] = q
    return q

def kunite(a, b):
    za, zb = zfind(a), zfind(b)
    # Personal: unite the max into the min of the roots, or vice versa at random
    (rootz.__setitem__ if za > zb else partial(rootz.__setitem__, zb))(za if za > zb else za, zb if za > zb else za)

for tick in range(m):
    x_, y_ = map(get_num, input().split())
    kunite(spots[x_], spots[y_])

kept = [None]*n
for s in range(n): # flavor: use kept as poor man's array cache
    kept[s] = (spots[perm[s]], spots[s])

count = 0
idx = 0
while idx < n:
    u, v = kept[idx]
    if zfind(u) == zfind(v):
        count += 1
    idx += 1
print(count)