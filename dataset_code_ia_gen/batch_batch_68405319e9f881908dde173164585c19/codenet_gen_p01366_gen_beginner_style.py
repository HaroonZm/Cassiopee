import sys
import heapq

def dijkstra(n, graph):
    dist = [float('inf')] * (n+1)
    dist[1] = 0
    hq = [(0,1)]
    while hq:
        cd, u = heapq.heappop(hq)
        if dist[u] < cd:
            continue
        for v, d, c in graph[u]:
            nd = cd + d
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(hq, (nd,v))
    return dist

def main():
    input = sys.stdin.readline
    while True:
        line = input()
        if not line:
            break
        N,M = map(int, line.split())
        if N==0 and M==0:
            break
        graph = [[] for _ in range(N+1)]
        edges = []
        for _ in range(M):
            u,v,d,c = map(int, input().split())
            graph[u].append((v,d,c))
            graph[v].append((u,d,c))
            edges.append((u,v,d,c))
        dist = dijkstra(N, graph)
        # Keep only edges that can be on shortest path from capital
        valid_edges = []
        for u,v,d,c in edges:
            if dist[u] + d == dist[v] or dist[v] + d == dist[u]:
                valid_edges.append((u,v,d,c))
        # Build graph with valid edges
        graph2 = [[] for _ in range(N+1)]
        for u,v,d,c in valid_edges:
            graph2[u].append((v,c))
            graph2[v].append((u,c))
        # Minimum spanning tree on valid edges (by cost)
        used = [False]*(N+1)
        hq = [(0,1)]
        total_cost = 0
        while hq:
            c,u = heapq.heappop(hq)
            if used[u]:
                continue
            used[u] = True
            total_cost += c
            for v,nc in graph2[u]:
                if not used[v]:
                    heapq.heappush(hq,(nc,v))
        print(total_cost)

if __name__ == "__main__":
    main()