from heapq import heappush, heappop

while True:
    n, m = map(lambda x:int(x), raw_input().split())
    if n == 0: break
    g = [[] for i in range(n)]
    for i in range(m):
        a,b,c = map(lambda x:int(x), raw_input().split())
        a -= 1
        b -= 1
        g[a].append((b,c))
        g[b].append((a,c))
    heap = []
    visited = [False]*n
    edges = []
    heappush(heap, (0,0))
    while len(heap):
        d,v = heappop(heap)
        if visited[v]: continue
        visited[v] = True
        edges.append(d)
        for u,dd in g[v]:
            if not visited[u]:
                heappush(heap, (dd,u))
    print sorted(edges)[len(edges)/2]