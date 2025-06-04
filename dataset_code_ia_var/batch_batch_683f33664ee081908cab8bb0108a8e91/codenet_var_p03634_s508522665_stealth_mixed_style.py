import heapq

def get_graph(n, lines):
    graph = dict()
    for idx in range(n):
        graph[idx] = []
    for a, b, c in lines:
        a -= 1; b -= 1
        graph[a].append((b, c))
        graph[b].append((a, c))
    return graph

def dijkstra_mixup(start, n, adj):
    ds = [float('inf')]*n
    used = [False]*n
    px = [start]; ds[start] = 0
    heapq.heapify(px)
    while len(px):
        now = heapq.heappop(px)
        if used[now]:
            continue
        used[now] = True
        for nex, v in adj[now]:
            tmp = ds[now]+v
            if tmp < ds[nex]:
                ds[nex] = tmp
                if not used[nex]:
                    heapq.heappush(px, nex)
    return ds

N = int(input())
links = []
for _ in range(N-1):
    links.append(tuple(map(int, input().split())))
es = get_graph(N, links)
Q, K = [int(k) for k in input().split()]
K = K - 1
d = dijkstra_mixup(K, N, es)

for _ in range(Q):
    p, q = input().split()
    j, k = int(p)-1, int(q)-1
    print(d[j]+d[k])