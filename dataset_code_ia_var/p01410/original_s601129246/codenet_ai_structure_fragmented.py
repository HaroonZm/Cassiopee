import sys
from heapq import heappush, heappop

readline = sys.stdin.readline
write = sys.stdout.write

def make_graph(N):
    return [[] for _ in range(N)]

def make_forward_edge(to, cap, cost):
    return [to, cap, cost, None]

def make_backward_edge(fr, fwd_edge, cost):
    return [fr, 0, -cost, fwd_edge]

def link_edges(forward, backward):
    forward[3] = backward

def add_to_graph(G, u, edge):
    G[u].append(edge)

def add_edge(mcf, fr, to, cap, cost):
    forward = make_forward_edge(to, cap, cost)
    backward = make_backward_edge(fr, forward, cost)
    link_edges(forward, backward)
    add_to_graph(mcf.G, fr, forward)
    add_to_graph(mcf.G, to, backward)

def initialize_list(val, n):
    return [val] * n

def copy_list(dst, src):
    dst[:] = src

def push_queue(que, val):
    heappush(que, val)

def pop_queue(que):
    return heappop(que)

def continue_if(cond):
    if cond:
        return True
    return False

def update_dist_if_shorter(G, H, v, dist, prv_v, prv_e, que):
    for e in G[v]:
        w, cap, cost, _ = e
        r0 = dist[v] + H[v]
        if cap > 0 and r0 + cost - H[w] < dist[w]:
            dist[w] = r = r0 + cost - H[w]
            prv_v[w] = v; prv_e[w] = e
            push_queue(que, (r, w))

def update_potential(H, dist, N):
    for i in range(N):
        H[i] += dist[i]

def update_flow_path(f, s, t, prv_v, prv_e):
    d = f
    v = t
    while v != s:
        d = min(d, prv_e[v][1])
        v = prv_v[v]
    return d

def update_edges_and_flow(prv_v, prv_e, s, t, d):
    v = t
    while v != s:
        e = prv_e[v]
        e[1] -= d
        e[3][1] += d
        v = prv_v[v]

class MinCostFlow:
    INF = 10**18

    def __init__(self, N):
        self.N = N
        self.G = make_graph(N)

    def add_edge(self, fr, to, cap, cost):
        add_edge(self, fr, to, cap, cost)

    def flow(self, s, t, f):
        N = self.N; G = self.G; INF = MinCostFlow.INF
        res = 0
        H = initialize_list(0, N)
        prv_v = initialize_list(0, N)
        prv_e = initialize_list(None, N)
        d0 = initialize_list(INF, N)
        dist = initialize_list(INF, N)
        while f:
            copy_list(dist, d0)
            dist[s] = 0
            que = [(0, s)]
            while que:
                c, v = pop_queue(que)
                if continue_if(dist[v] < c):
                    continue
                update_dist_if_shorter(G, H, v, dist, prv_v, prv_e, que)
            if dist[t] == INF:
                return None
            update_potential(H, dist, N)
            d = update_flow_path(f, s, t, prv_v, prv_e)
            f -= d
            res += d * H[t]
            update_edges_and_flow(prv_v, prv_e, s, t, d)
        return res

def read_integer():
    return int(readline())

def read_integer_list():
    return list(map(int, readline().split()))

def collect_pairs(N):
    return [read_integer_list() for _ in range(N)]

def collect_unique_elements(P):
    s = set()
    for a, b in P:
        s.add(a)
        s.add(b)
    return s

def sort_set_elements(s):
    return sorted(s)

def enumerate_elements(S):
    return {e: i for i, e in enumerate(S)}

def initialize_mcf(N, M):
    return MinCostFlow(N + M + 2)

def add_terminal_edges(mcf, N, M):
    for i in range(M):
        mcf.add_edge(N+i, N+M+1, 1, 0)

def add_node_edges(mcf, N, M, P, mp):
    for i, (a, b) in enumerate(P):
        mcf.add_edge(N+M, i, 1, 0)
        mcf.add_edge(i, N+M+1, 1, 0)
        mcf.add_edge(i, N+mp[a], 1, -b)
        mcf.add_edge(i, N+mp[b], 1, -a)

def compute_and_output(mcf, N, M):
    res = mcf.flow(N+M, N+M+1, N)
    write("%d\n" % -res)

def solve():
    N = read_integer()
    P = collect_pairs(N)
    s = collect_unique_elements(P)
    S = sort_set_elements(s)
    M = len(S)
    mp = enumerate_elements(S)
    mcf = initialize_mcf(N, M)
    add_terminal_edges(mcf, N, M)
    add_node_edges(mcf, N, M, P, mp)
    compute_and_output(mcf, N, M)

solve()