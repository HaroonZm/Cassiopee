import sys
input = sys.stdin.readline

N,s,t = map(int,input().split())

def ask(u,v):
    print(f"? {u} {v}", flush=True)
    d = int(input())
    if d == -1:
        sys.exit()
    return d

dist_s_t = ask(s,t)

prev = [-1]*(N+1)
dist = [None]*(N+1)
dist[s] = 0

from collections import deque
q = deque()
q.append(s)

while dist[t] is None:
    u = q.popleft()
    # Since graph unknown, try all other vertices to find neighbors on shortest path
    # A vertex v adjacent to u satisfies dist(u,t) = 1 + dist(v,t)
    for v in range(1,N+1):
        if dist[v] is not None or v==u:
            continue
        duv = ask(u,v) # distance u->v is unknown for edge check, but not needed here
        dvt = ask(v,t)
        dut = ask(u,t)
        # Actually ask(u,t) and ask(v,t) needed only once per node, optimize:
        # So cache ask(*,t)
        # To reduce asks, cache distances to t:
    # Let's cache distances to t first:
    pass

# Optimized approach:
# First: For all nodes v, ask distance v->t once; store in dt[v]
dt = [None]*(N+1)
for v in range(1,N+1):
    dt[v] = ask(v,t)

dist = [None]*(N+1)
dist[s] = 0
from collections import deque
q = deque([s])

while dist[t] is None:
    u = q.popleft()
    dsut = dt[u]
    for v in range(1,N+1):
        if dist[v] is not None or v==u:
            continue
        # u and v are adjacent if dist(u,t)=dist(v,t)+1
        # Let's verify adjacency by ask distance between u and v:
        dudv = ask(u,v)
        if dudv == 1 and dt[u] == dt[v] + 1:
            dist[v] = dist[u] + 1
            prev[v] = u
            q.append(v)

path = []
cur = t
while cur != -1:
    path.append(cur)
    cur = prev[cur]
path.reverse()

print("!")
print(*path, sep="\n", flush=True)