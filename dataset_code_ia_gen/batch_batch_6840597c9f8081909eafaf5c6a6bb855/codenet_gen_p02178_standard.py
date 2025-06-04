import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N,T,S,E = map(int,input().split())
edges = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b,w = map(int,input().split())
    edges[a].append((b,w))
    edges[b].append((a,w))

dist = [-1]*(N+1)
dist[S] = 0
from collections import deque
q = deque([S])
while q:
    v = q.popleft()
    for nv,w in edges[v]:
        if dist[nv]==-1:
            dist[nv]=dist[v]+1
            q.append(nv)

path = []
cur = E
parent = [-1]*(N+1)
q = deque([S])
visited = [False]*(N+1)
visited[S]=True
while q:
    v=q.popleft()
    if v==E:
        break
    for nv,w in edges[v]:
        if not visited[nv]:
            visited[nv]=True
            parent[nv]=v
            q.append(nv)
if parent[E]==-1 and S!=E:
    print("No")
    exit()

path_nodes=[]
cur=E
while cur!= -1:
    path_nodes.append(cur)
    cur=parent[cur]
path_nodes=path_nodes[::-1]

edge_map = {}
for i in range(N-1):
    a,b,w=0,0,0
# On N-1 edges, fill edge weights in a dict for quick lookup
for a,b,w in [tuple(map(int,input().split())) for _ in range(N-1)]:
    edge_map[frozenset({a,b})] = w

# Since we have already read edges, re-read is not possible.
# Instead, we store w in edges above, so we must find edges on path with weight.
# Rebuild edge_map from edges:
edge_map = {}
for v in range(1,N+1):
    for nv,w in edges[v]:
        if v < nv:
            edge_map[(v,nv)] = w

# Count how many times each node is visited on the path to collect all treasures:
# All nodes must be visited at least once to pick treasures.
# The path is connected, so visiting the nodes on path once suffices.

# Each bridge's durability decreases by T each time we visit endpoints. 
# Number of times an endpoint is visited = number of nodes on path.

k = len(path_nodes)
# We traverse path_nodes from S to E, visiting each node once.
# At each node, all connected edges lose T durability.
# But edges not on path may become invalid but we only need to cross edges on the path.
# So only edges on the path must remain durable.

# Each edge on path connects path_nodes[i] and path_nodes[i+1]
# Its durability must remain positive after visited endpoints decrease:
# Each endpoint visited once => durability after: w_i - 2*T > 0
# But we only visit the endpoints on path once.

for i in range(k-1):
    a,b = path_nodes[i],path_nodes[i+1]
    w = edge_map[(min(a,b),max(a,b))]
    if w - 2*T <= 0:
        print("No")
        exit()
print("Yes")