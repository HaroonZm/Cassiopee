from heapq import heappush, heappop
from sys import stdin

def dijkstra(n, graph, start, goal):
    dist = [float('inf')] * n
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        cost, node = heappop(heap)
        if node == goal:
            return cost
        if cost > dist[node]:
            continue
        for w, nxt in graph[node]:
            alt = cost + w
            if alt < dist[nxt]:
                dist[nxt] = alt
                heappush(heap, (alt, nxt))
    return -1

def process_case(n, k):
    graph = [[] for _ in range(n)]
    input = stdin.readline
    for _ in range(k):
        line = input().split()
        if line[0] == '0':
            start, goal = map(int, line[1:])
            print(dijkstra(n, graph, start, goal))
        else:
            u, v, w = map(int, line[1:])
            graph[u].append((w, v))
            graph[v].append((w, u))

def main():
    input = stdin.readline
    for line in iter(input, '0 0\n'):
        n, k = map(int, line.split())
        process_case(n, k)

if __name__ == '__main__':
    main()