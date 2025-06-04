from sys import stdin
from collections import defaultdict

input = stdin.readline

N = int(input())
D = [None, *map(int, (input() for _ in range(N)))]

d_to_i = {d: i for i, d in enumerate(D) if i}
parent = [None] * (N + 1)
size = [1] * (N + 1)
D_subtree = [0] * (N + 1)
edges = []

bl = True
for d in sorted(D[1:], reverse=True)[:-1]:
    i = d_to_i[d]
    d_parent = d - N + 2 * size[i]
    p = d_to_i.get(d_parent)
    if p is None:
        bl = False
        break
    edges.append(f"{i} {p}")
    parent[i] = p
    size[p] += size[i]
    D_subtree[p] += D_subtree[i] + size[i]

root = d_to_i[sorted(D[1:], reverse=True)[-1]]
bl &= (D_subtree[root] == D[root])

print('\n'.join(edges) if bl else -1)