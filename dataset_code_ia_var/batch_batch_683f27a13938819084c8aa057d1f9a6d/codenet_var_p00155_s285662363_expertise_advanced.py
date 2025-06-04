import sys
import math
import heapq
from itertools import repeat

INF = float('inf')

def readints():
    return map(int, sys.stdin.readline().split())

def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

def solve_case(n):
    buil_point = [None]*n
    for _ in range(n):
        b, x, y = readints()
        buil_point[b-1] = (x, y)

    adj = [[] for _ in repeat(None, n)]
    for i in range(n):
        pi = buil_point[i]
        for j in range(i+1, n):
            pj = buil_point[j]
            d = dist(pi, pj)
            if d <= 50:
                adj[i].append((d, j))
                adj[j].append((d, i))

    m, = readints()
    for _ in range(m):
        s, g = readints()
        s -= 1; g -= 1
        heap = [(0.0, s, (s,))]
        seen = [INF]*n
        seen[s] = 0.0
        found = False
        while heap:
            cost, v, path = heapq.heappop(heap)
            if v == g:
                print(*[x+1 for x in path])
                found = True
                break
            for wcost, w in adj[v]:
                ncost = cost + wcost
                if seen[w] > ncost:
                    seen[w] = ncost
                    heapq.heappush(heap, (ncost, w, path + (w,)))
        if not found:
            print("NA")

def main():
    stdin = sys.stdin
    while True:
        line = stdin.readline()
        if not line:
            break
        n = int(line)
        if n == 0:
            break
        solve_case(n)

if __name__ == '__main__':
    main()