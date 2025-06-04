from bisect import bisect
import sys
from collections import defaultdict

readline = sys.stdin.readline
write = sys.stdout.write

N_Q = readline().split()
N = int(N_Q[0])
Q = int(N_Q[1])

R = []
for i in range(N):
    R.append(int(readline()))
S = list(set(R))
S.sort()
mp = {}
for i, e in enumerate(S):
    mp[e] = i
D = defaultdict(int)
T = R[:]
T.sort()
mpm = {}
for i, e in enumerate(T):
    mpm[e] = i

INF = 10**9 + 1
ps = []

for i in range(Q):
    line = readline()
    spl = line.split()
    t = spl[0]
    x = int(spl[1])
    if t == 'ADD':
        y = R[x-1]
        if D[y] == 0:
            z = mp[y]
            idx = 0
            l = -1
            r = len(ps)
            while l+1 < r:
                m = (l + r) // 2
                if ps[m] <= z-1:
                    l = m
                else:
                    r = m
            idx = r
            ps = ps[:idx] + [z] + ps[idx:]
        D[y] += 1
    elif t == 'REMOVE':
        y = R[x-1]
        D[y] -= 1
        if D[y] == 0:
            z = mp[y]
            idx = 0
            l = -1
            r = len(ps)
            while l+1 < r:
                m = (l + r) // 2
                if ps[m] <= z-1:
                    l = m
                else:
                    r = m
            if 0 <= r < len(ps):
                ps.pop(r)
    else:
        left = -1
        right = INF
        while left + 1 < right:
            mid = (left + right) >> 1
            prv = -1
            cnt = 0
            for e in ps:
                s = S[e]
                v = mpm[s]
                l2 = -1
                r2 = len(T)
                val = s - mid - 1
                while l2+1 < r2:
                    m2 = (l2 + r2) // 2
                    if T[m2] <= val:
                        l2 = m2
                    else:
                        r2 = m2
                idx = max(r2-1, prv)
                cnt += v - idx
                prv = v
            if N - cnt <= x:
                right = mid
            else:
                left = mid
        if right == INF:
            write("NA\n")
        else:
            write(str(right) + "\n")