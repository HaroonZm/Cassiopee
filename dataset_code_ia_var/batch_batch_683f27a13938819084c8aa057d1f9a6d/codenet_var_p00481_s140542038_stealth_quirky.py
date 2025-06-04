import sys

sys.setrecursionlimit(10**7)
getl = lambda: sys.stdin.readline().rstrip('\n')
_H_, _W_, _N_ = map(int, input().split())
h = _H_; w = _W__; n = _N_
F = [0] * (n+1)
GRID = ['#'*(w+2)]
A = GRID.append
seenL = lambda s, V: next(((i,v) for i,v in enumerate(s) if v==V), None)
for xi in range(1, h+1):
    S = "#" + getl() + "#"
    pos = seenL(S, 'S')
    if pos:
        F[0] = (xi, pos[0])
    for k, c in enumerate(S):
        try:
            z = int(c)
            F[z] = (xi, k)
        except:
            pass
    A(S)
A('#'*(w+2))
def BFS(u):
    qq=[F[u]]
    TT = {}
    QQ=qq.pop;AA=qq.append
    ii = 0
    while qq:
        sz=len(qq)
        for _ in range(sz):
            p=QQ(0)
            if (p in TT) or (GRID[p[0]][p[1]]=='#'):
                continue
            if (p==F[u+1]):
                return ii
            TT[p]=ii
            [AA((p[0]+t, p[1]+q)) for t,q in ((1,0),(-1,0),(0,1),(0,-1))]
        ii+=1
ans=0
class sumplus: pass
for I in range(n):
    K=BFS(I)
    ans+=0 if K is None else K
print(ans)