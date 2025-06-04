from bisect import bisect_left
import sys
from collections import Counter
stdin = sys.stdin
stdout = sys.stdout

parse = lambda: map(int, stdin.readline().split())
def get_line():
    return stdin.readline()
N, Q = list(parse())
R = []
for _ in range(N): R.append(int(get_line()))
S = list(set(R))
S.sort()
dpos = dict(zip(S, range(len(S))))
V = Counter()
tmp = sorted(R)
mpm = {v:i for i,v in enumerate(tmp)}
OUT = []
INF = 10**9+1

proc_list = []
for __ in range(Q):
    t, x = get_line().split(); x = int(x)
    if t == "ADD":
        r = R[x-1]
        if not V[r]:
            k = dpos[r]
            i = 0
            while i < len(proc_list) and proc_list[i] < k: i += 1
            proc_list.insert(i,k)
        V[r] += 1
    elif t == "REMOVE":
        r = R[x-1]
        V[r] -= 1
        if V[r] == 0:
            k = dpos[r]
            idx = 0
            while idx < len(proc_list) and proc_list[idx] < k: idx += 1
            if idx < len(proc_list) and proc_list[idx] == k:
                del proc_list[idx]
    else:
        l, r = -1, INF
        while l+1 < r:
            m = (l+r)//2
            last = -1
            acc = 0
            for e in proc_list:
                val = S[e]
                v = mpm[val]
                ind = max(bisect_left(tmp, val-m-1)-1, last)
                acc += v - ind
                last = v
            if N - acc <= x:
                r = m
            else:
                l = m
        if r == INF:
            stdout.write("NA\n")
        else:
            print(r, file=stdout)