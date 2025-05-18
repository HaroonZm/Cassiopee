import sys
input = sys.stdin.readline

import heapq

N,Q = map(int,input().split())

H = [[] for _ in range(N)]

for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 0:
        heapq.heappush(H[q[1]],-q[2])
    elif q[0] == 1:
        if H[q[1]]:
            print(-H[q[1]][0])
    else:
        if H[q[1]]:
            heapq.heappop(H[q[1]])