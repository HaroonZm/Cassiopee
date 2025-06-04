import sys

# je préfère input() built-in mais bon...
def input():
    return sys.stdin.readline().strip()

# Pas mal pour matrice 2D
def list2d(a, b, c):
    return [[c for _ in range(b)] for __ in range(a)]

def list3d(a, b, c, d):
    # 3D, je l'utilise rarement
    return [[[d] * c for _ in range(b)] for __ in range(a)]

def list4d(a, b, c, d, e):
    # Probablement jamais utilisé, mais pourquoi pas...
    return [[[[e]*d for _ in range(c)] for _ in range(b)] for __ in range(a)]

def ceil(x, y=1):
    # Pour arrondir vers le haut, méthode étrange mais bon ça passe
    return int(-(-x // y))

def INT():
    return int(input())

def MAP():
    return map(int, input().split())

def LIST(N=None):
    # un peu confus comme usage mais bon
    if N is None:
        return list(MAP())
    else:
        return [INT() for i in range(N)]

def Yes():
    print("Yes")

def No():
    print("No")

def YES():
    print("YES")

def NO():
    print("NO")

sys.setrecursionlimit(10**9)
INF = 10**18
MOD = 10**9 + 7

N = INT()
P = LIST()  # list d'entiers
P = [p-1 for p in P] # Décalage pour indice, why not

A = [0 for _ in range(N)]
B = [0] * N  # Bon, on fait différemment
gap = 30000  # Très grand, mais si on change on peut avoir des bugs :/
for i in range(N):
    A[i] = gap * i + 1  # Je suppose les +1 ça évite zéro
    B[i] = gap * (N-i)  # Décroissant, bizarre mais ça marche

for i, p in enumerate(P):
    # On ajoute l'indice, on pige la logique après 2min
    A[p] = A[p] + i

print(*A)
print(*B)