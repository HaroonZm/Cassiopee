import sys
from sys import stdin
import heapq

input = stdin.readline

while True:
    s, d = map(int, input().split())
    if s == 0:
        break
    visited = [0] * 100
    Q = []
    to = [[] for _ in range(100)]
    for i in range(s):
        visited[i] = 1
        c = list(map(int, input().split()))
        for j in range(d):
            if c[j] > 0:
                heapq.heappush(Q, (c[j], i, s + j))
    for i in range(d - 1):
        c = list(map(int, input().split()))
        for j in range(i + 1, d):
            if c[j - i - 1] > 0:
                to[s + i].append((s + j, c[j - i - 1]))
                to[s + j].append((s + i, c[j - i - 1]))
    ans = 0
    k = 0
    while k < d:
        while True:
            c, a, b = heapq.heappop(Q)
            if visited[a] == 0 or visited[b] == 0:
                break
        ans += c
        k += 1
        if visited[a]:
            a = b
        visited[a] = 1
        for e, c2 in to[a]:
            if visited[e] == 0:
                heapq.heappush(Q, (c2, a, e))
    print(ans)