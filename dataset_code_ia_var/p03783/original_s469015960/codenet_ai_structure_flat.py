N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]

from heapq import heappush, heappop

l0, r0 = P[0]

L = [-l0+1]
R = [l0-1]
s = t = 0
res = 0

i = 0
while i < N-1:
    l0, r0 = P[i]
    l1, r1 = P[i+1]
    s += (r1 - l1)
    t += (r0 - l0)
    x = l1 - 1
    if -s - L[0] <= x <= t + R[0]:
        heappush(L, -x - s)
        heappush(R, x - t)
    elif x < -s - L[0]:
        heappush(L, -x - s)
        heappush(L, -x - s)
        p = -heappop(L) - s
        heappush(R, p - t)
        res += (p - x)
    elif t + R[0] < x:
        heappush(R, x - t)
        heappush(R, x - t)
        p = heappop(R) + t
        heappush(L, -p - s)
        res += (x - p)
    i += 1

print(res)