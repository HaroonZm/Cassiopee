import sys
from collections import defaultdict
import heapq

sys.setrecursionlimit(10**7)

INF = float('inf')
EPS = 1e-13
MOD = 10**9 + 7
DIRECTIONS_4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIRECTIONS_8 = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

input = sys.stdin.readline

def LI(): return list(map(int, sys.stdin.readline().split()))
def LI_(): return [x - 1 for x in LI()]
def LF(): return list(map(float, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return sys.stdin.readline().rstrip()
def pf(s): return print(s, flush=True)

def dijkstra(graph, start, n):
    dist = [INF] * (n + 1)
    visited = [False] * (n + 1)
    dist[start] = 0
    hq = [(0, start)]
    while hq:
        cur_dist, u = heapq.heappop(hq)
        if visited[u]:
            continue
        visited[u] = True
        for v, length, _ in graph[u]:
            if not visited[v] and dist[v] > cur_dist + length:
                dist[v] = cur_dist + length
                heapq.heappush(hq, (dist[v], v))
    return dist

def solve_case(n, m, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v, d, c in edges:
        graph[u].append((v, d, c))
        graph[v].append((u, d, c))
    dist = dijkstra(graph, 1, n)
    result = 0
    for i in range(2, n + 1):
        min_cost = INF
        for j, dlen, cost in graph[i]:
            if dist[i] - dlen == dist[j]:
                min_cost = min(min_cost, cost)
        result += min_cost
    return result

def main():
    results = []
    while True:
        n, m = LI()
        if n == 0 and m == 0:
            break
        edges = [LI() for _ in range(m)]
        results.append(solve_case(n, m, edges))
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()