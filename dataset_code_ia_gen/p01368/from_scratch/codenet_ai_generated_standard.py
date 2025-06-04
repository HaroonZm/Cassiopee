import sys
import heapq

def floyd_warshall(n, graph):
    dist = [[float('inf')] * n for _ in range(n)]
    for u in range(n):
        dist[u][u] = 0
    for u, nbrs in graph.items():
        for v, w in nbrs:
            dist[u][v] = min(dist[u][v], w)
            dist[v][u] = min(dist[v][u], w)
    for k in range(n):
        for i in range(n):
            di = dist[i]
            dik = di[k]
            dk = dist[k]
            for j in range(n):
                if dik + dk[j] < di[j]:
                    di[j] = dik + dk[j]
    return dist

def bpm(u, g, match, seen):
    for v in g[u]:
        if not seen[v]:
            seen[v] = True
            if match[v] == -1 or bpm(match[v], g, match, seen):
                match[v] = u
                return True
    return False

def minimum_santa(requests, dist):
    L = len(requests)
    graph = [[] for _ in range(L)]
    for i in range(L):
        p_i, t_i = requests[i]
        for j in range(L):
            if i == j:
                continue
            p_j, t_j = requests[j]
            if t_i + dist[p_i][p_j] <= t_j:
                graph[i].append(j)
    match = [-1]*L
    res = 0
    for u in range(L):
        seen = [False]*L
        if bpm(u, graph, match, seen):
            res += 1
    return L - res

def main():
    input = sys.stdin.readline
    while True:
        N, M, L = map(int, input().split())
        if N == 0 and M == 0 and L == 0:
            break
        graph = {}
        for i in range(N):
            graph[i] = []
        for _ in range(M):
            u,v,d = map(int, input().split())
            graph[u].append((v,d))
            graph[v].append((u,d))
        dist = floyd_warshall(N, graph)
        requests = []
        for _ in range(L):
            p,t = map(int, input().split())
            requests.append((p,t))
        requests.sort(key=lambda x:x[1])
        print(minimum_santa(requests, dist))

if __name__ == "__main__":
    main()