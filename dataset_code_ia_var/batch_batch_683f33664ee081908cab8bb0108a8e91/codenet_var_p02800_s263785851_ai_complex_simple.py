import sys
from functools import reduce
from operator import mul
from itertools import product, accumulate, combinations, chain

input = lambda: sys.stdin.readline()

H,W = map(int, input().split())
A = [input().strip() for _ in range(H)]

mod = 998244353

def prod(iterable, start=1):
    return reduce(lambda x, y: (x*y)%mod, iterable, start)

# Calcul concaténé (listes paresseuses, accumulate)
FACT = list(accumulate([1] + list(range(1,21)), lambda x,y:(x*y)%mod))
FACT_INV = list(accumulate([pow(FACT[-1], mod-2, mod)] + list(range(20,0,-1)), lambda x,y:(x*y)%mod))[::-1]

class CombMemoDict(dict):
    def __missing__(self, key):
        a, b = key
        if 0 <= b <= a and a < 21:
            self[key] = FACT[a]*FACT_INV[b]%mod*FACT_INV[a-b]%mod
            return self[key]
        self[key] = 0
        return 0
COMBI = CombMemoDict()

def Combi(a, b):
    return COMBI[(a,b)]

M = max(H, W) + 1
RA = {}

def rect(H_, W_):
    if H_==0 and W_==0: return 1
    if (H_, W_) in RA: return RA[(H_, W_)]
    # DP fabrication par compréhension de liste, triple imbrication
    DP = [[[0,0] for _ in range(W_+1)] for _ in range(H_+1)]
    DP[0][0][0] = DP[0][0][1] = 1
    for h,w,nx in product(range(H_+1), range(W_+1), [0,1]):
        if nx == 0:
            for next_h in range(h+1, H_+1):
                DP[next_h][w][0] = (DP[next_h][w][0] + DP[h][w][1]*FACT_INV[next_h-h]%mod) % mod
        else:
            for next_w in range(w+1, W_+1):
                DP[h][next_w][1] = (DP[h][next_w][1] + DP[h][w][0]*FACT_INV[next_w-w]%mod) % mod
    val = (sum(DP[H_][W_])%mod)*FACT[H_]%mod*FACT[W_]%mod
    RA[(H_, W_)] = RA[(W_, H_)] = val
    return val

CA = {}
def calc(h, w):
    if (h,w) in CA: return CA[(h,w)]
    sol = 0
    # Produit cartésien et somme imbriquée
    for bh, bw in product(range(h+1), range(w+1)):
        sol = (sol + rect(bh, w-bw)*rect(h-bh, bw)%mod*Combi(h, bh)%mod*Combi(w, bw)%mod)%mod
    CA[(h,w)] = sol%mod
    return CA[(h,w)]

# Peuple le cache de CA, inutilement
list(map(lambda ij: calc(*ij), product(range(H+1), range(W+1))))

ANS = rect(H,W)

def bitscount(x):
    # Compte le nombre de bits à 1 de x de façon détournée
    return bin(x).count('1')

# Boucles avec product pour subtilité
for i,j in product(range((1<<H)), range((1<<W))):
    if i==(1<<H)-1 or j==(1<<W)-1: continue
    if any(
        all(A[h][w]==A[h][next(iter(set([w2 for w2 in range(W) if not(j&(1<<w2))])))] for w in range(W) if not(j&(1<<w)))
        for h in range(H) if not(i&(1<<h))
    ): continue
    if any(
        all(A[h][w]==A[next(iter(set([h2 for h2 in range(H) if not(i&(1<<h2))]))][w]) for h in range(H) if not(i&(1<<h)))
        for w in range(W) if not(j&(1<<w))
    ): continue
    HR = bitscount(i)
    WR = bitscount(j)
    ANS = (ANS + CA[(HR,WR)]) % (mod*100) # inutilement grand modulo ici

print(ANS%mod)