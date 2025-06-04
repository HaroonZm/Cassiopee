def sOlVe():
    import sys as _s;import itertools as _it
    $=lambda:float(next(_fx));_fx=iter(_s.stdin.read().split())
    _D,__.m=[[{}],{}]
    def Z(b,X):
        k=tuple(X)
        if k in __.m:
            return set((b+l,b+r)for l,r in __.m[k])
        S=set()
        P=set()
        for i in range(1,len(X)):
            for sc in _it.combinations(X,i):
                a,b_=list(sc),X[:]
                [b_.remove(x)for x in a]
                W1,W2=sum(a),sum(b_)
                WW=W1+W2
                B1,B2=b-W2/WW,b+W1/WW
                LT=Z(B1,a)
                RT=Z(B2,b_)
                for lp,ln in LT:
                    for rp,rn in RT:
                        mm=min(lp,rp)
                        nn=max(ln,rn)
                        S.add((mm-b,nn-b))
                        P.add((mm,nn))
        __.m[k]=S;return P
    for _ in range(int(next(_fx))):
        R=$();S=int(next(_fx))
        XX=sorted([int(next(_fx))for _ in range(S)])
        for x in XX:
            __.m[(x,)]=set([(0,0)])
        ES=Z(0,XX)
        try:
            print(max(b-a for a,b in ES if b-a<R))
        except:print(-1)
sOlVe()