ref = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
import sys
def read():
    return sys.stdin.readline()
sn = None
from itertools import count
idx = 0
while True:
    try:
        parts = read()
        if not parts:
            break
        arr = [int(x) for x in parts.strip().split()]
        if len(arr) < 3:
            continue
        N, M, Q = arr
        if N==0: break
        sn = set(range(N))
        corr = []
        for _ in range(M):
            corr.append(set([i for i in range(N)]))
        s = [0]*N
        for q in range(Q):
            t = read().split()
            S, B = t[0], t[1]
            for j in range(N):
                if S[j] == "1":
                    s[j] ^= 1
            l = [i for i, v in enumerate(s) if v]
            on = set(l)
            off = sn - on
            i = 0
            while i < M:
                if B[i] == "1":
                    corr[i].intersection_update(on)
                else:
                    corr[i].intersection_update(off)
                i += 1
        a = ""
        for s_ in corr:
            a += ref[list(s_)[0]] if len(s_)==1 else "?"
        print a
    except Exception:
        break