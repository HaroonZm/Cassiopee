import sys
from collections import deque

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

def init_graph(N, M):
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = read_ints()
        add_edge(G, u, v)
    return G

def add_edge(G, u, v):
    G[u-1].append(v-1)
    G[v-1].append(u-1)

def bit_count_init(N):
    N1 = 1 << N
    return [0]*N1, N1

def fill_bit_count(bc, N1):
    for i in range(1, N1):
        bc[i] = bc[i ^ (i & -i)] + 1

def edge_count_init(N1):
    return [0]*N1

def fill_edge_count(ec, N1, N, G):
    for state in range(1, N1):
        ec[state] = count_edges_in_state(state, N, G)

def count_edges_in_state(state, N, G):
    c = 0
    for v in range(N):
        if state_has_vertex(state, v):
            c += count_adjacents_in_state(state, G, v)
    return c >> 1

def state_has_vertex(state, v):
    return (state & (1 << v)) != 0

def count_adjacents_in_state(state, G, v):
    c = 0
    for w in G[v]:
        if state_has_vertex(state, w):
            c += 1
    return c

def dp_init(N1):
    dp = [0] * N1
    dp[1] = 1
    return dp

def process_substates(N, dp, ec, P):
    N0 = 1 << (N-1)
    for s0 in range(1, N0):
        state0 = construct_state0(s0)
        dp[state0] = dp_value(state0, dp, ec, P)

def construct_state0(s0):
    return (s0 << 1) | 1

def dp_value(state0, dp, ec, P):
    state1 = initial_substate(state0)
    v = 0
    while state1:
        if is_state1_valid(state1):
            k = edge_contrib(state0, state1, ec)
            v += dp[state1] * power_contrib(P, k)
        state1 = next_substate(state1, state0)
    return 1 - v

def initial_substate(state0):
    return (state0-1) & state0

def is_state1_valid(state1):
    return (state1 & 1) != 0

def edge_contrib(state0, state1, ec):
    return ec[state0] - ec[state1] - ec[state0 ^ state1]

def power_contrib(P, k):
    return (P/100)**k

def next_substate(state1, state0):
    return (state1 - 1) & state0

def print_result(res):
    sys.stdout.write("%.16f\n" % res)

def main():
    N, M, P = read_ints()
    G = init_graph(N, M)
    bc, N1 = bit_count_init(N)
    fill_bit_count(bc, N1)
    ec = edge_count_init(N1)
    fill_edge_count(ec, N1, N, G)
    dp = dp_init(N1)
    process_substates(N, dp, ec, P)
    print_result(dp[N1-1])

main()