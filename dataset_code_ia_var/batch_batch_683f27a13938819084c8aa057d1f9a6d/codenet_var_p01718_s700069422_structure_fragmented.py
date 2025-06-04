import sys

def get_readline():
    return sys.stdin.readline

def get_write():
    return sys.stdout.write

def compute_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def get_mod():
    return 10 ** 9 + 7

def parse_N_Q(readline):
    return map(int, readline().split())

def parse_P(readline, N):
    return list(map(int, readline().split()))

def init_arrays(N):
    return [0]*N, [0]*N, [0]*N

def mark_cycle_start(used, i):
    used[i] = 1

def is_used(used, i):
    return used[i]

def build_cycle(P, used, i):
    vs = [i]
    s = i + 1
    mark_cycle_start(used, i)
    v = P[i] - 1
    while v != i:
        vs.append(v)
        s += v + 1
        mark_cycle_start(used, v)
        v = P[v] - 1
    return vs, s

def fill_S_K_for_cycle(vs, s, l, S, K, MOD):
    for v in vs:
        S[v] = s
        K[v] = l % MOD

def process_cycles(P, S, K, used, N, MOD):
    for i in range(N):
        if is_used(used, i):
            continue
        vs, s = build_cycle(P, used, i)
        l = len(vs)
        fill_S_K_for_cycle(vs, s, l, S, K, MOD)

def init_segment_tree_N0(N):
    return 2 ** (N - 1).bit_length()

def init_segment_tree_arrays(N, N0):
    return [0]*(2*N0), [1]*(2*N0)

def fill_segment_tree_leaves(N, N0, S, K, S0, K0):
    for i in range(N):
        S0[N0 - 1 + i] = S[i]
        K0[N0 - 1 + i] = K[i]

def merge_values(k0, k1, s0, s1, gcd_func, MOD):
    g = gcd_func(k0, k1)
    lcm_k = k0 // g * k1
    s = ((s0 * k1 + s1 * k0) // g) % MOD
    return lcm_k, s

def build_segment_tree(N0, K0, S0, gcd_func, MOD):
    for i in range(N0-2, -1, -1):
        K0[i], S0[i] = merge_values(K0[2*i+1], K0[2*i+2], S0[2*i+1], S0[2*i+2], gcd_func, MOD)

def query_segment_tree(l, r, N0, K0, S0, gcd_func, MOD):
    L = l + N0
    R = r + N0
    k = 1
    s = 0
    while L < R:
        if R & 1:
            R -= 1
            k, s = merge_values(k, K0[R-1], s, S0[R-1], gcd_func, MOD)
        if L & 1:
            k, s = merge_values(k, K0[L-1], s, S0[L-1], gcd_func, MOD)
            L += 1
        L >>= 1
        R >>= 1
    return s

def parse_query_indices(readline):
    l, r = map(int, readline().split())
    return l - 1, r

def process_queries(Q, readline, write, N0, K0, S0, gcd_func, MOD):
    for _ in range(Q):
        l, r = parse_query_indices(readline)
        res = query_segment_tree(l, r, N0, K0, S0, gcd_func, MOD)
        write("%d\n" % res)

def solve():
    readline = get_readline()
    write = get_write()
    MOD = get_mod()
    N, Q = parse_N_Q(readline)
    P = parse_P(readline, N)
    S, K, used = init_arrays(N)
    process_cycles(P, S, K, used, N, MOD)
    N0 = init_segment_tree_N0(N)
    S0, K0 = init_segment_tree_arrays(N, N0)
    fill_segment_tree_leaves(N, N0, S, K, S0, K0)
    build_segment_tree(N0, K0, S0, compute_gcd, MOD)
    process_queries(Q, readline, write, N0, K0, S0, compute_gcd, MOD)

solve()