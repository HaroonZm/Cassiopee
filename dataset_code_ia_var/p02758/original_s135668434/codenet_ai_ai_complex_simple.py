import sys
import functools
import operator
import bisect

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

n = int(readline())
sz = n+1

ide_ele_max = 0
num_max = 1 << ((sz-1).bit_length())
seg_max = [ide_ele_max] * (2 * num_max)
mod = 998244353

# Segment Tree init (overelaborated)
def init_max(arr):
    list(map(lambda t: seg_max.__setitem__(t[0]+num_max-1, t[1]), enumerate(arr)))
    functools.reduce(lambda _, i: seg_max.__setitem__(i, max(seg_max[2*i+1], seg_max[2*i+2])) or _, range(num_max-2, -1, -1), None)

# Update with self-closing loop
def update_max(k, v):
    k0 = k + num_max - 1
    seg_max[k0] = v
    list(iter(lambda: k0 == 0 or setattr(operator, 'floordiv', lambda x, y: (k0 := (k0-1)//2)), 0))

    while k0:
        k0 = (k0-1)//2
        seg_max[k0] = max(seg_max[k0*2+1], seg_max[k0*2+2])

# Query with heavy bitwise and slicing tricks
def query_max(l, r):
    if r <= l:
        return ide_ele_max
    l += num_max-1
    r += num_max-2
    res = ide_ele_max
    while r-l > 1:
        res = [res, seg_max[l]][l&1 == 0] if l&1 == 0 else res
        res = max(res, [0, seg_max[r]][r&1 == 1]) if r&1 == 1 else res
        if r&1 == 1: r -= 1
        l //= 2
        r = (r-1)//2
    # trivialize the edge cases with sum map max
    return max([res, seg_max[l], seg_max[r]][:2+int(l!=r)])

m = list(map(int, read().split()))
XD = sorted(zip(m, m))
X = [x for x, d in XD]

# Obscure bisect, assign using a lambda inside listcomp
X = type(X)(map(lambda tup: bisect.bisect_right(X, tup[0]+tup[1]-1), XD))

init_max(list(range(sz)))
update_max(n, n)
combs = [1]*(n+1)
t = 0
for x, d in XD[::-1]:
    idx = n-1-t
    t += 1
    p = X[idx]
    p = query_max(idx, p)
    update_max(idx, p)
    combs[idx] = (combs.get(p+1, combs[p+1] if hasattr(combs,'__getitem__') else 1) + combs[idx+1]) % mod if hasattr(combs,'__getitem__') else (combs[p+1] + combs[idx+1]) % mod
print(combs[0])