from math import sqrt
from collections import deque
M = 10**6
prime = [1]*(M+1)
prime[0] = 0
prime[1] = 0
i = 2
while i <= int(sqrt(M)):
    if prime[i]:
        j = i*i
        while j <= M:
            prime[j] = 0
            j += i
    i += 1

C = []
k = 0
while k <= M:
    kk = int(sqrt(k))
    if kk % 2:
        p = kk//2
        if k <= kk*kk + kk:
            i2 = k-kk*kk
            C.append( (p+1, p-i2) )
        else:
            i2 = k-(kk*kk+kk)
            C.append( (p+1-i2, -p-1) )
    else:
        p = kk//2
        if k <= kk*kk + kk:
            i2 = k-kk*kk
            C.append( (-p, -p+i2) )
        else:
            i2 = k-(kk*kk+kk)
            C.append( (-p+i2, p) )
    k += 1

dic = {}
idx = 0
while idx < len(C):
    dic[C[idx]] = idx+1
    idx += 1

while True:
    s = raw_input()
    mns = s.strip().split()
    m = int(mns[0])
    n = int(mns[1])
    if m == 0 and n == 0:
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
        x = C[c-1][0]
        y = C[c-1][1]
        dx = -1
        while dx <= 1:
            v = dic.get( (x+dx, y+1), M+1 )
            if v <= m:
                deq.append(v)
                if v not in used or used[v] < used[c]+prime[v]:
                    used[v] = used[c]+prime[v]
            dx += 1
    cnt = 0
    num = 0
    ks = used.keys()
    idx2 = 0
    while idx2 < len(ks):
        k2 = ks[idx2]
        if prime[k2]:
            if cnt < used[k2]:
                cnt = used[k2]
                num = k2
            elif cnt == used[k2] and num < k2:
                num = k2
        idx2 += 1
    print cnt, num