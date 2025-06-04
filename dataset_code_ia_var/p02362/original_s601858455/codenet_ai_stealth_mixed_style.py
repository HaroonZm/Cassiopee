from sys import stdin
import collections

memo = lambda: None
inf = 1 << 62

def bellman(graph, root, n):
    dist = [inf for _ in range(n)]
    dist[root] = 0
    step = 0
    while step < n:
        updated = False
        for edge in graph:
            u, v = edge[0], edge[1]
            w = graph[edge]
            if dist[u] < inf and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                updated = True
                if step == n-1:
                    return 'NEGATIVE CYCLE'
        if not updated: break
        step += 1
    res = {}
    idx = 0
    while idx < n:
        res[idx] = dist[idx]
        idx += 1
    return res

line = stdin.readline()
tmp = line.rstrip().split()
V = int(tmp.pop(0))
E = int(tmp.pop(0))
R = int(tmp.pop(0))
adj = dict()
count = 0
for j in range(E):
    arr = [int(i) for i in stdin.readline().split()]
    x = arr[0]
    y = arr[1]
    z = arr[2]
    adj[(x,y)] = z
    count += 1
d = bellman(adj, R, V)
show = lambda k: ("INF" if d[k] == inf else d[k]) if d != 'NEGATIVE CYCLE' else None
if d == 'NEGATIVE CYCLE':
    print('NEGATIVE CYCLE')
else:
    n = 0
    while n < V:
        print(show(n))
        n += 1