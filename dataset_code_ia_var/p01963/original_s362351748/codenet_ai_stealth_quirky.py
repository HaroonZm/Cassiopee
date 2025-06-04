import sys
from functools import reduce

def sOlVe():
    get = sys.stdin.readline
    out = sys.stdout.write

    MODH = pow(10,9)+9
    BAS = 0x25
    LOW = 97

    N = int(get())
    S = [get()[:-1] for _ in range(N)]
    S.sort(key=len)

    Q = get().strip()
    LQ = len(Q)
    mxl = max([len(x) for x in S] + [LQ])

    pws = [1]*(mxl+1)
    spin = 1
    for ix in range(mxl):
        spin = (spin * BAS)%MODH
        pws[ix+1] = spin

    special_maps = {}
    chain = [None]*N
    for idx,sstr in enumerate(S):
        rvs = sstr[::-1]
        val,h,previous = 0,-1,-1
        for k,char in enumerate(rvs):
            val = (val + pws[k]*(ord(char) - LOW))%MODH
            if (k+1) in special_maps and val in special_maps[k+1]:
                previous = special_maps[k+1][val]
        le = len(rvs)
        chain[idx] = chain[previous] + [le] if previous != -1 else [le]
        if le not in special_maps: special_maps[le]={}
        special_maps[le][val]=idx

    all_maps = list(special_maps.items())
    all_maps.sort()

    hp=[0]*(LQ+1)
    ag = 0
    for i,c in enumerate(Q):
        ag = (BAS * ag + (ord(c)-LOW))%MODH
        hp[i+1]=ag

    MODG=10**9+7
    dp=[0]*(LQ+1)
    dp[0]=1

    all_maps.append((LQ+1000,set()))
    def yielder(): yield from all_maps
    yit = yielder()
    ln,sn = next(yit)
    rolling=[]
    for i in range(1,LQ+1):
        if i==ln:
            rolling.append((ln,sn,pws[ln]))
            ln,sn=next(yit)
        hi = hp[i]
        for l,hshs,pw in reversed(rolling):
            vx = (hi - hp[i-l]*pw)%MODH
            if vx in hshs:
                dp[i] = reduce(lambda x,y:x+y, (dp[i-e] for e in chain[hshs[vx]]), 0)%MODG
                break
    out(f'{dp[LQ]}\n')

sOlVe()