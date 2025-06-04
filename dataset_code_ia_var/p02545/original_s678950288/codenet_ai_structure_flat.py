import sys
readline = sys.stdin.buffer.readline

n = int(readline())
N = n * 3
a = list(map(int, readline().split()))
b = list(map(int, readline().split()))

for i in range(N):
    a[i] -= 1
    b[i] -= 1

apos = [[] for _ in range(n)]
for i in range(N):
    apos[a[i]].append(i)

bpos = [[] for _ in range(n)]
for i in range(N):
    bpos[b[i]].append(i)

ans = 10 ** 18

for l in range(N):
    for r in range(l, N + 1):
        t = [False] * N
        head = l
        subseq_ok = True
        for i in range(N):
            if t[i]:
                head_ = head
                while head_ < r and a[i] != b[head_]:
                    head_ += 1
                if head_ == r:
                    subseq_ok = False
                    break
                head_ += 1
                head = head_
        if not subseq_ok:
            continue
        l2r = []
        r2l = []
        w = []
        invalid = False
        for val in range(n):
            z = []
            for x in bpos[val]:
                if x < l:
                    z.append(0)
                elif x < r:
                    z.append(1)
                else:
                    z.append(2)
            if z == [0,0,0]:
                invalid = True
                break
            elif z == [0,0,1]:
                t[apos[val][2]] = 1
            elif z == [0,0,2]:
                x = l - bpos[val][0]
                y = bpos[val][2] - r
                r2l.append((x, y))
            elif z == [0,1,1]:
                t[apos[val][0]] = 1
                t[apos[val][2]] = 1
            elif z == [0,1,2]:
                x = l - bpos[val][0]
                y = bpos[val][2] - r
                w.append((apos[val][0], apos[val][2], x, y))
            elif z == [0,2,2]:
                x = l - bpos[val][0]
                y = bpos[val][2] - r
                l2r.append((x, y))
            elif z == [1,1,1]:
                t[apos[val][0]] = 1
                t[apos[val][1]] = 1
                t[apos[val][2]] = 1
            elif z == [1,1,2]:
                t[apos[val][0]] = 1
                t[apos[val][2]] = 1
            elif z == [1,2,2]:
                t[apos[val][0]] = 1
            elif z == [2,2,2]:
                invalid = True
                break
            else:
                invalid = True
                break
        if invalid:
            continue
        head = l
        subseq_ok = True
        for i in range(N):
            if t[i]:
                head_ = head
                while head_ < r and a[i] != b[head_]:
                    head_ += 1
                if head_ == r:
                    subseq_ok = False
                    break
                head_ += 1
                head = head_
        if not subseq_ok:
            continue
        conflict_arr = []
        for xa, xb in l2r:
            for ya, yb in r2l:
                if ya <= xa and xb <= yb:
                    invalid = True
                    break
            if invalid:
                break
        if invalid:
            continue
        s = len(w)
        g_n = 2 * s
        g_head = [None] * g_n
        class E:
            def __init__(self, to, nx):
                self.to = to
                self.nx = nx
        def g_ae(a, b):
            g_head[a] = E(b, g_head[a])
            return g_head[a]
        def add(x, y):
            g_ae(x ^ 1, y)
            g_ae(y ^ 1, x)
        for i in range(s):
            pa, pb, qa, qb = w[i]
            ok = True
            t[pa] = 1
            head = l
            for x in range(N):
                if t[x]:
                    head_ = head
                    while head_ < r and a[x] != b[head_]:
                        head_ += 1
                    if head_ == r:
                        ok = False
                        break
                    head_ += 1
                    head = head_
            t[pa] = 0
            if ok:
                ok2 = True
                for xa, xb in l2r:
                    if qa <= xa and xb <= qb:
                        ok2 = False
                        break
                ok = ok2
            if not ok:
                add(i * 2 + 1, i * 2 + 1)
            ok = True
            t[pb] = 1
            head = l
            for x in range(N):
                if t[x]:
                    head_ = head
                    while head_ < r and a[x] != b[head_]:
                        head_ += 1
                    if head_ == r:
                        ok = False
                        break
                    head_ += 1
                    head = head_
            t[pb] = 0
            if ok:
                ok2 = True
                for ya, yb in r2l:
                    if qa <= ya and yb <= qb:
                        ok2 = False
                        break
                ok = ok2
            if not ok:
                add(i * 2, i * 2)
        for i in range(s):
            for j in range(i+1, s):
                p0a, p0b, q0a, q0b = w[i]
                p1a, p1b, q1a, q1b = w[j]
                t0 = bpos[a[p0a]][1]
                t1 = bpos[a[p1a]][1]
                ok = True
                if (p0a < p1a) != (t0 < t1):
                    ok = False
                if not ok:
                    add(i * 2 + 1, j * 2 + 1)
                ok = True
                if (p0a < p1b) != (t0 < t1):
                    ok = False
                if q1a <= q0a and q0b <= q1b:
                    ok = False
                if not ok:
                    add(i * 2 + 1, j * 2)
                ok = True
                if (p0b < p1a) != (t0 < t1):
                    ok = False
                if q0a <= q1a and q1b <= q0b:
                    ok = False
                if not ok:
                    add(i * 2, j * 2 + 1)
                ok = True
                if (p0b < p1b) != (t0 < t1):
                    ok = False
                if not ok:
                    add(i * 2, j * 2)
        n1 = g_n
        cur = g_head[:]
        last = [None] * n1
        order = [-1] * n1
        low = [-1] * n1
        bl = [-1] * n1
        idx_ = []
        st = []
        num = 0
        for i_ in range(n1):
            if order[i_] != -1:
                continue
            rec = [i_]
            while rec:
                v = rec[-1]
                if last[v] is None:
                    order[v] = low[v] = num
                    num += 1
                    st.append(v)
                else:
                    low[v] = min(low[v], low[last[v].to])
                found = False
                while cur[v] is not None:
                    e = cur[v]
                    cur[v] = e.nx
                    to = e.to
                    if order[to] == -1:
                        rec.append(to)
                        last[v] = e
                        found = True
                        break
                    elif bl[to] == -1:
                        low[v] = min(low[v], order[to])
                if not found:
                    rec.pop()
                    if order[v] == low[v]:
                        c = len(idx_)
                        tmp = []
                        while True:
                            a_ = st.pop()
                            bl[a_] = c
                            tmp.append(a_)
                            if v == a_:
                                break
                        idx_.append(tmp)
        scc_s = len(idx_)
        for i_ in range(n1):
            bl[i_] = scc_s - 1 - bl[i_]
        idx_.reverse()
        sat_ok = True
        for i_ in range(s):
            if bl[i_*2] == bl[i_*2+1]:
                sat_ok = False
                break
        if not sat_ok:
            continue
        ans = min(ans, N-(r-l))

if ans == 10**18:
    ans = -1

print(ans)