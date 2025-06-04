import sys
import numpy as np
from numba import njit

# -----------------------------------------------------------------------------
# Utilitaires rapides de lecture depuis l'entrée standard via sys.stdin.buffer
# -----------------------------------------------------------------------------
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# Définition d'une constante "infinie" utilisée comme borne
INF = 10**9 + 1

# -----------------------------------------------------------------------------
# Lecture des paramètres de la grille et des obstacles
# -----------------------------------------------------------------------------
# N : nombre de zones "murs" rectangulaires à placer,
# M : nombre de zones "barrières" verticales à placer
N, M = map(int, readline().split())

# Lecture des paramètres de tous les rectangles au format aplati
# Les rectangles sont encodés par groupes de trois entiers
# (coordonnée gauche, coordonnée droite/haut, coordonnée bas/haut ou droite selon type)
data = np.array(read().split(), np.int64)

# Extraction des coordonnées pour chaque type de rectangle
A = data[::3]    # Pour les N "murs" et ensuite les M "barrières"
B = data[1::3]
C = data[2::3]

# Séparation des murs (premiers N) et des barrières (restants)
D = A[N:]  # Débuts d'intervalles horizontaux pour barrières verticales
E = B[N:]
F = C[N:]
A = A[:N]  # Coord liées aux murs
B = B[:N]
C = C[:N]

# -----------------------------------------------------------------------------
# Compression de coordonnées pour optimiser la représentation de la grille
# -----------------------------------------------------------------------------
# Rassembler toutes les coordonnées nécessaires pour axes X et Y
X = np.unique(np.concatenate([A, B, D, [0, -INF, INF]])) # Coord x extrêmes, y compris 0
Y = np.unique(np.concatenate([C, E, F, [0, -INF, INF]])) # Pour coord y

# Différences successives sur X et Y pour calculer l'aire des cases
DX = X[1:] - X[:-1]
DY = Y[1:] - Y[:-1]

# Remplace les coordonnées brutes par leurs indices compressés
A = np.searchsorted(X, A)
B = np.searchsorted(X, B)
C = np.searchsorted(Y, C)
D = np.searchsorted(X, D)
E = np.searchsorted(Y, E)
F = np.searchsorted(Y, F)

# Dimensions de la grille compressée
H, W = len(X), len(Y)
N = H * W   # Nombre total de cases dans la grille (après compression)

# -----------------------------------------------------------------------------
# Construction des structures d'adjacence pour les obstacles dans la grille
# -----------------------------------------------------------------------------
@njit
def set_ng(A, B, C, D, E, F):
    """Construit la liste des positions inaccessibles (liens bloquants/murs) de la grille
    
    Args:
        A, B, C : Début, fin des intervalles horizontaux, hauteur associée pour chaque mur
        D, E, F : Colonne, débuts et fins verticales pour barrières

    Returns:
        head : Tableau, chaque case pointe sur la tête de sa liste d'arêtes bloquées
        ng   : Tableau des destinations d'arêtes bloquées
        nxt  : Prochain index dans la liste adjacente
    """
    p = 0
    head = np.full(N, -1, np.int32)        # Liste chaînée des obstacles pour chaque cellule
    ng = np.empty(4 * N, np.int32)         # À la louche, max 4N liens cassés
    nxt = np.empty(4 * N, np.int32)        # Pointeur vers l'élément suivant

    def add(v, w):
        nonlocal p
        nxt[p] = head[v]
        head[v] = p
        ng[p] = w
        p += 1

    # Murs horizontaux bloquent le passage entre (x, y) <-> (x, y-1)
    for i in range(len(A)):
        a, b, c = A[i], B[i], C[i]
        for x in range(a, b):
            v = x * W + c
            add(v, v - 1)        # Bloque passage bas-haut
            add(v - 1, v)        # Bloque passage haut-bas

    # Barrières verticales bloquent (x, y) <-> (x-1, y)
    for i in range(len(D)):
        d, e, f = D[i], E[i], F[i]
        for y in range(e, f):
            v = d * W + y
            add(v, v - W)        # Bloque passage droite-gauche
            add(v - W, v)        # Bloque passage gauche-droite

    return head, ng[:p], nxt[:p]

# Construction des obstacles sur la grille
head, ng, nxt = set_ng(A, B, C, D, E, F)

# -----------------------------------------------------------------------------
# Calcul des voisins accessibles pour un sommet de la grille, 
# compte tenu des obstacles définis dans set_ng
# -----------------------------------------------------------------------------
@njit
def next_w(head, ng, nxt, v):
    """Retourne la liste des voisins accessibles depuis la cellule v
    
    Args:
        head, ng, nxt : structures d'adjacence calculées par set_ng
        v : index linéarisé de la cellule de la grille

    Returns:
        Liste d'entiers, indices des voisins accessibles
    """
    p = head[v]
    # Quatre voisins candidats : haut, bas, gauche, droite
    V = [v - W, v + W, v - 1, v + 1]
    while p != -1:
        # Retire les liens qui sont bloqués par un mur
        if ng[p] in V:
            V.remove(ng[p])
        p = nxt[p]
    return V

# -----------------------------------------------------------------------------
# Calcul de l'aire accessible depuis la case (0, 0) (origine) en évitant les obstacles,
# ou INF si le domaine n'est pas borné
# -----------------------------------------------------------------------------
# Trouve l'indice compressé correspondant à l'origine pour X et Y
x0, y0 = np.searchsorted(X, 0), np.searchsorted(Y, 0)
v0 = x0 * W + y0  # Index linéarisé de la cellule (0, 0)

@njit
def solve():
    """
    Explore la grille à partir de la cellule d'origine (v0), compte la surface accessible.
    
    Retourne :
        0 si l'une des cases atteignables touche le bord infini (le domaine n'est pas fermé),
        sinon la surface totale accessible à partir de (0,0) en évitant les obstacles.
    """
    visited = np.zeros(N, np.bool_)    # Marqueur des cases visitées
    visited[v0] = 1
    stack = np.empty(N, np.int32)      # Pile pour DFS implicite
    p = 0
    ret = 0                            # Aire totale accumulée

    def area(x):
        # Retourne l'aire de la cellule indexée x (via compression)
        x, y = divmod(x, W)
        return DX[x] * DY[y]

    def push(x):
        nonlocal p, ret
        stack[p] = x
        visited[x] = 1
        ret += area(x)
        p += 1

    def pop():
        nonlocal p
        p -= 1
        return stack[p]

    push(v0)
    while p:
        v = pop()
        for w in next_w(head, ng, nxt, v):
            if visited[w]:
                continue
            x, y = divmod(w, W)
            # Si on atteint un bord externe, alors la zone est illimitée
            if x == 0 or x == H - 1 or y == 0 or y == W - 1:
                return 0
            push(w)
    return ret

# -----------------------------------------------------------------------------
# Exécution du calcul et affichage du résultat
# -----------------------------------------------------------------------------
x = solve()
if x == 0:
    print('INF')
else:
    print(x)