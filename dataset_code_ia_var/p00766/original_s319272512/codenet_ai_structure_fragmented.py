from collections import deque

def make_graph(n):
    return [[] for _ in range(n)]

def create_level_list(n):
    return [-1] * n

def add_edge_to_graph(g, fr, to, cap):
    g[fr].append([to, cap, len(g[to])])
    g[to].append([fr, 0, len(g[fr])-1])

def add_multi_edge_to_graph(g, v1, v2, cap1, cap2):
    g[v1].append([v2, cap1, len(g[v2])])
    g[v2].append([v1, cap2, len(g[v1])-1])

def bfs_level(g, n, s):
    level = create_level_list(n)
    deq = deque()
    level[s] = 0
    deq.append(s)
    while deq:
        v = deq.popleft()
        for e in g[v]:
            if e[1] > 0 and level[e[0]] < 0:
                level[e[0]] = level[v] + 1
                deq.append(e[0])
    return level

def min_value(a, b):
    return a if a < b else b

def dfs_find(g, level, it, v, t, f):
    if v == t:
        return f
    es = g[v]
    for i in range(it[v], len(g[v])):
        e = es[i]
        if e[1] > 0 and level[v] < level[e[0]]:
            d = dfs_find(g, level, it, e[0], t, min(f, e[1]))
            if d > 0:
                e[1] -= d
                g[e[0]][e[2]][1] += d
                it[v] = i
                return d
    it[v] = len(g[v])
    return 0

def max_flow_compute(g, n, s, t):
    flow = 0
    while True:
        level = bfs_level(g, n, s)
        if level[t] < 0:
            break
        it = [0] * n
        while True:
            f = dfs_find(g, level, it, s, t, 10**9+7)
            if f > 0:
                flow += f
            else:
                break
    return flow

def new_dinic(n):
    g = make_graph(n)
    return {'n': n, 'g': g}

def dinic_add_edge(dinic, fr, to, cap):
    add_edge_to_graph(dinic['g'], fr, to, cap)

def dinic_add_multi_edge(dinic, v1, v2, cap1, cap2):
    add_multi_edge_to_graph(dinic['g'], v1, v2, cap1, cap2)

def dinic_max_flow(dinic, s, t):
    return max_flow_compute(dinic['g'], dinic['n'], s, t)

def input_map():
    return map(int, raw_input().split())

def input_row():
    return raw_input()

def create_conn_mat(h, w):
    return [[0 for _ in range(w)] for _ in range(h)]

def process_rectangle(R, h, w):
    conn = create_conn_mat(h, w)
    P = []
    Q = []
    dep = 0
    for i in range(h-1):
        for j in range(w-1):
            first = R[i][j:j+2]
            second = R[i+1][j:j+2]

            if (first == '.#' and second == '##') or (first == '##' and second == '.#'):
                k = j
                while k+1 < w and R[i][k+1] != '.' and R[i+1][k+1] != '.':
                    k += 1
                if k+1 < w and ((R[i][k+1] == '#') ^ (R[i+1][k+1] == '#')):
                    P.append(((i, j), (i, k)))
                    conn[i][j] += 1
                    conn[i][k] += 1

            if first in ['.#', '#.'] and second == '##':
                k = i
                while k+1 < h and R[k+1][j] != '.' and R[k+1][j+1] != '.':
                    k += 1
                if k+1 < h and ((R[k+1][j] == '#') ^ (R[k+1][j+1] == '#')):
                    Q.append(((i, j), (k, j)))
                    conn[i][j] += 1
                    conn[k][j] += 1

            if first.count('#') + second.count('#') == 3:
                dep += 1
    return P, Q, dep, conn

def build_dinic_and_edges(lenP, lenQ, P, Q):
    dinic = new_dinic(2 + lenP + lenQ)
    connect_sources_to_P(dinic, lenP)
    connect_Q_to_sink(dinic, lenP, lenQ)
    connect_P_to_Q_with_constraints(dinic, P, Q, lenP)
    return dinic

def connect_sources_to_P(dinic, lenP):
    for i in range(lenP):
        dinic_add_edge(dinic, 0, i+2, 1)

def connect_Q_to_sink(dinic, lenP, lenQ):
    for i in range(lenQ):
        dinic_add_edge(dinic, lenP+i+2, 1, 1)

def connect_P_to_Q_with_constraints(dinic, P, Q, lenP):
    for i, p in enumerate(P):
        (a, b), (a2, s) = p
        for j, q in enumerate(Q):
            (c, d), (t, d2) = q
            if c <= a <= t and b <= d <= s:
                dinic_add_edge(dinic, i+2, lenP + j+2, 1)

def calculate_final_answer(dep, P, Q, dinic):
    result = dep - (len(P) + len(Q) - dinic_max_flow(dinic, 0, 1)) + 1
    return result

def process_case(h, w, R):
    P, Q, dep, conn = process_rectangle(R, h, w)
    dinic = build_dinic_and_edges(len(P), len(Q), P, Q)
    answer = calculate_final_answer(dep, P, Q, dinic)
    return answer

def read_and_process():
    while True:
        h, w = input_map()
        if h == 0 and w == 0:
            break
        R = [input_row() for _ in range(h)]
        result = process_case(h, w, R)
        print result

read_and_process()