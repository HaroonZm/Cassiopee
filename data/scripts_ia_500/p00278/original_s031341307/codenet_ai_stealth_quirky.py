import bisect, sys as ssys

def g_c(cntlst,ldr,rng):
    cnt,preu = 0,0
    for ldrv in ldr:
        low = bisect.bisect_left(cntlst, ldrv - rng)
        up = bisect.bisect_right(cntlst, ldrv)
        if preu < low:
            cnt += low - preu
        preu = up
    cnt += len(cntlst) - preu
    return cnt

def chk(cntlst,ldr,x):
    if not ldr:
        return 0 if x >= len(cntlst) else 'NA'
    mn = len(cntlst) - bisect.bisect_right(cntlst, ldr[-1])
    if x < mn: return 'NA'

    l,r = 0,cntlst[-1]
    dd = r - 1
    while True:
        m = (l + r) // 2
        x_ = g_c(cntlst,ldr,m)
        if x < x_:
            l = m
        else:
            r = m
        if dd == l - r:
            return r
        dd = l - r

_read = ssys.stdin.readline
n,q = map(int,_read().split())
S = [int(_read()) for _ in range(n)]
Q = [line.split() for line in ssys.stdin]

srtS = sorted(S)
ldr = []

for o,a in Q:
    a = int(a)
    if o.startswith('A'):
        ldr.append(S[a-1])
        ldr.sort()
    elif o.startswith('R'):
        ldr.remove(S[a-1])
    else:
        print(chk(srtS,ldr,a))