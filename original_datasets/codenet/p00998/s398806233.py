INF = 10**9
def update(nd):
    if nd:
        l = nd[0]; r = nd[1]
        nd[4] = min((l[4] if l else INF), (r[4] if r else INF), nd[2])

# splay a node nd
def __splay(st, dr, nd):
    l = nd[0]; r = nd[1]
    L = (l[3] if l else 0); R = (r[3] if r else 0)
    c = len(st) >> 1
    while c:
        # y(d1)-x(d)-nd
        x = st.pop(); y = st.pop()
        d = dr.pop(); d1 = dr.pop()

        if d == d1:
            # Zig-zig step
            y[3] = e = y[3] - L - R - 2
            if d:
                y[1] = x[0]; x[0] = y
                x[1] = l; l = x

                l[3] = L = e + L + 1
            else:
                y[0] = x[1]; x[1] = y
                x[0] = r; r = x

                r[3] = R = e + R + 1
        else:
            # Zig-zag step
            if d:
                x[1] = l; l = x
                y[0] = r; r = y

                l[3] = L = l[3] - R - 1
                r[3] = R = r[3] - L - 1
            else:
                x[0] = r; r = x
                y[1] = l; l = y

                r[3] = R = r[3] - L - 1
                l[3] = L = l[3] - R - 1
        c -= 1
        update(y); update(x)
    if st:
        # Zig step
        x = st[0]; d = dr[0]
        if d:
            x[1] = l; l = x
            l[3] = L = l[3] - R - 1
        else:
            x[0] = r; r = x
            r[3] = R = r[3] - L - 1
        update(x)
    nd[0] = l; nd[1] = r
    nd[3] = L + R + 1
    update(nd)
    return nd

def new_node(val):
    return [None, None, val, 1, val]

# merge a tree l with a tree r
def merge(l, r):
    if not l or not r:
        return l or r
    if not l[1]:
        l[3] += r[3]
        l[1] = r
        return l

    st = []
    x = l
    while x[1]:
        st.append(x)
        x = x[1]

    l = __splay(st, [1]*len(st), x)
    l[3] += r[3]
    l[1] = r
    update(l)
    return l

# split a tree t into two trees of size k and |t|-k
def split(t, k):
    if not t:
        return None, None
    if not 0 < k < t[3]:
        if k == t[3]:
            return findk(t, k), None
        return None, t
    x = t
    st = []; dr = []
    while x:
        l = x[0]
        c = (l[3] if l else 0) + 1

        if c == k:
            break

        st.append(x)
        if c < k:
            k -= c
            x = x[1]
            dr.append(1)
        else:
            x = x[0]
            dr.append(0)
    l = __splay(st, dr, x)
    r = l[1]
    if r:
        l[3] -= r[3]
    l[1] = None
    update(l)
    return l, r

# find the k-th element
def findk(t, k):
    if not t or not 0 < k <= t[3]:
        return t
    x = t
    st = []; dr = []
    while x:
        l = x[0]
        c = (l[3] if l else 0) + 1

        if c == k:
            break

        st.append(x)
        if c < k:
            k -= c
            x = x[1]
            dr.append(1)
        else:
            x = x[0]
            dr.append(0)
    return __splay(st, dr, x)

def debug(root):
    def dfs(v, k):
        if v[0]:
            dfs(v[0], k+1)
        print(" "*k, v[2:])
        if v[1]:
            dfs(v[1], k+1)
    dfs(root, 0)

readline = open(0).readline
writelines = open(1, 'w').writelines

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
        v = b; b = b[0]
        a, b = split(b, y)
        d = merge(b, c)
        v[0] = a; v[3] = (a[3] if a else 0) + 1
        update(v)
        root = merge(v, d)
    elif x == 1:
        b, c = split(root, z+1)
        a, b = split(b, y)
        ans.append("%d\n" % b[4])
        d = merge(b, c)
        root = merge(a, d)
    else:
        root = findk(root, y+1)
        root[2] = z
        update(root)
writelines(ans)