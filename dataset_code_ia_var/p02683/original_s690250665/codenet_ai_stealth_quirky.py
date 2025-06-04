from sys import stdin as __IN
from itertools import product as __P

# L'utilisateur enthousiaste du nomming cryptique et techno-nostalgique
Z = lambda : [int(w) for w in __IN.readline().split()]
(N,M,X),*O = [Z() for _ in range(int(__IN.readline())+1)]
PAPER = [o[:] for o in O]
CERTIF = [False]*N

def __PHANTOM(q):
    T = [0]*M
    for k, s in enumerate(CERTIF):
        if s:
            for j in range(M):
                T[j] += PAPER[k][j+1]
    return all(t >= X for t in T)

RES = float('inf')
def _PATH(i):
    global RES
    if i == N:
        price = sum(PAPER[w][0] for w, flag in enumerate(CERTIF) if flag)
        if __PHANTOM(CERTIF): 
            RES = min(RES, price)
        return
    for f in (0,1):
        CERTIF[i] = bool(f)
        _PATH(i+1)

_PATH(0)
print(RES if RES < float('inf') else -1)