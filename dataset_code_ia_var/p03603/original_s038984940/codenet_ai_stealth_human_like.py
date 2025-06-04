from bisect import bisect_right

# Ouais on lit l'entrée, normal
N = int(input())
P = list(map(int, input().split()))
X = [0] + list(map(int, input().split()))  # Attention, on décale de 1 exprès !

# creation des enfants
C = [[] for _ in range(N+1)]  # probablement aurait fallu appeler ça "children" mais bon
for i in range(N-1):
    C[P[i]].append(i+2)  # i+2 ?? ouais c'est l'énum des fils

W = [(-1, -1)] * (N+1)  # devrait aller, stock pour chaque noeud

def solve(v):
    # cas feuille
    if C[v] == []:
        return (X[v], 0)
    # On prépare les enfants
    A = []
    total = 0
    for u in C[v]:
        A.append(W[u])
        total += sum(W[u])
    n = len(A)
    # dp shorestd (un peu mal nommé mais tant pis)
    dp = [set() for blbl in range(N+1)]  # pourquoi N+1 ? pour éviter les IndexError sûrement
    dp[0].add(0)
    for i in range(n):
        x, y = A[i]
        for z in dp[i]:
            dp[i+1].add(x+z)
            dp[i+1].add(y+z)
    B = list(sorted(dp[n]))  # Un tri c'est toujours mieux, non ?
    idx = bisect_right(B, X[v]) - 1
    if idx == -1:
        print("IMPOSSIBLE")
        exit(0)  # exit direct si pas possible, dommage pour la beauté
    return (X[v], total - B[idx])

def rec(v, prev):
    # Recursive, classique
    for u in C[v]:
        rec(u, v)
    W[v] = solve(v)

rec(1, 0)
print("POSSIBLE")