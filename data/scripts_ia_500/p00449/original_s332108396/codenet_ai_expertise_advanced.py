from sys import stdin
from heapq import heappush, heappop

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

def process_queries(n, k):
    graph = [[] for _ in range(n)]
    input_lines = (stdin.readline() for _ in range(k))
    for line in input_lines:
        cmd, *args = line.split()
        if cmd == '0':
            s, g = map(int, args)
            print(dijkstra(n, graph, s, g))
        else:
            c, d, e = map(int, args)
            graph[c].append((e, d))
            graph[d].append((e, c))

def main():
    for line in stdin:
        if line == '0 0\n':
            break
        n, k = map(int, line.split())
        process_queries(n, k)

if __name__ == '__main__':
    main()