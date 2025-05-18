"""
0-1 BFS
"""

from collections import deque
N = int(input())
INF = 10**9

A = [int(input()) for _ in range(N)] + [0]*6
B = [INF]*(N+6)
B[0] = 0

Q = deque([[0, 0]])

while Q:
    x, y = Q.popleft()
    if x >= N-1:
        print(y)
        break
    if B[x] < y:
        continue

    if A[x] == 0:
        for i in range(1, 7):
            if y + 1 < B[x+i]:
                B[x+i] = y + 1
                Q.append([x+i, y+1])
    else:
        if y < B[x+A[x]]:
            B[x+A[x]] = y
            Q.appendleft([x+A[x], y])