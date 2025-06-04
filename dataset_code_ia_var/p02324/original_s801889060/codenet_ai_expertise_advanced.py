import sys
from itertools import combinations
from math import log2

# Constants
NO_EDGE = 14001

def read_input(stream):
    V, E = map(int, next(stream).split())
    adj = [[NO_EDGE]*V for _ in range(V)]
    for i in range(V):
        adj[i][i] = 0
    odd_mask = 0
    total_weight = 0
    for line in stream:
        s, t, d = map(int, line.split())
        adj[s][t] = adj[t][s] = min(d, adj[s][t])
        odd_mask ^= 1 << s
        odd_mask ^= 1 << t
        total_weight += d
    return V, adj, odd_mask, total_weight

def warshall_floyd(V, adj):
    # Mutates adj
    for k in range(V):
        for i in range(V):
            aik = adj[i][k]
            if aik == NO_EDGE:
                continue
            for j in range(V):
                aij = adj[i][j]
                akj = adj[k][j]
                sum_ = aik + akj
                if aij > sum_:
                    adj[i][j] = sum_
    return adj

def bits_indices(mask):
    # Yields indices of set bits
    i = 0
    while mask:
        if mask & 1:
            yield i
        mask >>= 1
        i += 1

def min_weight_matching(adj, odd_mask):
    # Bitmask-based DP for minimal weight matching on odd degree vertices
    mem = {0: 0}
    N = odd_mask.bit_length()
    indices = list(bits_indices(odd_mask))
    idx_map = {v: i for i, v in enumerate(indices)}
    # State: bitmask over the odd-degree indices
    size = len(indices)
    # Precompute pairwise minimum distances
    dist = [[adj[indices[i]][indices[j]] for j in range(size)] for i in range(size)]

    for pair_mask in range(1, 1<<size):
        if bin(pair_mask).count('1') % 2:
            continue
        mem[pair_mask] = float('inf')
        first = (pair_mask & -pair_mask).bit_length() - 1
        for j in range(first+1, size):
            if pair_mask & (1<<j):
                smaller = pair_mask ^ (1<<first) ^ (1<<j)
                candidate = mem[smaller] + dist[first][j]
                if candidate < mem[pair_mask]:
                    mem[pair_mask] = candidate
    return mem[(1<<size)-1]

def main():
    V, adj, odd_mask, ans = read_input(sys.stdin)
    if odd_mask:
        warshall_floyd(V, adj)
        ans += min_weight_matching(adj, odd_mask)
    print(ans)

if __name__ == "__main__":
    main()