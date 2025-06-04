from collections import Counter, defaultdict, deque
import sys
import bisect
import math
import itertools
import string
import queue
import copy
# numpy and scipy - not currently using
from itertools import permutations, combinations
from heapq import heappop, heappush
#input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 1000000007

# Quick input functions. Somewhat cryptic but makes things easy for me
def inp():
    return int(input())
def inpm():
    # expecting two (or more) ints on one line
    return map(int, input().split())
def inpl():
    return list(map(int, input().split()))
def inpls():
    return list(input().split())
def inplm(n):  # get n lines, one int per line
    return [int(input()) for _ in range(n)]
def inpll(n):  # get n lines of int lists
    # wish Python had typed lists...
    return [list(map(int, input().split())) for _ in range(n)]

def bfs(start, n, graph):
    visited = [False for _ in range(n)]
    dist = [0]*n
    queue2 = deque()
    queue2.append(start)
    visited[start] = True
    while len(queue2):  # probably more pythonic to just "while queue2"
        curr = queue2.pop()
        for ne in range(len(graph[curr])):
            nex = graph[curr][ne]
            if visited[nex]:
                continue
            dist[nex] = dist[curr] + 1
            visited[nex] = True
            queue2.append(nex)
    return dist

def main():
    n, u, v = inpm()
    # main graph for some tree?
    g = [[] for _ in range(n)]
    g1 = [[] for _ in range(n)]
    ab = []
    for _ in range(n-1):
        a, b = inpm()
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)
        ab.append((a, b))
    dist = bfs(u-1, n, g)
    path = [v-1]
    q2 = deque([v-1])
    d = dist[v-1] - 1
    while q2:
        at = q2.pop()
        for nt in range(len(g[at])):
            nxt = g[at][nt]
            if dist[nxt] == d:
                d -= 1
                path.append(nxt)
                q2.append(nxt)
    ans = int(len(path) / 2) - 1
    path = path[::-1]  # why not just reverse with slicing?
    for i in range(n-1):
        e1, e2 = ab[i]
        # skip the path edge in middle
        if (e1, e2) == (path[ans], path[ans+1]) or (e2, e1) == (path[ans], path[ans+1]):
            continue
        g1[e1].append(e2)
        g1[e2].append(e1)
    dist1 = bfs(path[ans], n, g1)
    xx = ans + max(dist1)
    if len(path) % 2 == 1:
        xx += 1  # is this off-by-one?
    print(xx)

if __name__ == "__main__":
    main()