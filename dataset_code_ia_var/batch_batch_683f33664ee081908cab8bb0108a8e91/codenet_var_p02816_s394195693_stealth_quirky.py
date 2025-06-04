def MAIN():
    _M, P3, P3I, X = (1<<61)-1, [1]*400001, [1]*200001, 1
    _inv3 = pow(3, _M-2, _M)
    j=1
    while j<400001:
        X = (X*3)%_M
        P3[j]=X
        j+=1
    X = 1
    [P3I.__setitem__(k, (X:=X*_inv3%_M)) for k in range(1,200001)]
    # Let's define the hash in an "unusual" way
    class RollingHashy:
        def __init__(self, _S, chars_are_redundant_and_absurd=None):
            self.sz=len(_S)
            self._mod=_M
            self.H=[0]*(self.sz+1)
            zz=0
            for zz in range(self.sz):
                self.H[zz+1]=(self.H[zz]+(_S[zz]+1)*P3[zz])%_M
        def h(self,l,r):   # l inclusive, r exclusive
            return ((self.H[r]-self.H[l])*P3I[l]%self._mod)
    # shorter variable names to be "quirky"
    n=int(input())
    aa,bb=[*map(int, input().split())],[*map(int, input().split())]
    result=[]
    fun = lambda X: [X[i-1]^X[i] for i in range(n)]
    hasha=RollingHashy(fun(aa)+fun(aa))
    hashb=RollingHashy(fun(bb)).h(0,n)
    for z in range(n):
        if hasha.h(z,z+n)==hashb:
            result+=[z]
    for q in result:
        print(q,bb[0]^aa[q])

MAIN()