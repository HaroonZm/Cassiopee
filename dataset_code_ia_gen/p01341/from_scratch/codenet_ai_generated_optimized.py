import sys
import math
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M = map(int, input().split())
coords = [tuple(map(int, input().split())) for _ in range(N)]

def dist(a, b):
    x1, y1 = coords[a]
    x2, y2 = coords[b]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

parent = list(range(N))
rank = [0]*N

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        if rank[a] < rank[b]:
            parent[a] = b
        else:
            parent[b] = a
            if rank[a] == rank[b]:
                rank[a] += 1
        return True
    return False

edges = []
for _ in range(M):
    p, q = map(int, input().split())
    p -= 1
    q -= 1
    edges.append((dist(p,q), p, q))

# The fences enclose areas; to free cats in all enclosed regions,
# we must break enough fences to connect all regions.
# Each fence removed costs its length in holy water.
# The minimum amount corresponds to the minimal total length of fences
# that connect all piles, i.e. the Minimum Spanning Tree (MST)
# with the existing fences as edges. But we must only break a subset to connect all piles,
# so the minimal set of edges connecting all nodes is MST.
# But we want fences to break; the witch creates fences forming enclosed regions,
# so the edges given form polygons (cycles).
# To free all cats, we must delete edges to connect all regions,
# which is removing edges so that the graph is a tree.
# The minimal total length to connect all nodes is MST length.
# Since fences are all edges, the minimal holy water is sum of fence lengths - MST length.
# But problem states amount proportional to length to destroy fences.
# To connect all cats freed, remove M - (N-1) edges with minimal sum.
# So minimal holy water = sum of edges - MST length.

total_length = 0
for w,p,q in edges:
    total_length += w

edges.sort(key=lambda x: x[0])
mst_len = 0
count = 0
for w,p,q in edges:
    if union(p,q):
        mst_len += w
        count += 1
        if count == N - 1:
            break

ans = total_length - mst_len
if ans < 0:
    ans = 0.0
print(f"{ans:.3f}")