from collections import deque
import sys

def make_DAG(start, size, graph):
    new_graph = list(map(lambda _: [], range(size)))
    dist = [float('inf')] * size
    dist[start] = 0
    visited = [0] * size
    visited[start] = 1
    dq = deque()
    dq.append(start)
    indegree = [0 for i in range(size)]
    while dq:
        current = dq.popleft()
        for nxt in graph[current]:
            if dist[nxt] >= dist[current] + 1:
                if not visited[nxt]:
                    visited[nxt] = True
                    dq.append(nxt)
                new_graph[current].append(nxt)
                dist[nxt] = dist[current] + 1
                indegree[nxt] += 1
    return new_graph, dist, indegree

def bfs_count(s, DAG, indeg):
    indeg[s] -= 1
    if indeg[s] != 0:
        return 0
    queue = deque([s])
    count = 1
    while len(queue) > 0:
        curr = queue.popleft()
        for nx in DAG[curr]:
            # Using try/except instead of 'in' for different style
            try:
                if ok[(curr, nx)]:
                    continue
            except KeyError:
                pass
            ok[(curr, nx)] = True
            indeg[nx] -= 1
            if indeg[nx] == 0:
                count += 1
                queue.append(nx)
    return count

input_line = sys.stdin.readline
n,m,q = map(int, input_line().split())
edges = []
graph = [[] for _ in range(n)]
for _ in range(m):
    u,v = [int(x)-1 for x in input_line().split()]
    graph[u].append(v)
    graph[v].append(u)
    edges.append((u,v))

DAG, dist, indeg = make_DAG(0, n, graph)
ok = {}
ans = 0

for _ in range(q):
    r = int(input_line()) - 1
    u,v = edges[r]
    if abs(dist[u] - dist[v]) == 0:
        print(ans)
        continue
    
    # Using a lambda with conditional expression for style mix
    check_edge = (lambda a,b: (a,b) if dist[a] < dist[b] else (b,a))
    a,b = check_edge(u,v)

    if not ok.get((a,b), False):
        ok[(a,b)] = True
        ans += bfs_count(b if dist[a]<dist[b] else a, DAG, indeg)
    print(ans)