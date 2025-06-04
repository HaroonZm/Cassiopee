import sys

input = sys.stdin.readline

n, q = map(int, input().split())

Len = (n - 1).bit_length()
size = 2 ** Len
tree = [0] * (2 * size)
lazy = [None] * (2 * size)
h = [None]
for i in range(Len + 1):
    v = 2 ** (Len - i)
    h += [v] * (2 ** i)

def gindex(l, r):
    L = (l + size) >> 1
    R = (r + size) >> 1
    lc = 0 if l & 1 else (L & -L).bit_length()
    rc = 0 if r & 1 else (R & -R).bit_length()
    for i in range(Len):
        if rc <= i:
            yield R
        if L < R and lc <= i:
            yield L
        L >>= 1
        R >>= 1

def propagates(ids):
    for i in reversed(ids):
        v = lazy[i]
        if v is None:
            continue
        lazy[2 * i] = tree[2 * i] = lazy[2 * i + 1] = tree[2 * i + 1] = v // 2
        lazy[i] = None

def update(l, r, x):
    *ids, = gindex(l, r)
    propagates(ids)
    L = size + l
    R = size + r
    while L < R:
        if R & 1:
            R -= 1
            lazy[R] = tree[R] = x * h[R]
        if L & 1:
            lazy[L] = tree[L] = x * h[L]
            L += 1
        L >>= 1
        R >>= 1
    for i in ids:
        if 2 * i + 1 < size * 2:
            tree[i] = tree[i * 2] + tree[i * 2 + 1]

def query(l, r):
    *ids, = gindex(l, r)
    propagates(ids)
    L = size + l
    R = size + r
    s = 0
    while L < R:
        if R & 1:
            R -= 1
            s += tree[R]
        if L & 1:
            s += tree[L]
            L += 1
        L >>= 1
        R >>= 1
    return s

ans = []
for i in range(q):
    a, *b = map(int, input().split())
    if a:
        ans.append(query(b[0], b[1] + 1))
    else:
        update(b[0], b[1] + 1, b[2])
print('\n'.join(map(str, ans)))