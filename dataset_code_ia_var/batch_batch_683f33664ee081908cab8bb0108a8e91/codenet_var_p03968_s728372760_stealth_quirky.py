import sys
from collections import defaultdict as DD
getint = lambda: list(map(int, sys.stdin.readline().split()))
id = lambda x: x
W, = getint()
D = DD(int)
CCC, NNN, SSS = {}, {}, []
for noodle in range(W):
    spot = getint()
    cube = [tuple(spot[j:]+spot[:j]) for j in range(4)]
    z = min(cube)
    for qq in cube: NNN[qq] = z
    D[z] += 1
    CCC[z] = (4 if z[0]==z[1] else 2) if z[0]==z[2] and z[1]==z[3] else 1
    SSS.append(z)
def magic(AX, QB):
    a,b,c,d=AX
    e,h,g,f=QB
    pots = [(a,e,f,b),(b,f,g,c),(c,g,h,d),(d,h,e,a)]
    TT = DD(int)
    for tt in pots:
        if tt not in NNN: return 0
        TT[NNN[tt]]+=1
    ans = 1
    for tkey,qcnt in TT.items():
        for wow in range(qcnt):
            ans *= D[tkey]-wow
        ans *= CCC[tkey]**qcnt
    return ans
SUMREZ = 0
for idx, X in enumerate(SSS):
    D[X]-=1
    for jdx in range(idx+1, W):
        Y = SSS[jdx]
        D[Y]-=1
        SUMREZ += sum(magic(X,tuple(Y[k:]+Y[:k])) for k in range(4))
        D[Y]+=1
print(SUMREZ)