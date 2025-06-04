from collections import deque

def create_graph(n):
    return [[] for _ in range(n)]

def create_dinic(n):
    dinic = {}
    dinic['n'] = n
    dinic['g'] = create_graph(n)
    dinic['level'] = None
    dinic['it'] = None
    return dinic

def add_edge(g, fr, to, cap):
    g[fr].append([to, cap, len(g[to])])
    g[to].append([fr, 0, len(g[fr])-1])

def add_multi_edge(g, v1, v2, cap1, cap2):
    g[v1].append([v2, cap1, len(g[v2])])
    g[v2].append([v1, cap2, len(g[v1])-1])

def bfs_set_level(g, n, s):
    level = [-1]*n
    deq = deque()
    level[s] = 0
    deq.append(s)
    while deq:
        v = deq.popleft()
        for e in g[v]:
            if e[1]>0 and level[e[0]]<0:
                level[e[0]] = level[v] + 1
                deq.append(e[0])
    return level

def dfs_impl(g, level, it, v, t, f):
    if v==t: return f
    es = g[v]
    for i in xrange(it[v], len(es)):
        e = es[i]
        if e[1]>0 and level[v]<level[e[0]]:
            d = dfs_impl(g, level, it, e[0], t, min(f, e[1]))
            if d>0:
                e[1] -= d
                g[e[0]][e[2]][1] += d
                it[v] = i
                return d
    it[v] = len(es)
    return 0

def dinic_max_flow(dinic, s, t):
    flow = 0
    while True:
        dinic['level'] = bfs_set_level(dinic['g'], dinic['n'], s)
        if dinic['level'][t]<0: break
        dinic['it'] = [0]*dinic['n']
        while True:
            f = dfs_impl(dinic['g'], dinic['level'], dinic['it'], s, t, 10**9+7)
            if f>0:
                flow += f
            else:
                break
    return flow

def read_input():
    return map(int, raw_input().split())

def read_rows(h):
    return [raw_input() for _ in xrange(h)]

def make_conn(h, w):
    return [[0 for i in xrange(w)] for j in xrange(h)]

def add_P(P, conn, i, j, k):
    P.append(((i, j), (i, k)))
    conn[i][j] += 1
    conn[i][k] += 1

def add_Q(Q, conn, i, j, k):
    Q.append(((i, j), (k, j)))
    conn[i][j] += 1
    conn[k][j] += 1

def check_P_case(R, i, j, h, w, P, conn):
    first = R[i][j:j+2]; second = R[i+1][j:j+2]
    if (first == '.#' and second == '##') or (first == '##' and second == '.#'):
        k = j
        while k+1 < w and R[i][k+1] != '.' and R[i+1][k+1] != '.':
            k += 1
        if k+1 < w and ((R[i][k+1] == '#') ^ (R[i+1][k+1] == '#')):
            add_P(P, conn, i, j, k)
    return

def check_Q_case(R, i, j, h, w, Q, conn):
    first = R[i][j:j+2]; second = R[i+1][j:j+2]
    if first in ['.#', '#.'] and second == '##':
        k = i
        while k+1 < h and R[k+1][j] != '.' and R[k+1][j+1] != '.':
            k += 1
        if k+1 < h and ((R[k+1][j] == '#') ^ (R[k+1][j+1] == '#')):
            add_Q(Q, conn, i, j, k)
    return

def count_dep(R, i, j):
    first = R[i][j:j+2]; second = R[i+1][j:j+2]
    if first.count('#') + second.count('#') == 3:
        return 1
    return 0

def preprocess_blocks(R, h, w):
    conn = make_conn(h, w)
    P = []
    Q = []
    dep = 0
    for i in xrange(h-1):
        for j in xrange(w-1):
            check_P_case(R, i, j, h, w, P, conn)
            check_Q_case(R, i, j, h, w, Q, conn)
            dep += count_dep(R, i, j)
    return P, Q, dep, conn

def create_bipartite_dinic(P, Q):
    dinic = create_dinic(2 + len(P) + len(Q))
    for i in xrange(len(P)):
        add_edge(dinic['g'], 0, i+2, 1)
    for i in xrange(len(Q)):
        add_edge(dinic['g'], len(P)+i+2, 1, 1)
    return dinic

def seg_intersect(p, q):
    (a, b), (a_, s) = p
    (c, d), (t, d_) = q
    if c <= a <= t and b <= d <= s:
        return True
    return False

def connect_PQ_edges(dinic, P, Q):
    for i, p in enumerate(P):
        for j, q in enumerate(Q):
            if seg_intersect(p, q):
                add_edge(dinic['g'], i+2, len(P) + j+2, 1)

def solve_case(h, w):
    R = read_rows(h)
    P, Q, dep, conn = preprocess_blocks(R, h, w)
    dinic = create_bipartite_dinic(P, Q)
    connect_PQ_edges(dinic, P, Q)
    mf = dinic_max_flow(dinic, 0, 1)
    ans = dep - (len(P) + len(Q) - mf) + 1
    print ans

def mainloop():
    while True:
        h, w = read_input()
        if h==0 and w==0:
            break
        solve_case(h, w)

mainloop()