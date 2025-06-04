import sys
from bisect import bisect

def read_input():
    return sys.stdin.readline()

def simple_construct(N, S, base, MOD):
    L = 26
    root = [0, 0, N-1, [None] * L]
    all_nodes = [root]
    for i in range(len(S)):
        curr_node = root
        for c in S[i]:
            h, a, b, next_nodes = curr_node
            if next_nodes[c] is None:
                new_hash = (h * base + c + 1) % MOD
                next_nodes[c] = [new_hash, i, i, [None] * L]
                all_nodes.append(next_nodes[c])
            else:
                node = next_nodes[c]
                node[1] = min(node[1], i)
                node[2] = max(node[2], i)
            curr_node = next_nodes[c]
    hashes = {}
    for h, a, b, _ in all_nodes:
        hashes[h] = (a, b)
    return hashes

def main():
    data = read_input().split()
    N, Q = int(data[0]), int(data[1])
    MOD = 10 ** 18 + 3
    base = 41
    ca = ord('a')
    
    def to_idx(x):
        return ord(x) - ca
    
    A = []
    for i in range(N):
        s = read_input().strip()
        A.append(list(map(to_idx, s)))
    A.sort()
    ha = simple_construct(N, A, base, MOD)
    
    B = []
    for i, s in enumerate(A):
        rev_s = s[::-1]
        B.append((rev_s, i))
    B.sort(key=lambda x: x[0])
    C = [0] * N
    for i, (b, j) in enumerate(B):
        C[j] = i
    B_only = [b for (b, _) in B]
    hb = simple_construct(N, B_only, base, MOD)
    
    N0 = 1
    while N0 < N:
        N0 *= 2
    data2 = [None] * (2 * N0)
    for i in range(N):
        data2[N0 - 1 + i] = [C[i]]
    for i in range(N, N0):
        data2[N0 - 1 + i] = [-1]
    for i in range(N0 - 2, -1, -1):
        p = data2[2 * i + 1]
        q = data2[2 * i + 2]
        merged = []
        a, b = 0, 0
        while a < len(p) and b < len(q):
            if p[a] < q[b]:
                merged.append(p[a])
                a += 1
            else:
                merged.append(q[b])
                b += 1
        while a < len(p):
            merged.append(p[a])
            a += 1
        while b < len(q):
            merged.append(q[b])
            b += 1
        data2[i] = merged
    
    def seg_query(l, r, a, b):
        L = l + N0
        R = r + N0
        res = 0
        while L < R:
            if R % 2 == 1:
                R -= 1
                res += bisect(data2[R - 1], b - 1) - bisect(data2[R - 1], a - 1)
            if L % 2 == 1:
                res += bisect(data2[L - 1], b - 1) - bisect(data2[L - 1], a - 1)
                L += 1
            L //= 2
            R //= 2
        return res

    for _ in range(Q):
        line = read_input()
        if not line:
            continue
        p_str, s_str = line.strip().split()
        h1 = 0
        for c in map(to_idx, p_str):
            h1 = (h1 * base + c + 1) % MOD
        h2 = 0
        for c in map(to_idx, s_str[::-1]):
            h2 = (h2 * base + c + 1) % MOD
        if h1 not in ha or h2 not in hb:
            print(0)
            continue
        p_first, p_last = ha[h1]
        q_first, q_last = hb[h2]
        result = seg_query(p_first, p_last + 1, q_first, q_last + 1)
        print(result)

main()