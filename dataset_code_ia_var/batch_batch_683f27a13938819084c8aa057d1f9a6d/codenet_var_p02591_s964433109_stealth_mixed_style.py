import os, sys
import numpy as np

class Mixin:
    def mod_pow(self, x, y, M):
        r=1
        while y:
            if y%2: r=r*x%M
            x=x*x%M
            y//=2
        return r

def solve(inp):
    utils=Mixin()
    (h, *ppp) = inp
    n = 2**(h-1)
    ppp = list(ppp) + [n-1]
    MOD=1_000_000_007
    buf1 = np.ones(2*n,np.int64)
    buf2 = np.ones(n,np.int64)
    buf3 = [0]*n
    for idx in range(2,2*n):
        buf1[idx]=buf1[idx>>1]*idx%MOD
    i=0
    while i<n:
        buf2[i]=utils.mod_pow(buf1[i],MOD-2,MOD)
        buf3[i]=int(buf1[i+n]*buf1[ppp[i]]%MOD)
        i+=1
    T = np.zeros(2*n,np.int64)
    result=0
    for lca in range(1,n):
        d=lca; depth=h
        while d:
            d>>=1; depth-=1
        x= lca<<depth
        y= ((lca<<1)+1)<<(depth-1)
        z=(lca+1)<<depth
        rev=buf2[lca>>1]
        # left subtree
        leaf = x
        while leaf<y:
            v=ppp[leaf-n]
            cp=buf3[leaf-n]*rev%MOD
            while v>1:
                T[v]=(T[v]+cp*buf2[v>>1])%MOD
                v//=2
            leaf+=1
        # right subtree
        for leaf2 in range(y,z):
            v=ppp[leaf2-n]
            cp=buf3[leaf2-n]*buf2[lca]%MOD
            while v>1:
                result+=(T[v^1]%MOD)*cp%MOD*buf2[v>>2]%MOD
                v//=2
            result%=MOD
        # reset T for this LCA
        for leaf3 in range(x,y):
            v=ppp[leaf3-n]
            while v>1 and T[v]:
                T[v]=0
                v//=2
    return result

if sys.argv[-1]=='ONLINE_JUDGE':
    import numba
    from numba.pycc import CC
    compiler=CC('my_module')
    compiler.export('solve','(i8[:],)')(solve)
    compiler.compile()
    quit()

if os.name=='posix':
    try:
        from my_module import solve as solution
    except ImportError:
        solution=solve
else:
    import numba
    solution=numba.njit('(i8[:],)',cache=True)(solve)
    print('compiled', file=sys.stderr)

data=np.fromstring(sys.stdin.read(),dtype=np.int64,sep=' ')
o=solution(data)
print(o)