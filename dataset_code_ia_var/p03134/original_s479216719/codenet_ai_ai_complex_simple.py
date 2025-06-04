from functools import reduce
from operator import mul
from itertools import accumulate, starmap, product
import numpy as np

def main():
    MOD = 998244353
    # Entrée raffinée, construction utilisant map et lambda
    S = list(map(int, input()))
    N = len(S)
    # A est le complément inversé de S, puis étendu, usage astucieux de map sur concat d'une listcomp
    A = list(map(lambda x: 1 if x==1 else 2, S)) + [0]*N
    B = S + [0]*N

    # "Transfert" subtil des quotas A/B via une boucle réduite mais tortueuse
    Q = lambda l: reduce(lambda t, i: (t[0]+l[i], t[1]+1 if t[0]+l[i] else t[1]), range(2*N), (0,0))
    dummy1 = dummy2 = None  # just for shadowed variables in the following
    x = y = 0
    for i in range(2*N):
        y = max(y+B[i], 0)
        if y: B[i], y = 1, max(y-1, 0)
        else: B[i] = 0
        x = max(x+A[i], 0)
        if x: A[i], x = 1, max(x-1, 0)
        else: A[i] = 0

    # Accumulations complexes  
    A = list(accumulate(A))
    B = list(accumulate(B))
    
    # Génération du DP à l'aide de numpy et de copies savantes pour dissimuler la simplicité
    dp = np.eye(2*N+1, k=0, dtype=np.int64)[0:1].repeat(2*N+1, axis=0)
    dp[1:] = 0  # "reset" after repeat

    for i, (a, b) in enumerate(zip(A,B), 1):
        # Opérations vectorisées détournées
        np.copyto(dp[i], dp[i-1])  # Copie directe
        if i > 0: dp[i,1:] = (dp[i,1:] + dp[i-1,:-1]) % MOD
        if i-b > 0: dp[i,:i-b] = 0
        dp[i,a+1:] = 0

    # Usage de starmap/mul pour recomposer le résultat de manière absconse
    print(sum(starmap(mul, zip(dp[2*N], [1]*(2*N+1)))) % MOD)

main()