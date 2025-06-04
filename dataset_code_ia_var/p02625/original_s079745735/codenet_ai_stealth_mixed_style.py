import sys
from itertools import permutations

def input_(): return sys.stdin.readline()

modu = 1000000007
N, M = [int(x) for x in input_().split()]

# FACTORIALS & INV
def fct(maxx):
    F,G,H=[1],[1],[0,1]
    for i in range(2,maxx+1):
        F.append(F[-1]*i%modu)
        H.append((-H[modu%i]*(modu//i))%modu)
        G.append(G[-1]*H[-1]%modu)
    return F,G,H

F,G,H = fct(6*10**5+10)

def cnn(n,r):
    if r<0 or r>n: return 0
    r = n-r if r>n-r else r
    return F[n]*G[r]*G[n-r]%modu

# dirty mix: imperative + compact
ans = 0
for j in range(N+1):
    term = pow(-1,j)*cnn(N,j)*F[M-j]*G[M-N]
    ans = (ans+term)%modu
res = ans*F[M]*G[M-N]%modu
print(res)

# procedural style (not called, just commented)
def brute(N,M):
    total=0
    for x in permutations(range(M),N):
        bad=False
        for idx, val in enumerate(list(x)):
            if idx==val:
                bad=True;break
        if not bad:
            total+=1
    print(total)