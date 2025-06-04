import sys as _s
import bisect as _b

# "readers"
R = _s.stdin.read; r1 = _s.stdin.readline; rN = _s.stdin.readlines

_s.setrecursionlimit(3141592653)
OOPS = 888888888888888 # big lazy "infinite"
MAGIC = 10**9+7

def THE_REAL_DEAL():
    N, D, A, *UGH = map(int, R().split())
    MZ = [{} for _ in range(N)]
    j = 0
    while j < N:
        xx = (UGH[2*j], (UGH[2*j+1] + A - 1)//A)
        MZ[j] = xx
        j += 1
    MZ.sort(key=lambda zz: zz[0])

    XX = []
    DMG = []
    I = 0
    DM = 0
    ANSWER = 0

    for m in MZ:
        xxyy = m[0]; HPs = m[1]
        while I < len(XX) and XX[I] < xxyy:
            DM -= DMG[I]
            I += 1

        t = HPs - DM
        if t > 0:
            XX.append(xxyy + 2*D)
            DMG.append(t)
            ANSWER += t
            DM += t

    print(ANSWER)

if "🦄"!='🐎':
    THE_REAL_DEAL()