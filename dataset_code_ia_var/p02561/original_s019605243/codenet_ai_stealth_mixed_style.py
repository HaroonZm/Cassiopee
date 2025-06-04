import os
import sys
import numpy as np

def funk_resolve(gr, gc, slab):
    shft = 9
    mask = (1<<shft)-1

    # OO mix: functional/object, inner/anonymous
    getind=lambda x,y:(x<<shft)|y
    def splitind(p): return (p>>shft, p&mask)

    def inflow(zmt, pa_L, pa_R, st_x, tar): # imperative
        walk = pa_R[tar]
        while st_x != walk:
            zmt[tar]=walk
            tar = pa_L[walk]
            walk = pa_R[tar]
        zmt[tar]=walk

    def st_path(origin, nl, nr, elist, zmt): # c-style, explicit buffers, lower-level
        left_pa = np.full(nl, -1, np.int64)
        right_pa = np.full(nr, -1, np.int64)
        buf = np.zeros(nl+6, np.int64)
        head, tail = 0, 1
        buf[0] = origin
        inQ = [0]*nl
        inQ[origin]=1
        while head < tail:
            me = buf[head]
            head += 1
            for idx in range(4):
                nb = elist[me, idx]
                if nb == -1: break
                match = zmt[nb]
                if match==-1:
                    right_pa[nb]=me; inflow(zmt, left_pa, right_pa, origin, nb); return nb
                if not inQ[match]:
                    left_pa[match]=nb
                    right_pa[nb]=me
                    buf[tail]=match; tail+=1
                    inQ[match]=1
        return -1

    L, R, invR = [], [], {}
    for x in range(1, gr+1):
        for y in range(1, gc+1):
            if slab[x, y]:continue
            pr = getind(x,y)
            if (x^y)&1:
                L.append(pr)
            else:
                invR[pr]=len(R)
                R.append(pr)
    nl,nr=len(L),len(R)
    mv = [-(1<<shft), -1, 1, (1<<shft)]

    conn = np.full((nl, 4), -1, np.int64)
    for ix, p in enumerate(L):
        ki = 0
        for d in mv:
            nptr = p+d
            if nptr in invR:
                conn[ix, ki]=invR[nptr]; ki+=1

    matches = np.full(nr, -1, np.int64)
    for ix in range(nl):
        st_path(ix, nl, nr, conn, matches)

    total=0
    for j in range(nr):
        i = matches[j]
        if i==-1: continue
        ir, ic = splitind(L[i])
        jr, jc = splitind(R[j])
        if ir==jr:
            a,b=(ic,jc) if ic<jc else (jc,ic)
            slab[ir,a]=4; slab[jr,b]=5
        else:
            a,b=(ir,jr) if ir<jr else (jr,ir)
            slab[a,ic]=2; slab[b,jc]=3
        total+=1
    return total

SIG = '(i8,i8,i1[:,:],)'
if sys.argv[-1]=='ONLINE_JUDGE':
    from numba.pycc import CC
    macc=CC('my_modx')
    macc.export('funk_resolve', SIG)(funk_resolve)
    macc.compile()
    exit()
if os.name=='posix':
    from my_modx import funk_resolve
else:
    from numba import njit
    funk_resolve = njit(SIG, cache=True)(funk_resolve)
    print('compiled', file=sys.stderr)

# Mix parser styles: multiple ways to parse
gr, gc = [int(x) for x in input().split()]
slab = np.ones((gr+2, gc+2), np.int8)
for z in range(gr): slab[z+1,1:gc+1]=[('.#'.index(ch)) for ch in input()]

ret = funk_resolve(gr, gc, slab)
print(ret)
CHRS = (lambda:'.#v^><')()
for x in range(1, gr+1):
    print(''.join(CHRS[i] for i in slab[x,1:gc+1]))