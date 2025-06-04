from math import sqrt
from collections import deque

M = 10**6
prime = [1] * (M + 1)
prime[0] = prime[1] = 0

i = 2
while i <= int(sqrt(M)):
    if prime[i]:
        j = i * i
        while j <= M:
            prime[j] = 0
            j += i
    i += 1

P = {(0, 0): 1}
R = [None, (0, 0)]
c = 1
i = 1
p = 1
x = 0
y = 0
while c < M:
    j = 0
    while j < i:
        x += p
        c += 1
        P[(x, y)] = c
        R.append((x, y))
        j += 1
    j = 0
    while j < i:
        y -= p
        c += 1
        P[(x, y)] = c
        R.append((x, y))
        j += 1
    p = -p
    i += 1

dd = [-1, 0, 1]
while True:
    try:
        s = raw_input()
        if not s:
            continue
        m, n = map(int, s.split())
        if m == 0 and n == 0:
            break
        deq = deque()
        deq.append(n)
        cnts = {n: prime[n]}
        used = set()
        while deq:
            v = deq.popleft()
            x, y = R[v]
            for dx in dd:
                tx, ty = x + dx, y + 1
                t = P.get((tx, ty), M + 1)
                if t <= m:
                    cnts[t] = max(cnts[v] + prime[t], cnts.get(t, 0))
                    if t not in used:
                        deq.append(t)
                        used.add(t)
        vals = sorted((v, k) for k, v in cnts.items() if prime[k])
        if vals:
            print "%d %d" % vals[-1]
        else:
            print "0 0"
    except EOFError:
        break