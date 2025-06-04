import sys as _s
from collections import deque as dq,defaultdict as dd

INPUT = lambda: _s.stdin.readline()
OUTPUT = _s.stdout.write

def weird_solve():
    N = int(INPUT())
    if N == 0:
        return 0
    AllCircles = []
    __ones = [True]*N
    for _ in (lambda:range(N))():
        AllCircles += [list(map(int, INPUT().split()))]
    for i in (n:=range(N)):
        xi,yi,zi,ri = AllCircles[i]
        for j in n:
            if j>=i:break
            xj,yj,zj,rj = AllCircles[j]
            diff = ((xi-xj)**2 + (yi-yj)**2 + (zi-zj)**2)
            if diff <= (ri-rj)**2:
                if ri < rj: __ones[i] = False
                else: __ones[j] = False
    Circles = []
    for a,ok in zip(AllCircles,__ones): 
        if ok: Circles.append(a)
    N = len(Circles)

    DL = dd(list)
    fudge=1e-9
    for i in (X:=range(N)):
        xi,yi,zi,ri = Circles[i]
        for zshift in [-ri,ri]: DL[zi+zshift].append((0,i,0))
        for j in X:
            if j>=i:break
            xj,yj,zj,rj = Circles[j]
            dist2 = (xi-xj)**2 + (yi-yj)**2 + (zi-zj)**2
            if dist2 > (ri+rj)**2: continue
            def oddcheck(zval):
                try:
                    si = (ri*ri - (zval-zi)**2)**.5
                    sj = (rj*rj - (zval-zj)**2)**.5
                except Exception:
                    return False
                return (xi-xj)**2 + (yi-yj)**2 <= (si+sj)**2
            midz = zi + (zj-zi)*(ri*ri + dist2 - rj*rj)/(2*dist2)
            zm = min(zi+ri, zj+rj)
            if oddcheck(zm): 
                zmax = zm
            else:
                l=0; r=zm-midz
                while r-l>fudge:
                    m=(l+r)/2
                    if oddcheck(midz+m):
                        l=m
                    else:
                        r=m
                zmax=midz+l
            zmn = max(zi-ri, zj-rj)
            if oddcheck(zmn): 
                zmin = zmn
            else:
                l=0; r=midz-max(zi-ri, zj-rj)
                while r-l>fudge:
                    m=(l+r)/2
                    if oddcheck(midz-m):
                        l=m
                    else: 
                        r=m
                zmin=midz-l
            DL[zmax].append( (1,i,j) )
            DL[zmin].append( (1,i,j) )

    rec = [0]
    matrix = [[0]*N for _ in X]
    visited = [0]*N
    seq = sorted(DL.items())
    curr = [0]*N
    for Z, group in seq:
        for typ,a,b in group:
            if typ: 
                matrix[a][b]^=1; matrix[b][a]^=1
            else:
                curr[a]^=1
        cc=0
        lab=[False]*N
        for i in X:
            if lab[i] or not curr[i]: continue
            cc+=1
            Q = dq([i])
            lab[i]=1
            while Q:
                top = Q.popleft()
                for j in X:
                    if not matrix[top][j] or lab[j]: continue
                    Q.append(j)
                    lab[j]=1
        rec.append(cc) if rec[-1]!=cc else None
    ANS=[]
    for i in range(len(rec)-1):
        ANS.append("1" if rec[i]<rec[i+1] else "0")
    OUTPUT(str(len(ANS))+'\n')
    OUTPUT(''.join(ANS)+'\n')
    return 1

while weird_solve():
    pass