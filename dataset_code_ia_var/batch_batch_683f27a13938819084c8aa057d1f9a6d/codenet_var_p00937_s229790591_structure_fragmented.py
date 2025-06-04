from collections import deque
import sys

def read_input():
    return sys.stdin.readline

def write_output(s):
    sys.stdout.write(s)

def parse_first_line(line):
    data = list(map(int, line.split()))
    N, M = data[0], data[1]
    V = data[2:]
    return N, M, V

def init_graph(N):
    return [[] for _ in range(N)]

def add_edges(G, M, readline):
    for _ in range(M):
        u, v = map(int, readline().split())
        add_single_edge(G, u, v)

def add_single_edge(G, u, v):
    G[u-1].append(v-1)

def init_adj_matrix(N, G):
    ES = [[0]*N for _ in range(N)]
    for v in range(N):
        mark_edges_for_vertex(ES, v, G)
    return ES

def mark_edges_for_vertex(ES, v, G):
    for w in G[v]:
        ES[v][w] = 1

def matmul(A, B, N):
    C = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            C[i][j] = calc_cell(A, B, N, i, j)
    return C

def calc_cell(A, B, N, i, j):
    return +(sum(A[i][k] & B[k][j] for k in range(N)) > 0)

def identity_matrix(N):
    R = [[0]*N for _ in range(N)]
    for i in range(N):
        R[i][i] = 1
    return R

def fast_pow(X, k, N):
    R = identity_matrix(N)
    while k:
        if k & 1:
            R = matmul(R, X, N)
        X = matmul(X, X, N)
        k >>= 1
    return R

def process_V(V):
    V_sorted = list(V)
    V_sorted.sort()
    return V_sorted

def prepare_EE_ds_rgs(V, ES, N):
    EE = []
    ds = []
    rgs = []
    for k in V:
        ek, d, rg = process_single_k(ES, k, N)
        EE.append(ek)
        ds.append(d)
        rgs.append(rg)
    return EE, ds, rgs

def process_single_k(ES, k, N):
    ek = fast_pow(ES, k, N)
    d = [0]*N
    rg = [[] for _ in range(N)]
    fill_d_rg(N, ek, d, rg)
    return ek, d, rg

def fill_d_rg(N, ek, d, rg):
    for v in range(N):
        fill_single_v(N, ek, d, rg, v)

def fill_single_v(N, ek, d, rg, v):
    ts = ek[v]
    for w in range(N):
        if ts[w]:
            d[v] += 1
            rg[w].append(v)

def prepare_D(ds, N):
    D = [0]*N
    for i in range(3):
        apply_d_to_D(ds, D, i, N)
    return D

def apply_d_to_D(ds, D, i, N):
    d = ds[i]
    for v in range(N):
        if d[v]:
            D[v] += 1

def init_U(N):
    U = [-1]*N
    U[N-1] = 0
    return U

def create_initial_queue(N):
    return deque([N-1])

def process_propagation(U, rgs, ds, D):
    que = create_initial_queue(len(U))
    while que:
        v = que.popleft()
        process_vertex(v, U, rgs, ds, D, que)

def process_vertex(v, U, rgs, ds, D, que):
    u = U[v]
    num_rgs = len(rgs)
    for i in range(num_rgs):
        rg = rgs[i]
        d = ds[i]
        for w in rg[v]:
            if d[w] == 0:
                continue
            d[w] = 0
            D[w] -= 1
            if D[w] == 0:
                if U[w] == -1:
                    U[w] = u+1
                    que.append(w)

def output_result(U, write):
    if U[0] != -1:
        write("%d\n" % U[0])
    else:
        write("IMPOSSIBLE\n")

def solve():
    readline = read_input()
    write = write_output
    N, M, V = parse_first_line(readline())
    G = init_graph(N)
    add_edges(G, M, readline)
    V_sorted = process_V(V)
    ES = init_adj_matrix(N, G)
    EE, ds, rgs = prepare_EE_ds_rgs(V_sorted, ES, N)
    D = prepare_D(ds, N)
    U = init_U(N)
    process_propagation(U, rgs, ds, D)
    output_result(U, write)

solve()