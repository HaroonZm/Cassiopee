import sys
import math

def flush():
    sys.stdout.flush()

N, K = map(int, input().split())

# Construction of a graph that allows locating any vertex within 10 questions:
# Use a tree of degree at most 20 and height at most 3 because 20^3=8000 > 200.
# We create a k-ary tree (k=20), which is shallow enough.
k = 20
edges = []
parent = [0]*(N+1)

for i in range(2, N+1):
    p = (i - 2)//k + 1
    parent[i] = p
    edges.append((p, i))

print(len(edges))
for a, b in edges:
    print(a, b)
flush()

def query(v):
    print(v)
    flush()
    res = input()
    return res

for _ in range(K):
    # Binary search guided by 'Yes', 'Near', 'No'
    # We know the graph is a k-ary tree with edges printed above.
    # Start from root=1
    candidates = [1]
    visited = set()
    for _ in range(10):
        # Since degree<=k, we query current candidates efficiently
        # To determine exact location, query mid candidate
        # But here, we do a kind of BFS + query approach to prune candidates.

        # For performance, since we must always ask one vertex:
        # We'll maintain a set of candidates that might be the target.

        # At first iteration, candidates=[1], we query 1:
        v = candidates[0]  # always query first candidate
        res = query(v)
        if res == 'Yes':
            break
        elif res == 'Near':
            # Target is neighbor of v
            # So candidates := neighbors of v
            # We have a tree, neighbors are parent and children
            nbrs = []
            if parent[v] != 0:
                nbrs.append(parent[v])
            # find children
            start = (v - 1)*k + 2
            end = min(v*k +1, N)
            for c in range(start, end+1):
                if c <= N:
                    nbrs.append(c)
            candidates = nbrs
            visited = set()
        else:
            # target not v nor neighbors of v
            # eliminate v and neighbors
            elim = {v}
            if parent[v] != 0:
                elim.add(parent[v])
            start = (v - 1)*k + 2
            end = min(v*k +1, N)
            for c in range(start, end+1):
                if c <= N:
                    elim.add(c)
            # candidates exclude those
            if len(candidates) == 1:
                # must find other candidates among all nodes excluding elim
                candidates = [x for x in range(1,N+1) if x not in elim]
            else:
                candidates = [x for x in candidates if x not in elim]

            # If no candidates left (should not happen), fallback to all except elim
            if not candidates:
                candidates = [x for x in range(1,N+1) if x not in elim]

    # Next game starts automatically, loop continues until K games done.