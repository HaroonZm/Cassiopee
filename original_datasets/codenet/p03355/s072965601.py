s = input()
K = int(input())

from heapq import heappush, heappop

Q = set()
u = set()
N = len(s)
for i in range(N):
    for j in range(i+1, i+K+1):
        ss = s[i:j]
        if ss in u:
            continue
        u.add(ss)
        Q.add(ss)
        if len(Q) > K:
            Q.remove(max(Q))
l = sorted(Q)
print(l[K-1])