from itertools import product
from collections import deque
import sys

readline = sys.stdin.readline
write = sys.stdout.write

def read_ints():
    return list(map(int, readline().split()))

def compute_factorials(K, MOD):
    fact = [1] * (K + 1)
    rfact = [1] * (K + 1)
    r = 1
    for i in range(1, K + 1):
        fact[i] = r = r * i % MOD
    rfact[K] = r = pow(fact[K], MOD - 2, MOD)
    for i in range(K, 0, -1):
        rfact[i - 1] = r = r * i % MOD
    return fact, rfact

def compute_powers(N, MOD):
    pr6 = [1] * (N + 1)
    base = pow(6, MOD - 2, MOD)
    r = 1
    for i in range(N):
        pr6[i + 1] = r = base * r % MOD
    return pr6

def make_graph_and_edges(M):
    mp = {}
    G = []
    cur = 0
    m = 0
    E = []
    for i in range(M):
        a, b, c = map(int, readline().split())
        if a not in mp:
            mp[a] = cur
            cur += 1
        ma = mp[a]
        if b not in mp:
            mp[b] = cur
            cur += 1
        mb = mp[b]
        if len(G) < cur:
            extension = cur - len(G)
            G.extend([] for _ in range(extension))
        if c == 0:
            G[ma].append(mb)
            G[mb].append(ma)
        else:
            E.append((ma, mb))
            m += 1
    return mp, G, m, E, cur

def bfs_component(G, u, i):
    que = deque()
    que.append(i)
    vs = []
    u[i] = 1
    while que:
        v = que.popleft()
        vs.append(v)
        for w in G[v]:
            if u[w]:
                continue
            u[w] = 1
            que.append(w)
    return vs

def process_components(G, L):
    cr = 0
    lb = [-1] * L
    sz = []
    zz = []
    cc = [0, 0, 0]
    u = [0] * L
    for i in range(L):
        if u[i]:
            continue
        vs = bfs_component(G, u, i)
        s = len(vs)
        if s > 3:
            return None, None, None, None
        for v in vs:
            lb[v] = cr
        sz.append(s)
        zz.append(vs)
        cc[s - 1] += 1
        cr += 1
    return lb, sz, zz, cc

def update_cc(cc, pl, ql, s, sz):
    cc0 = [0] * 3
    cc0[:] = cc
    cc0[sz[pl] - 1] -= 1
    cc0[sz[ql] - 1] -= 1
    cc0[s - 1] += 1
    return cc0

def apply_merge(vs, lb, nl):
    orig_labels = {}
    for v in vs:
        orig_labels[v] = lb[v]
        lb[v] = nl
    return orig_labels

def revert_merge(vs, lb, orig_labels):
    for v in vs:
        lb[v] = orig_labels[v]

def count_k_and_x_y(cc, K, L):
    x = cc[0] + (K - L)
    y = cc[1]
    return x, y

def compute_contrib(x, y, c, fact, pr6, rfact, MOD):
    if x >= y:
        k = (x - y) // 3
        v = fact[x] * pr6[k] % MOD * rfact[k] % MOD
        if c & 1 == 0:
            return v
        else:
            return -v
    return 0

def dfs(state, c, lb, cc, E, m, sz, zz, used, K, L, fact, pr6, rfact, MOD, ans_list):
    if used[state]:
        return
    used[state] = 1
    x, y = count_k_and_x_y(cc, K, L)
    contrib = compute_contrib(x, y, c, fact, pr6, rfact, MOD)
    ans_list[0] = (ans_list[0] + contrib) % MOD
    cc0 = [0] * 3
    for i in range(m):
        if state & (1 << i):
            continue
        p, q = E[i]
        pl = lb[p]
        ql = lb[q]
        if pl != ql:
            s = sz[pl] + sz[ql]
            if s > 3:
                continue
            cc0 = update_cc(cc, pl, ql, s, sz)
            nl = len(sz)
            vs = zz[pl] + zz[ql]
            orig_labels = apply_merge(vs, lb, nl)
            sz.append(s)
            zz.append(vs)
            dfs(state | (1 << i), c + 1, lb, cc0, E, m, sz, zz, used, K, L, fact, pr6, rfact, MOD, ans_list)
            sz.pop()
            zz.pop()
            revert_merge(vs, lb, orig_labels)
        else:
            dfs(state | (1 << i), c + 1, lb, cc, E, m, sz, zz, used, K, L, fact, pr6, rfact, MOD, ans_list)

def output_result(ans):
    write("%d\n" % ans)

def solve():
    MOD = 10 ** 9 + 9
    N, M = map(int, readline().split())
    K = 3 * N

    fact, rfact = compute_factorials(K, MOD)
    pr6 = compute_powers(N, MOD)
    mp, G, m, E, L = make_graph_and_edges(M)
    if len(G) < L:
        extension = L - len(G)
        G.extend([] for _ in range(extension))

    lb, sz, zz, cc = process_components(G, L)
    if lb is None:
        write("0\n")
        return
    used = [0] * (1 << m)
    ans_list = [0]
    dfs(0, 0, lb[:], cc[:], E, m, sz[:], zz[:], used, K, L, fact, pr6, rfact, MOD, ans_list)
    ans = ans_list[0] % MOD
    output_result(ans)

solve()