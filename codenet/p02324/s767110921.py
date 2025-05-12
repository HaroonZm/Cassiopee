def warshall_floyd(n, dists):
    prev = [t.copy() for t in dists]

    for k in range(n):
        current = [[0] * n for _ in range(n)]
        prev_k = prev[k]
        for i in range(n):
            prev_i, current_i = prev[i], current[i]
            prev_i_k = prev_i[k]
            for j in range(n):
                current_i[j] = min(prev_i[j], prev_i_k + prev_k[j])
        prev = current

    return prev

def solve(n, links, total_d, odd_vertices):
    if not odd_vertices:
        return total_d

    d_table = warshall_floyd(n, links)
    d_table = [[d for oj, d in enumerate(d_table[oi]) if oj in odd_vertices] for ni, oi in enumerate(odd_vertices)]
    ndt = len(d_table)
    bit_dict = {1 << i: i for i in range(ndt)}

    def minimum_pair(remains):
        if not remains:
            return 0
        b = remains & -remains
        remains ^= b
        i = bit_dict[b]
        return min(minimum_pair(remains ^ (1 << j)) + d_table[i][j] for j in range(ndt) if remains & (1 << j))

    return total_d + minimum_pair((1 << ndt) - 1)

v, e = map(int, input().split())

dists = [[float('inf')] * v for _ in range(v)]
for i in range(v):
    dists[i][i] = 0
odd_vertices = [0] * v
total_d = 0

for _ in range(e):
    s, t, d = map(int, input().split())
    dists[s][t] = min(dists[s][t], d)
    dists[t][s] = min(dists[t][s], d)
    odd_vertices[s] ^= 1
    odd_vertices[t] ^= 1
    total_d += d

print(solve(v, dists, total_d, [i for i, v in enumerate(odd_vertices) if v]))