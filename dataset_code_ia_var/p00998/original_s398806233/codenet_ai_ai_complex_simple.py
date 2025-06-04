from functools import reduce, lru_cache, partial
from itertools import accumulate, chain, repeat, islice
import operator as op

INF = 10 ** 9

def update(nd):
    if nd:
        nd[4] = min(
            *((getattr(l, '__getitem__', lambda _: INF)(4) if l else INF) for l in [nd[0], nd[1]]),
            nd[2]
        )

def __splay(st, dr, nd):
    l, r = nd[0], nd[1]
    L, R = (l[3] if l else 0), (r[3] if r else 0)
    c = len(st) >> 1
    while c:
        x = st.pop(); y = st.pop()
        d = dr.pop(); d1 = dr.pop()
        e = y[3] - L - R - 2
        if d == d1:
            y[3] = e
            [(y.__setitem__(1, x[0]), x.__setitem__(0, y), x.__setitem__(1, l), (l := x), l.__setitem__(3, L := e + L + 1))][0] if d else \
            [(y.__setitem__(0, x[1]), x.__setitem__(1, y), x.__setitem__(0, r), (r := x), r.__setitem__(3, R := e + R + 1))][0]
        else:
            if d:
                [x.__setitem__(1, l), (l := x), y.__setitem__(0, r), (r := y), l.__setitem__(3, L := l[3] - R - 1), r.__setitem__(3, R := r[3] - L - 1)]
            else:
                [x.__setitem__(0, r), (r := x), y.__setitem__(1, l), (l := y), r.__setitem__(3, R := r[3] - L - 1), l.__setitem__(3, L := l[3] - R - 1)]
        c -= 1
        update(y); update(x)
    if st:
        x = st[0]; d = dr[0]
        [(x.__setitem__(1, l), (l := x), l.__setitem__(3, L := l[3] - R - 1)) if d else (x.__setitem__(0, r), (r := x), r.__setitem__(3, R := r[3] - L - 1))]
        update(x)
    nd[0], nd[1] = l, r
    nd[3] = L + R + 1
    update(nd)
    return nd

def new_node(val):
    return [None, None, val, 1, val]

def merge(l, r):
    if not l or not r:
        return l or r
    if not l[1]:
        l[3] += r[3]
        l[1] = r
        return l
    st = list(takewhile(lambda node: node[1], iterate(lambda n: n[1], l)))
    x = st[-1] if st else l
    l = __splay(st, [1]*len(st), x)
    l[3] += r[3]
    l[1] = r
    update(l)
    return l

def split(t, k):
    if not t:
        return (None, None)
    if not 0 < k < t[3]:
        return (findk(t, k), None) if k == t[3] else (None, t)
    x, st, dr = t, [], []
    getc = lambda x: (x[0][3] if x[0] else 0) + 1
    while x:
        c = getc(x)
        if c == k: break
        st.append(x)
        if c < k:
            k -= c; x = x[1]; dr.append(1)
        else:
            x = x[0]; dr.append(0)
    l = __splay(st, dr, x)
    r = l[1]
    if r:
        l[3] -= r[3]
    l[1] = None
    update(l)
    return (l, r)

def findk(t, k):
    if not t or not 0 < k <= t[3]:
        return t
    x, st, dr = t, [], []
    while x:
        l = x[0]
        c = (l[3] if l else 0) + 1
        if c == k: break
        st.append(x)
        if c < k:
            k -= c; x = x[1]; dr.append(1)
        else:
            x = x[0]; dr.append(0)
    return __splay(st, dr, x)

def debug(root):
    def dfs(v, k):
        v[0] and dfs(v[0], k+1)
        print(' '*k, v[2:])
        v[1] and dfs(v[1], k+1)
    dfs(root, 0)

def iterate(f, x):
    while x:
        yield x
        x = f(x)

def takewhile(pred, iterable):
    for item in iterable:
        if pred(item):
            yield item
        else:
            break

readline = lambda: next(chain(islice(open(0), 0, None), repeat('')))
writelines = partial(open(1, 'w').writelines)

N, Q = map(int, readline().split())
root = prv = new_node(int(readline()))
prv[3] = N
for i in range(N-1):
    prv[1] = prv = new_node(int(readline()))
    prv[3] = N-1-i
ans = []

for q in range(Q):
    x, y, z = map(int, readline().split())
    if x == 0:
        b, c = split(root, z+1)
        v, b = b, b[0]
        a, b = split(b, y)
        d = merge(b, c)
        v[0], v[3] = a, (a[3] if a else 0) + 1
        update(v)
        root = merge(v, d)
    elif x == 1:
        b, c = split(root, z+1)
        a, b = split(b, y)
        ans.append('%d\n' % b[4])
        d = merge(b, c)
        root = merge(a, d)
    else:
        root = findk(root, y+1)
        root[2] = z
        update(root)
writelines(ans)