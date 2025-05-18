"""
Shopping in JOI Kingdom
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0562

"""
import sys
from heapq import heappush, heappop
from itertools import combinations

def dijkstra(adj, s):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * len(adj)
    d = [float('inf')] * len(adj)
    d[s] = 0
    pq = []
    heappush(pq, (0, s))
    while pq:
        cost, u = heappop(pq)
        color[u] = BLACK
        if d[u] < cost:
            continue
        for v, cost in adj[u]:
            if color[v] == BLACK:
                continue
            if d[v] > d[u] + cost:
                d[v] = d[u] + cost
                heappush(pq, (d[v], v))
                color[v] = GRAY
    return d

def solve(adj, malls, n):
    distance = dijkstra(adj, malls[0])
    ans = [max([(d + j[1] + distance[j[0]])/2 for j in adj[n]]) for n, d in enumerate(distance[1:], start=1)]
    return int(max(ans) + 0.5) 

def main(args):
    n, m, k = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        f,t, c = map(int, input().split())
        adj[f].append((t, c))
        adj[t].append((f, c))

    malls = [int(input()) for _ in range(k)]
    for f, t in combinations(malls, 2):
        adj[f].append((t, 0))
        adj[t].append((f, 0))
    ans = solve(adj, malls, n)
    print(ans)

if __name__ == '__main__':
    main(sys.argv[1:])