from collections import deque

def create_graph(n):
    return [[] for _ in xrange(n)]

def edge_list(to, cap, rev):
    return [to, cap, rev]

def add_single_edge(g, fr, to, cap):
    g[fr].append(edge_list(to, cap, len(g[to])))
    g[to].append(edge_list(fr, 0, len(g[fr]) - 1))

def add_bidirectional_edge(g, v1, v2, cap1, cap2):
    g[v1].append(edge_list(v2, cap1, len(g[v2])))
    g[v2].append(edge_list(v1, cap2, len(g[v1]) - 1))

def bfs_level(n, g, s):
    level = [-1] * n
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

def dfs_flow_rec(g, level, it, v, t, f):
    if v == t:
        return f
    es = g[v]
    for i in xrange(it[v], len(g[v])):
        e = es[i]
        if e[1] > 0 and level[v] < level[e[0]]:
            d = dfs_flow_rec(g, level, it, e[0], t, min(f, e[1]))
            if d > 0:
                e[1] -= d
                g[e[0]][e[2]][1] += d
                it[v] = i
                return d
    it[v] = len(g[v])
    return 0

class Dinic:
    def __init__(self, n):
        self.n = n
        self.g = create_graph(n)
        self.level = None
        self.it = None

    def add_edge(self, fr, to, cap):
        add_single_edge(self.g, fr, to, cap)

    def add_multi_edge(self, v1, v2, cap1, cap2):
        add_bidirectional_edge(self.g, v1, v2, cap1, cap2)

    def bfs(self, s):
        self.level = bfs_level(self.n, self.g, s)

    def dfs(self, v, t, f):
        return dfs_flow_rec(self.g, self.level, self.it, v, t, f)

    def max_flow(self, s, t):
        flow = 0
        INF = 10**9 + 7
        while True:
            self.bfs(s)
            if self.level[t] < 0:
                break
            self.it = [0] * self.n
            while True:
                f = self.dfs(s, t, INF)
                if f > 0:
                    flow += f
                else:
                    break
        return flow

def parse_input():
    h, w = map(int, raw_input().split())
    return h, w

def parse_grid(h):
    return [raw_input() for _ in xrange(h)]

def check_first_case(first, second):
    return (first == '.#' and second == '##') or (first == '##' and second == '.#')

def find_horizontal_extent(R, i, k, w):
    while k + 1 < w and R[i][k + 1] != '.' and R[i + 1][k + 1] != '.':
        k += 1
    return k

def last_horizontal_check(R, i, k, w):
    if k + 1 < w and ((R[i][k + 1] == '#') ^ (R[i + 1][k + 1] == '#')):
        return True
    return False

def first_case_handle(P, i, j, R, w):
    first = R[i][j:j+2]
    second = R[i+1][j:j+2]
    if check_first_case(first, second):
        k = j
        k = find_horizontal_extent(R, i, k, w)
        if last_horizontal_check(R, i, k, w):
            P.append(((i, j), (i, k)))

def check_second_case(first, second):
    return first in ['.#', '#.'] and second == '##'

def find_vertical_extent(R, j, k, h):
    while k + 1 < h and R[k + 1][j] != '.' and R[k + 1][j + 1] != '.':
        k += 1
    return k

def last_vertical_check(R, k, j, h):
    if k + 1 < h and ((R[k + 1][j] == '#') ^ (R[k + 1][j + 1] == '#')):
        return True
    return False

def second_case_handle(Q, i, j, R, h):
    first = R[i][j:j+2]
    second = R[i+1][j:j+2]
    if check_second_case(first, second):
        k = i
        k = find_vertical_extent(R, j, k, h)
        if last_vertical_check(R, k, j, h):
            Q.append(((i, j), (k, j)))

def third_case_count(first, second):
    return first.count('#') + second.count('#') == 3

def process_grid(h, w, R):
    P = []
    Q = []
    dep = [0]

    def do_cases(i, j):
        first_case_handle(P, i, j, R, w)
        second_case_handle(Q, i, j, R, h)
        first = R[i][j:j+2]
        second = R[i+1][j:j+2]
        if third_case_count(first, second):
            dep[0] += 1

    for i in xrange(h-1):
        for j in xrange(w-1):
            do_cases(i, j)
    return P, Q, dep[0]

def create_dinic(lenP, lenQ):
    return Dinic(2 + lenP + lenQ)

def connect_source_to_P(dinic, lenP):
    for i in xrange(lenP):
        dinic.add_edge(0, i + 2, 1)

def connect_Q_to_sink(dinic, lenP, lenQ):
    for i in xrange(lenQ):
        dinic.add_edge(lenP + i + 2, 1, 1)

def is_intersect_segment(a, b, s, c, d, t):
    if c <= a <= t and b <= d <= s:
        return True
    return False

def connect_P_to_Q(dinic, P, Q, lenP):
    for i, p in enumerate(P):
        (a, b), (a2, s) = p
        for j, q in enumerate(Q):
            (c, d), (t, d2) = q
            if is_intersect_segment(a, b, s, c, d, t):
                dinic.add_edge(i + 2, lenP + j + 2, 1)

def solve_single_case(h, w, R):
    P, Q, dep = process_grid(h, w, R)
    dinic = create_dinic(len(P), len(Q))
    connect_source_to_P(dinic, len(P))
    connect_Q_to_sink(dinic, len(P), len(Q))
    connect_P_to_Q(dinic, P, Q, len(P))
    flow = dinic.max_flow(0, 1)
    res = dep - (len(P) + len(Q) - flow) + 1
    return res

def main():
    while True:
        h, w = parse_input()
        if h == 0 and w == 0:
            break
        R = parse_grid(h)
        result = solve_single_case(h, w, R)
        print result

main()