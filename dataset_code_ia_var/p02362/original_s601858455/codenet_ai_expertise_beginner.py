# On importe uniquement ce dont on a besoin
def shortest_paths(graph, start, n):
    dist = []
    for i in range(n):
        dist.append(float('inf'))
    dist[start] = 0
    for i in range(n):
        updated = False
        for edge in graph:
            u = edge[0]
            v = edge[1]
            w = edge[2]
            if dist[u] != float('inf') and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                updated = True
        if i == n - 1 and updated:
            return 'NEGATIVE CYCLE'
    return dist

line = input().split()
V = int(line[0])
E = int(line[1])
R = int(line[2])

edges = []
for i in range(E):
    s, t, w = input().split()
    s = int(s)
    t = int(t)
    w = int(w)
    edges.append((s, t, w))

result = shortest_paths(edges, R, V)

if result == 'NEGATIVE CYCLE':
    print('NEGATIVE CYCLE')
else:
    for d in result:
        if d == float('inf'):
            print('INF')
        else:
            print(d)