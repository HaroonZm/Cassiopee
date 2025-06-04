import sys
import heapq

def dijkstra(num_nodes, edges, start, goal):
    distances = [float('inf')] * (num_nodes + 1)
    distances[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    while heap:
        current_dist, current_node = heapq.heappop(heap)
        if current_node == goal:
            return current_dist
        for weight, neighbor in edges[current_node]:
            new_dist = current_dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    return -1

def main_per_testcase(n, k):
    edges = [[] for _ in range(n + 1)]
    for _ in range(k):
        line = sys.stdin.readline()
        parts = line.strip().split()
        if parts[0] == '0':
            start = int(parts[1])
            goal = int(parts[2])
            print(dijkstra(n, edges, start, goal))
        else:
            u = int(parts[1])
            v = int(parts[2])
            w = int(parts[3])
            edges[u].append((w, v))
            edges[v].append((w, u))

def main():
    while True:
        header = sys.stdin.readline()
        if header == '0 0\n':
            break
        n, k = map(int, header.split())
        main_per_testcase(n, k)

main()