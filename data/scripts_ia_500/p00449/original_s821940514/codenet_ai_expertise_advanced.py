import sys
import heapq

input = sys.stdin.readline

def dijkstra(n, graph, start, goal):
    dist = [float('inf')] * n
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        cost, node = heapq.heappop(heap)
        if node == goal:
            return cost
        if cost > dist[node]:
            continue
        for weight, neighbor in graph[node]:
            new_cost = cost + weight
            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))
    return -1

def main():
    for line in iter(input, '0 0\n'):
        n, k = map(int, line.split())
        graph = [[] for _ in range(n)]
        for _ in range(k):
            cmd = input()
            if cmd[0] == '0':
                _, s, g = map(int, cmd.split())
                print(dijkstra(n, graph, s, g))
            else:
                _, c, d, e = map(int, cmd.split())
                graph[c].append((e, d))
                graph[d].append((e, c))

main()