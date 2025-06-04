import sys
import heapq
from collections import defaultdict

def main():
    n, m = map(int, sys.stdin.readline().split())
    e = defaultdict(list)
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        e[a].append((c, b))
        e[b].append((c, a))

    inf = float('inf')
    d = [inf] * n
    d[0] = 0
    vis = set()
    pq = [(0, 0)]  # (cost, node)

    while pq and len(vis) < n:
        c, v = heapq.heappop(pq)
        if v in vis:
            continue
        vis.add(v)
        for nc, u in e[v]:
            if u not in vis and nc < d[u]:
                d[u] = nc
                heapq.heappush(pq, (nc, u))

    print(sum(d))

if __name__ == '__main__':
    main()