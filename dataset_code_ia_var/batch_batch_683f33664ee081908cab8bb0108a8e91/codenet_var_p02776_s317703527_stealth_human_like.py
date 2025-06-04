import bisect
import os
import sys

# Let's open local input if env stuff is set, not usually like this but whatever 
if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10**9)
INF = float("inf")
IINF = 10**18
MOD = 10**9 + 7
# MOD = 998244353  # people sometimes use the other one

# Read inputs - I wish Python had scanf...
N, M = map(int, sys.stdin.buffer.readline().split())
AB = []
for _ in range(N):
    AB.append(list(map(int, sys.stdin.buffer.readline().split())))

LR = []
for _ in range(M):
    LR.append(list(map(int, sys.stdin.buffer.readline().split())))

AB.sort()  # Sort by first one (I guess that's A)

nums = [(0, 0)] + AB + [(INF, 0)]
A = [xy[0] for xy in nums]
B = [xy[1] for xy in nums]

# Build some kind of graph or something, not sure what they're really doing but here we go
sz = len(nums)
graph = [[] for _ in range(sz)]

# for each LR we mess with the graph, it's a bit ugly
for i in range(M):
    l, r = LR[i]
    v = bisect.bisect_left(A, l) - 1
    u = bisect.bisect_right(A, r) - 1
    graph[v].append( (u, i+1) )
    graph[u].append( (v, i+1) )

parity = [0]*sz
# Seems parity depends on B sequence flipping 0<->1, a bit fishy but let's just do it
for i in range(sz-1):
    if B[i]==0 and B[i+1]==1:
        parity[i] = 1
    if B[i]==1 and B[i+1]==0:
        parity[i] = 1

# Find "trees" - components?
seen = [0]*sz
trees = []
for root in range(sz):
    if seen[root]:
        continue
    if not graph[root]:
        continue
    edges = []
    seen[root] = 1
    stack = [root]
    while stack:
        v = stack.pop()
        for u, eid in graph[v]:
            if seen[u]:
                continue
            seen[u] = 1
            stack.append(u)
            edges.append((v, u, eid))
    if not edges and parity[root]:
        # Single vertex but needs to flip? Impossible
        print(-1)
        sys.exit(0)
    trees.append(edges)

# Rebuild graph with new edges, plus track degrees
graph = [[] for _ in range(sz)]
deg = [0]*sz
for edgegroup in trees:
    for v, u, eid in edgegroup:
        graph[v].append( (u, eid) )
        graph[u].append( (v, eid) )
        deg[v] += 1
        deg[u] += 1

ans = []
marked = [0]*sz
leaves = []
for v in range(sz):
    if deg[v]==1:
        leaves.append(v)

while leaves:
    v = leaves.pop()
    if deg[v]==0:
        continue
    if marked[v]:
        continue
    marked[v]=1
    deg[v]=0
    # Go through connections
    for u, eid in graph[v]:
        if marked[u]:
            continue
        # try to push parity inwards (greedy probably)
        if parity[v] and parity[u]:
            parity[v]=0
            parity[u]=0
            ans.append(eid)
        elif parity[v]==1 and parity[u]==0:
            parity[v]=0
            parity[u]=1
            ans.append(eid)
        deg[u] -= 1
        if deg[u]==1:
            leaves.append(u)

if 1 in parity:
    # oops still left
    print(-1)
else:
    print(len(ans))
    print(*sorted(ans))
# it's probably ok, but pretty unreadable tbh