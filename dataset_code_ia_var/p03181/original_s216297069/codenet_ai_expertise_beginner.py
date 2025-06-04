import sys
from collections import deque

# Lire les entrées
n_m = sys.stdin.readline().split()
N = int(n_m[0])
M = int(n_m[1])

# Construire la liste d'adjacence
X = []
for i in range(N):
    X.append([])

for i in range(N-1):
    x_y = sys.stdin.readline().split()
    x = int(x_y[0]) - 1
    y = int(x_y[1]) - 1
    X[x].append(y)
    X[y].append(x)

# Parcours pour trouver l'ordre et les parents
P = []
for i in range(N):
    P.append(-1)

Q = deque()
Q.append(0)
R = []

while len(Q) > 0:
    i = Q.popleft()
    R.append(i)
    for a in X[i][:]:
        if a != P[i]:
            P[a] = i
            # Retirer i des voisins de a
            if i in X[a]:
                X[a].remove(i)
            Q.append(a)

# Fonctions et initialisations
def merge(a, b, m):
    return (a * b) % m

def adj_bu(a, i):
    return a + 1

def adj_td(a, i):
    return a + 1

unit = 1

ME = []
for i in range(N):
    ME.append(unit)
XX = []
for i in range(N):
    XX.append(0)
TD = []
for i in range(N):
    TD.append(unit)

# Calcul de bas en haut
for i in range(len(R) - 1, 0, -1):
    v = R[i]
    XX[v] = adj_bu(ME[v], v)
    p = P[v]
    ME[p] = merge(ME[p], XX[v], M)

# Racine
XX[R[0]] = adj_bu(ME[R[0]], R[0])

# Calcul de haut en bas
for idx in range(N):
    i = R[idx]
    ac = TD[i]
    for j in X[i]:
        TD[j] = ac
        ac = merge(ac, XX[j], M)
    ac = unit
    for j in reversed(X[i]):
        TD[j] = adj_td(merge(TD[j], ac, M), i)
        ac = merge(ac, XX[j], M)
        XX[j] = adj_bu(merge(ME[j], TD[j], M), j)

# Afficher la réponse
for x in XX:
    print(x - 1)