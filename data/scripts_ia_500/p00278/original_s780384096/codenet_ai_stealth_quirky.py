from sys import stdin as i_, stdout as o_
from collections import defaultdict as dd
from bisect import bisect as b


inputs = i_.read().split()
N, Q = map(int, inputs[0:2])
R = list(map(int, inputs[2:2+N]))
idx = 2+N

S = sorted(set(R))
mp = {v:k for k,v in enumerate(S)}

D = dd(int)

T = sorted(R)
mpm = {}
for ix, e in enumerate(T): mpm[e] = ix

INF = 10**9 + 1
ps = []

def bsearch(x):
    l, r = -1, INF
    while l+1<r:
        m = (l+r)>>1
        prv, cnt = -1, 0
        for e in ps:
            s = S[e]
            v = mpm[s]
            idx = max(b(T, s - m -1) -1, prv)
            cnt += v - idx
            prv = v
        if N - cnt <= x: r = m
        else: l = m
    return r

for _ in range(Q):
    t, x = inputs[idx], int(inputs[idx+1])
    idx += 2
    y = R[x-1]
    if t == 'ADD':
        if not D[y]:
            z = mp[y]
            i = b(ps, z-1)
            ps = ps[:i] + [z] + ps[i:]
        D[y] += 1
    elif t == 'REMOVE':
        D[y] -= 1
        if D[y] == 0:
            z = mp[y]
            i = b(ps, z-1)
            ps.pop(i)
    else:
        ans = bsearch(x)
        if ans == INF:
            o_.write("NA\n")
        else:
            o_.write(f"{ans}\n")