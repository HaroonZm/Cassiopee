import sys
import heapq

def dijkstra(n, edges, start, goal):
    # n: number of nodes, edges: adjacency list, start: start node, goal: end node
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    while heap:
        cost, u = heapq.heappop(heap)
        if u == goal:
            return cost
        for weight, v in edges[u]:
            total = cost + weight
            if total < dist[v]:
                dist[v] = total
                heapq.heappush(heap, (total, v))
    return -1

def process_case(n, k):
    edges = [[] for _ in range(n + 1)]
    for _ in range(k):
        line = sys.stdin.readline()
        op_and_params = line.strip().split()
        op = op_and_params[0]
        params = list(map(int, op_and_params[1:]))
        if op == '0':
            start, goal = params
            result = dijkstra(n, edges, start, goal)
            print(result)
        else:
            c, d, e = params
            edges[c].append((e, d))
            edges[d].append((e, c))

def main():
    while True:
        line = sys.stdin.readline()
        if line == '0 0\n':
            break
        n, k = map(int, line.strip().split())
        process_case(n, k)

main()