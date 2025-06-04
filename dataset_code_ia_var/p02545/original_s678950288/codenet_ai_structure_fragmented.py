import sys

def get_readline():
    return sys.stdin.buffer.readline

def parse_int():
    return int(get_readline()())

def parse_int_list():
    return list(map(int, get_readline().split()))

class E:
    def __init__(self, to, nx):
        self.to = to
        self.nx = nx

class Graph:
    def __init__(self, n):
        self.n = n
        self.head = [None] * n

    def ae(self, a, b):
        self.head[a] = E(b, self.head[a])
        return self.head[a]

def init_last(n):
    return [None] * n

def init_order(n):
    return [-1] * n

def init_low(n):
    return [-1] * n

def init_bl(n):
    return [-1] * n

def scc_visit_init(n, g):
    cur = g.head
    last = init_last(n)
    order = init_order(n)
    low = init_low(n)
    bl = init_bl(n)
    idx = []
    st = []
    num = 0
    return cur, last, order, low, bl, idx, st, num

def scc_assign_bl(n, idx, bl):
    s = len(idx)
    for i in range(n):
        bl[i] = s - 1 - bl[i]
    idx.reverse()
    return s, bl, idx

def process_edge(v, cur, order, bl, low, rec, last, st, num, idx):
    if last[v] is None:
        order[v] = low[v] = num
        num += 1
        st.append(v)
    else:
        low[v] = min(low[v], low[last[v].to])
    return num

def process_next_edge(v, cur, order, bl, low, rec, last):
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
    return found

def process_finish(v, st, order, low, bl, idx, rec):
    rec.pop()
    if order[v] == low[v]:
        c = len(idx)
        tmp = []
        while True:
            a = st.pop()
            bl[a] = c
            tmp.append(a)
            if v == a:
                break
        idx.append(tmp)

def scc(g):
    n = g.n
    cur, last, order, low, bl, idx, st, num = scc_visit_init(n, g)
    for i in range(n):
        if order[i] != -1:
            continue
        rec = [i]
        while rec:
            v = rec[-1]
            num = process_edge(v, cur, order, bl, low, rec, last, st, num, idx)
            found = process_next_edge(v, cur, order, bl, low, rec, last)
            if not found:
                process_finish(v, st, order, low, bl, idx, rec)
    s, bl, idx = scc_assign_bl(n, idx, bl)
    return s, bl, idx

class twosat:
    def __init__(self, n):
        self.n = n
        self.g = Graph(2 * n)

    def add(self, x, y):
        self.g.ae(x ^ 1, y)
        self.g.ae(y ^ 1, x)

    def solve(self):
        s, bl, idx = scc(self.g)
        for i in range(self.n):
            if bl[i * 2] == bl[i * 2 + 1]:
                return False
        return True

def decrease_by_one(arr):
    for i in range(len(arr)):
        arr[i] -= 1

def build_pos(n, src):
    pos = [[] for _ in range(n)]
    for i, val in enumerate(src):
        pos[val].append(i)
    return pos

def is_issubseq(t, N, l, r, a, b):
    head = l
    for i in range(N):
        if t[i]:
            while head < r and a[i] != b[head]:
                head += 1
            if head == r:
                return False
            head += 1
    return True

def feasible_construct_z(val, bpos, l, r):
    z = []
    for x in bpos[val]:
        if x < l:
            z.append(0)
        elif x < r:
            z.append(1)
        else:
            z.append(2)
    return z

def feasible_process_z(n, N, l, r, a, b, apos, bpos, t, l2r, r2l, w):
    for val in range(n):
        z = feasible_construct_z(val, bpos, l, r)
        if z == [0,0,0]:
            return False
        elif z == [0,0,1]:
            t[apos[val][2]] = 1
        elif z == [0,0,2]:
            x = l - bpos[val][0]
            y = bpos[val][2] - r
            r2l.append((x,y))
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
            return False
        else:
            assert False
    return True

def conflict(xa, xb, ya, yb):
    return ya <= xa and xb <= yb

def feasible_check_conflicts(l2r, r2l):
    for xa, xb in l2r:
        for ya, yb in r2l:
            if conflict(xa, xb, ya, yb):
                return False
    return True

def feasible_handle_w(t, N, a, b, bpos, l2r, r2l, w):
    s = len(w)
    ts = twosat(s)
    for i in range(s):
        pa, pb, qa, qb = w[i]

        # left is ok?
        ok_l = True
        t[pa] = 1
        if not is_issubseq(t, N, 0, N, a, b):
            ok_l = False
        t[pa] = 0
        if ok_l:
            for xa, xb in l2r:
                if conflict(xa, xb, qa, qb):
                    ok_l = False
        if not ok_l:
            ts.add(i * 2 + 1, i * 2 + 1)

        # right is ok?
        ok_r = True
        t[pb] = 1
        if not is_issubseq(t, N, 0, N, a, b):
            ok_r = False
        t[pb] = 0
        if ok_r:
            for ya, yb in r2l:
                if conflict(qa, qb, ya, yb):
                    ok_r = False
        if not ok_r:
            ts.add(i * 2, i * 2)

    for i in range(s):
        for j in range(i + 1, s):
            p0a, p0b, q0a, q0b = w[i]
            p1a, p1b, q1a, q1b = w[j]
            t0 = bpos[a[p0a]][1]
            t1 = bpos[a[p1a]][1]

            # left-left
            ok = True
            if (p0a < p1a) != (t0 < t1):
                ok = False
            if not ok:
                ts.add(i*2+1, j*2+1)
            # left-right
            ok = True
            if (p0a < p1b) != (t0 < t1):
                ok = False
            if conflict(q1a, q1b, q0a, q0b):
                ok = False
            if not ok:
                ts.add(i*2+1, j*2)
            # right-left
            ok = True
            if (p0b < p1a) != (t0 < t1):
                ok = False
            if conflict(q0a, q0b, q1a, q1b):
                ok = False
            if not ok:
                ts.add(i*2, j*2+1)
            # right-right
            ok = True
            if (p0b < p1b) != (t0 < t1):
                ok = False
            if not ok:
                ts.add(i*2, j*2)
    return ts.solve()

def feasible(l, r):
    t = [False] * N
    l2r = []
    r2l = []
    w = []
    if not feasible_process_z(n, N, l, r, a, b, apos, bpos, t, l2r, r2l, w):
        return False
    if not is_issubseq(t, N, l, r, a, b):
        return False
    if not feasible_check_conflicts(l2r, r2l):
        return False
    return feasible_handle_w(t, N, a, b, bpos, l2r, r2l, w)

def main():
    global n, N, a, b, apos, bpos
    readline = get_readline()
    n = int(readline())
    N = n * 3
    a = list(map(int, readline().split()))
    b = list(map(int, readline().split()))
    decrease_by_one(a)
    decrease_by_one(b)
    apos = build_pos(n, a)
    bpos = build_pos(n, b)

    ans = 10 ** 18
    def update_ans(ans, i, j):
        if feasible(i, j):
            return min(ans, N - (j - i))
        return ans

    for i in range(N):
        for j in range(i, N + 1):
            ans = update_ans(ans, i, j)

    if ans == 10 ** 18:
        ans = -1

    print(ans)

if __name__ == "__main__":
    main()