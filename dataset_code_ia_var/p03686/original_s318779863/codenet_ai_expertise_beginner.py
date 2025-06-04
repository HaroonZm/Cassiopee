import sys

# Utiliser input normal à la place de sys.stdin.readline pour un débutant
N, M = map(int, input().split())

INF = 2**31 - 1

# Trouver la taille nécessaire pour stocker les informations (en suivant le code d'origine)
LV = (M + 1).bit_length()
N0 = 2 ** LV
data = [0] * (2 * N0)
lazy = [0] * (2 * N0)

# Fonction pour générer les indices à mettre à jour
def gindex(l, r):
    L = (l + N0) >> 1
    R = (r + N0) >> 1
    if l & 1:
        lc = 0
    else:
        lc = (L & -L).bit_length()
    if r & 1:
        rc = 0
    else:
        rc = (R & -R).bit_length()
    for i in range(LV):
        if rc <= i:
            yield R
        if L < R and lc <= i:
            yield L
        L = L >> 1
        R = R >> 1

# Propagation du lazy
def propagates(*ids):
    for i in reversed(ids):
        v = lazy[i - 1]
        if v == 0:
            continue
        lazy[2 * i - 1] += v
        lazy[2 * i] += v
        data[2 * i - 1] += v
        data[2 * i] += v
        lazy[i - 1] = 0

# Mise à jour : ajoute x à l'intervalle [l, r)
def update(l, r, x):
    ids = list(gindex(l, r))
    propagates(*ids)
    L = N0 + l
    R = N0 + r
    while L < R:
        if R % 2 == 1:
            R -= 1
            lazy[R - 1] += x
            data[R - 1] += x
        if L % 2 == 1:
            lazy[L - 1] += x
            data[L - 1] += x
            L += 1
        L = L >> 1
        R = R >> 1
    for i in ids:
        data[i - 1] = min(data[2 * i - 1], data[2 * i])

# Requête du minimum sur [l, r)
def query(l, r):
    propagates(*gindex(l, r))
    L = N0 + l
    R = N0 + r
    s = INF
    while L < R:
        if R % 2 == 1:
            R -= 1
            s = min(s, data[R - 1])
        if L % 2 == 1:
            s = min(s, data[L - 1])
            L += 1
        L = L >> 1
        R = R >> 1
    return s

# Initialisation
for i in range(1, M + 1):
    update(0, i + 1, 1)

add = M - N
hito = []
for i in range(N):
    L, R = map(int, input().split())
    hito.append((L, R))
hito.sort()

for l, r in hito:
    update(0, r + 1, -1)
    m = query(l + 1, M + 2) + l
    if m < add:
        add = m

if -add > 0:
    print(-add)
else:
    print(0)