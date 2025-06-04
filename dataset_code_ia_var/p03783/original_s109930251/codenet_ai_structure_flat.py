N = int(input())
P = []
i = 0
while i < N:
    P.append(list(map(int, input().split())))
    i += 1

INF = 10**18

from heapq import heappush, heappop

l0, r0 = P[0][0], P[0][1]

L = []
heappush(L, -l0+1)
R = []
heappush(R, l0-1)
s = 0
t = 0

res = 0
i = 0
while i < N-1:
    l0, r0 = P[i][0], P[i][1]
    l1, r1 = P[i+1][0], P[i+1][1]
    s += (r1 - l1)
    t += (r0 - l0)
    check_val = l1-1
    if -s-L[0] <= check_val <= t+R[0]:
        heappush(L, -l1+1-s)
        heappush(R, l1-1-t)
    elif check_val < -s-L[0]:
        heappush(L, -l1+1-s)
        heappush(L, -l1+1-s)
        p = -heappop(L)-s
        heappush(R, p-t)
        res += (p - (l1-1))
    elif t+R[0] < check_val:
        heappush(R, l1-1-t)
        heappush(R, l1-1-t)
        p = heappop(R) + t
        heappush(L, -p-s)
        res += (l1-1 - p)
    i += 1
print(res)