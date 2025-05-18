from math import sqrt
from collections import deque
M = 10**6
prime = [1]*(M+1)
prime[0] = prime[1] = 0
for i in xrange(2, int(sqrt(M))+1):
    if prime[i]:
        for j in xrange(i*i, M+1, i):
            prime[j] = 0
def calc(x):
    k = int(sqrt(x))
    if k % 2:
        p = k/2
        if x <= k**2 + k:
            i = x-k**2
            return (p+1, p-i)
        else:
            i = x-(k**2 + k)
            return (p+1-i, -p-1)
    else:
        p = k/2
        if x <= k**2 + k:
            i = x-k**2
            return (-p, -p+i)
        else:
            i = x-(k**2+k)
            return (-p+i, p)
C = map(calc, xrange(M+1))
dic = {x: i+1 for i, x in enumerate(C)}
while 1:
    m, n = map(int, raw_input().split())
    if m == n == 0:
        break
    used = {}
    deq = deque()
    deq.append(n)
    used[n] = prime[n]
    u = set()
    while deq:
        c = deq.popleft()
        if c in u:
            continue
        u.add(c)
        x, y = C[c-1]
        for dx in [-1, 0, 1]:
            v = dic.get((x+dx, y+1), M+1)
            if v <= m:
                deq.append(v)
                used[v] = max(used[c]+prime[v], used.get(v, 0))
    cnt = 0; num = 0
    for k in used:
        if prime[k]:
            if cnt < used[k]:
                cnt = used[k]
                num = k
            elif cnt == used[k] and num < k:
                num = k
    print cnt, num