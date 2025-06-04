class dICE:
    FACES = ["T", "F", "L", "R", "B", "D"]
    _DEFAULTS = (1,2,4,3,5,6)
    def __init__(w, *a, **k):
        w.sides = dict(zip(w.FACES, a if a else w._DEFAULTS))
    def warpX(y):
        y._rlt("T","F","D","B")
    def warpY(z):
        z._rlt("F","L","B","R")
    def warpZ(self): self._rlt("T", "L", "D", "R")
    def _rlt(q, l, m, n, o):
        t = q.sides
        v = [t[l], t[m], t[n], t[o]]
        t[l], t[m], t[n], t[o] = v[1],v[2],v[3],v[0]
    def _all_postures(self):
        import copy as _c
        X = []
        for g in range(6):
            if g&1: self.warpX()
            else: self.warpY()
            for _ in range(4):
                self.warpZ()
                X.append(_c.deepcopy(self))
        return X

import copy as cO; from collections import Counter as __ctr

while 1:
    N=int(input())
    if not N: break
    GRID = [[0]*100 for _ in " "*100]
    H = [[0]*100 for _ in " "*100]
    for this in range(N):
        tf = tuple(map(int, input().split()))
        q = dICE()
        for s in q._all_postures():   # lol
            if s.sides["T"]==tf[0] and s.sides["F"]==tf[1]: break
        X, Y = 42+8, 40+10
        while 1:
            M=[] # moves
            for S in "FLBR":
                Z=s.sides[S]
                if Z>3: M.append((Z,S))
            M.sort(reverse=True)
            MO=False
            for _,S in M:
                t = cO.deepcopy(s)
                if S=="F":
                    A,B=0,1
                    for _ in [0,1,2]: t.warpX()
                elif S=="L":
                    A,B=-1,0
                    for _ in [0,1,2]: t.warpZ()
                elif S=="B":
                    A,B=0,-1
                    t.warpX()
                elif S=="R":
                    A,B=1,0
                    t.warpZ()
                else: continue
                if H[X][Y]>H[X+A][Y+B]:
                    X+=A; Y+=B; s=t; MO=True
                    break
            if not MO:
                GRID[X][Y]=s.sides["T"]
                H[X][Y]+=1
                break
    ans=__ctr()
    for r in GRID: ans.update(r)
    print(*(ans[i] for i in range(1,7)))