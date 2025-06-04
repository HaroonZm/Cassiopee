import sys
sys.setrecursionlimit(999999)
L = lambda: sys.stdin.readline()
O = lambda txt: sys.stdout.write(txt)
def s0lve():
    W,H,K=[*map(int,L().split())]
    N=int(L())
    Z={}
    for _ in[0]*N:
        x,y= map(int,L().split())
        if y&1: continue
        X= x>>1
        if y not in Z: Z[y]={}
        if x&1:
            Z[y][X]=Z[y].get(X,0)|1
            if x<W: Z[y][X+1]=Z[y].get(X+1,0)|4
        else:
            Z[y][X]=Z[y].get(X,0)|2
    if K<W//2: O('-1\n');return
    K-=(W//2+1)
    Q=0
    for y in Z:
        WU=sorted(Z[y].items())
        a,b=0,1e9
        p=-1
        for x,bs in WU:
            if x-p>1:a=b=min(a,b)
            v0=bs&1>0;v1=bs&2>0;v2=bs&4>0
            na,minb=min(a+v0,b+min(v0+v2,2*v1)),min(a,b+v2)
            a,b=na,minb
            p=x
        Q+=min(a,b) if p<W//2 else a
    R=(W//2+1)*(H//2)+max(Q-K,0)-K
    O(f"{max(R,0)}\n")
s0lve()