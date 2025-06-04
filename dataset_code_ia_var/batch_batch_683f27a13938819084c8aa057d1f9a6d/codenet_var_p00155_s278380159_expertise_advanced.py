import sys
import heapq
from math import hypot

def dijkstra(start, graph):
    dist = [float('inf')] * 101
    prev = [-1] * 101
    dist[start] = 0
    heap = [(0, start)]
    visited = set()

    while heap:
        d, u = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        for v, w in graph[u].items():
            if v not in visited and d + w < dist[v]:
                dist[v] = d + w
                prev[v] = u
                heapq.heappush(heap, (dist[v], v))
    return dist, prev

def reconstruct_path(prev, start, goal):
    path = []
    while goal != -1:
        path.append(goal)
        if goal == start:
            break
        goal = prev[goal]
    else:
        return []
    return path[::-1]

def main(_):
    input = sys.stdin.readline
    while True:
        try:
            n = int(input())
        except Exception:
            break
        if n == 0:
            break
        coords = {}
        for _ in range(n):
            b, x, y = map(int, input().split())
            coords[b] = (x, y)

        graph = [{} for _ in range(101)]
        nodes = list(coords)
        for i in range(len(nodes)):
            b1, (x1, y1) = nodes[i], coords[nodes[i]]
            for j in range(i+1, len(nodes)):
                b2, (x2, y2) = nodes[j], coords[nodes[j]]
                dist = hypot(x1 - x2, y1 - y2)
                if dist <= 50.0:
                    graph[b1][b2] = graph[b2][b1] = dist

        m = int(input())
        queries = [tuple(map(int, input().split())) for _ in range(m)]
        for s, g in queries:
            if s == g:
                print(s)
                continue
            if s not in coords or g not in coords:
                print('NA')
                continue
            dist, prev = dijkstra(s, graph)
            if dist[g] == float('inf'):
                print('NA')
                continue
            path = reconstruct_path(prev, s, g)
            if not path:
                print('NA')
            else:
                print(' '.join(map(str, path)))

if __name__ == "__main__":
    main(sys.argv[1:])