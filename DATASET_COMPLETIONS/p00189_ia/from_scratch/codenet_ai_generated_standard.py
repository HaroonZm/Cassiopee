import sys
import heapq

def dijkstra(start, graph, n):
    dist = [float('inf')] * (n)
    dist[start] = 0
    hq = [(0, start)]
    while hq:
        cost, u = heapq.heappop(hq)
        if dist[u] < cost:
            continue
        for v, w in graph[u]:
            nd = cost + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(hq, (nd, v))
    return dist

def main():
    input = sys.stdin.readline
    while True:
        n = input().strip()
        if n == '0' or n == '':
            break
        n = int(n)
        edges = []
        nodes = set()
        for _ in range(n):
            a,b,c = map(int, input().split())
            edges.append((a,b,c))
            nodes.add(a)
            nodes.add(b)
        max_node = max(nodes) + 1
        graph = [[] for _ in range(max_node)]
        for a,b,c in edges:
            graph[a].append((b,c))
            graph[b].append((a,c))
        ans, mind = 0, float('inf')
        for i in range(max_node):
            dist = dijkstra(i, graph, max_node)
            s = sum(dist)
            if s < mind:
                mind = s
                ans = i
        print(ans, mind)

if __name__ == '__main__':
    main()