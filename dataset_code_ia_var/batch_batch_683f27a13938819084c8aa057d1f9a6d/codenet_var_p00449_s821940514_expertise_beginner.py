import sys
import heapq

def dijkstra(n, graph, start, goal):
    # Distance to each node initialized to a very large value
    distances = [float('inf')] * (n + 1)
    distances[start] = 0

    # Priority queue for the nodes to visit
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        cost, node = heapq.heappop(heap)
        if node == goal:
            return cost
        for edge_cost, neighbor in graph[node]:
            new_cost = cost + edge_cost
            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))

    return -1  # Goal not reachable

def main():
    read = sys.stdin.readline
    while True:
        line = read()
        if line == '0 0\n':
            break
        n, k = map(int, line.strip().split())
        graph = []
        for i in range(n + 1):
            graph.append([])
        for _ in range(k):
            cmd = read()
            if cmd[0] == '0':
                # Query: find shortest path
                _, a, b = cmd.strip().split()
                a = int(a)
                b = int(b)
                print(dijkstra(n, graph, a, b))
            else:
                # Add edge to the graph
                _, u, v, w = cmd.strip().split()
                u = int(u)
                v = int(v)
                w = int(w)
                graph[u].append((w, v))
                graph[v].append((w, u))

main()