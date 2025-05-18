import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np

N,M,P = map(int,readline().split())
ABC = np.array(read().split(),np.int64)

A = ABC[::3]
B = ABC[1::3]
C = ABC[2::3]

C = P-C

# bellman fordでAからBへの最短距離を求める

INF = 10**18
dist = np.full(N+1,INF,np.int64)
dist[1] = 0
for T in range(N+N+10):
    x = dist[A] + C
    update = (dist[B] > x) & (x < INF//2)
    b = B[update]; x = x[update]
    if T > N:
        dist[b] = -INF
    else:
        ind = x.argsort(); x = x[ind][::-1]; b=b[ind][::-1]
        dist[b] = x

answer = -dist[N]
if answer < 0:
    answer = 0
elif answer == INF:
    answer = -1
print(answer)