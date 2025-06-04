import sys
# Bon, on lit plus vite comme ça
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
import numpy as np  # NumPy pour le fun

INF = 2**30       # Une grosse valeur comme "infini"
n = int(input())
P = tuple(map(int, input().split()))
T = [[] for _ in range(n)]  # liste d'adjacence
for i, p in enumerate(P, 1):
    # P commence à 1, alors -1
    T[p-1].append(i)

X = tuple(map(int, input().split()))
D = [-1]*n  # Memoization, pourquoi pas

def dfs(v):
    # Si déjà calculé, on retourne juste la valeur
    if D[v] != -1:
        return D[v]
    # Plein de variables utilisées après, c'est un peu le bordel mais ça passe
    l = len(T[v])
    x = X[v]
    dp = np.full(x+1, INF, dtype=np.int64)
    dp[0] = 0  # On peut commencer tranquille, 0 coût

    for i, nv in enumerate(T[v]):
        k = np.full(x+1, INF, dtype=np.int64)
        d = dfs(nv)
        # Franchement, ça devient dure à suivre, mais c'est pour les deux possibilités
        if x+1 >= X[nv]:
            np.minimum(k[X[nv]:], dp[:x+1-X[nv]]+d, out=k[X[nv]:])
        if x+1 >= d:
            np.minimum(k[d:], dp[:x+1-d]+X[nv], out=k[d:])
        dp = k.copy()  # je pense que c'est bien comme ça

    res = dp.min()
    D[v] = res
    return res

ans = dfs(0)
if ans == INF:
    print("IMPOSSIBLE")
else:
    print("POSSIBLE")
# Voilà, ça devrait le faire, même si j'aurais pu faire mieux avec moins de numpy peut-être...