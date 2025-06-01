from heapq import heappush, heappop
from sys import stdin
INF = 10**20

def main():
    n, m, x = map(int, stdin.readline().split())
    tlst = list(map(int, (stdin.readline() for _ in range(n))))
    edges = [[] for _ in range(n)]
    for _ in range(m):
        a, b, d = map(int, stdin.readline().split())
        a, b = a-1, b-1
        edges[a].append((b, d))
        edges[b].append((a, d))

    dist = {}
    heap = [(0, x, x, x-1)]  # distance, cold, hot, room
    dist[(x, x, x-1)] = 0

    while heap:
        total, cold, hot, node = heappop(heap)
        if node == n-1:
            print(total)
            return
        if dist[(cold, hot, node)] < total:
            continue
        for nxt, d in edges[node]:
            ncold = max(0, cold - d)
            nhot = max(0, hot - d)
            t = tlst[nxt]
            if t == 1 or (t == 0 and nhot == 0) or (t == 2 and ncold == 0):
                ntotal = total + d
                if t == 0: ncold = x
                if t == 2: nhot = x
                key = (ncold, nhot, nxt)
                if ntotal < dist.get(key, INF):
                    dist[key] = ntotal
                    heappush(heap, (ntotal, ncold, nhot, nxt))
    print(min((dist.get((ct, ht, n-1), INF) for ct in range(x+1) for ht in range(x+1)), default=-1))

main()