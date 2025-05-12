from math import sqrt
from collections import deque
M = 10**6
prime = [1]*(M+1)
prime[0] = prime[1] = 0
for i in xrange(2, int(sqrt(M))+1):
    if prime[i]:
        for j in xrange(i*i, M+1, i):
            prime[j] = 0
P = {(0, 0): 1}; R = [None, (0, 0)]
c = 1; i = 1; p = 1
x = y = 0
while c < M:
    for j in xrange(i):
        x += p; c += 1
        P[x, y] = c; R.append((x, y))
    for j in xrange(i):
        y -= p; c += 1
        P[x, y] = c; R.append((x, y))
    p = -p
    i += 1
deq = deque()
dd = [-1, 0, 1]
while 1:
    m, n = map(int, raw_input().split())
    if m == n == 0:
        break
    deq.append(n)
    cnts = {n: prime[n]}
    used = set()
    while deq:
        v = deq.popleft()
        x, y = R[v]
        for dx in dd:
            t = P.get((x+dx, y+1), M+1)
            if t <= m:
                cnts[t] = max(cnts[v] + prime[t], cnts.get(t, 0))
                if t not in used:
                    deq.append(t)
                    used.add(t)
    vals = sorted((v, k) for k, v in cnts.items() if prime[k])
    print "%d %d" % vals[-1] if vals else "0 0"