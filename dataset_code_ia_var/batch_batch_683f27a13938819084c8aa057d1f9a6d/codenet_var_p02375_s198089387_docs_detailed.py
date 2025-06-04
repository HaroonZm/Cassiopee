from collections import deque
import sys

# Augmenter la limite de récursivité dans le cas d'arbres profonds
sys.setrecursionlimit(10**6)

# Fonctions utilitaires pour les entrées/sorties rapides
readline = sys.stdin.readline
write = sys.stdout.write

# Lecture du nombre de nœuds dans l'arbre
N = int(readline())

# Construction du graphe G : G[i] contient la liste des enfants du nœud i
G = [None] * N
for i in range(N):
    k, *c = map(int, readline().split())
    G[i] = c  # Liste des enfants

# H stocke pour chaque nœud l'enfant "lourd" (heavy) selon la décomposition HLD
H = [0] * N
# prv enregistre le parent de chaque nœud
prv = [None] * N

def dfs(v):
    """
    Effectue un parcours en profondeur pour calculer la taille des sous-arbres
    et déterminer le fils "lourd" pour chaque nœud.

    Args:
        v (int): Indice du nœud courant.

    Returns:
        int: Taille totale du sous-arbre enraciné en v.
    """
    s = 1       # Taille du sous-arbre
    heavy = None # Le fils "lourd" avec le plus grand sous-arbre
    m = 0       # Taille maximale trouvée parmi les enfants
    for w in G[v]:
        prv[w] = v  # Enregistrer le parent
        c = dfs(w)  # Taille du sous-arbre pour l'enfant w
        if m < c:
            heavy = w
            m = c
        s += c
    H[v] = heavy
    return s

# Effectue la décomposition heavy-light à partir de la racine (nœud 0)
dfs(0)

# SS = liste des chaînes lourdes
# D = profondeur de la tête de chaque chaîne
SS = []  # Contient les chaînes (listes de nœuds)
D = []   # Profondeur d'entrée de chaque chaîne
L = [0] * N  # Numéro de chaîne auquel appartient chaque nœud
I = [0] * N  # Position du nœud dans sa chaîne

# Construction des chaînes lourdes en BFS
que = deque([(0, 0)])  # (nœud, profondeur)
while que:
    v, d = que.popleft()
    S = []  # Chaîne lourde courante
    k = len(SS)  # Numéro de la chaîne en cours de création
    while v is not None:
        I[v] = len(S)   # Position de v dans sa chaîne
        S.append(v)
        L[v] = k        # Enregistrer à quelle chaîne appartient v
        h = H[v]        # Fils "lourd" de v
        # Enquêter sur les autres fils (non-lourds) pour de futures chaînes
        for w in G[v]:
            if h == w:
                continue
            que.append((w, d+1))
        v = h  # Suivre le chemin "lourd"
    SS.append(S)
    D.append(d)

# C stocke la longueur de chaque chaîne
C = list(map(len, SS))

# Deux tableaux Fenwick (Binary Indexed Tree) pour chaque chaîne pour gérer les ajouts et les requêtes
DS0 = [[0] * (c+1) for c in C]
DS1 = [[0] * (c+1) for c in C]

def add(K, data, k, x):
    """
    Ajoute la valeur x à l'indice k d'un arbre de Fenwick sur K éléments.

    Args:
        K (int): Nombre d'éléments dans l'arbre de Fenwick.
        data (list): Tableau Fenwick à mettre à jour.
        k (int): Indice de mise à jour (1-based).
        x (int): Quantité à ajouter.
    """
    while k <= K:
        data[k] += x
        k += k & -k

def get(K, data, k):
    """
    Calcule la somme des préfixes jusqu'à l'indice k d'un arbre de Fenwick.

    Args:
        K (int): Nombre d'éléments dans l'arbre de Fenwick.
        data (list): Tableau Fenwick.
        k (int): Indice jusqu'où sommer (inclus, 1-based).

    Returns:
        int: Somme des éléments de 1 à k inclus.
    """
    s = 0
    while k:
        s += data[k]
        k -= k & -k
    return s

def query_add(v, x):
    """
    Ajoute la valeur x à l'intervalle (sous-arbre) allant de la racine jusqu'au nœud v
    dans la structure, en appliquant l'opération de majoration descendante sur la HLD.

    Args:
        v (int): Indice du nœud cible.
        x (int): Valeur à ajouter.
    """
    while v is not None:
        l = L[v]        # Numéro de chaîne contenant v
        i = I[v]        # Indice de v dans sa chaîne
        add(C[l], DS1[l], i+1, -x)       # Péage inversé pour la position exacte
        add(C[l], DS1[l], 1, x)          # Ajoute la valeur pour toute la chaîne
        add(C[l], DS0[l], i+1, x*(i+1))  # Péage pondéré par la position
        # Monter à la tête de la chaîne précédente (le parent du sommet de la chaîne courante)
        v = prv[SS[l][0]]

def query_sum(v):
    """
    Calcule la somme de toutes les valeurs accumulées de la racine jusqu'au nœud v.

    Args:
        v (int): Indice du nœud cible.

    Returns:
        int: Somme cumulative de la racine jusqu'à v.
    """
    s = - get(C[0], DS1[L[0]], 1) - get(C[0], DS0[L[0]], 1)
    # Parcourt chaque chaîne en remontant de v à la racine
    while v is not None:
        l = L[v]        # Numéro de chaîne de v
        i = I[v]        # Position de v dans la chaîne
        s += get(C[l], DS1[l], i+1) * (i+1) + get(C[l], DS0[l], i+1)
        # Monter à la chaîne précédente
        v = prv[SS[l][0]]
    return s

# Lecture du nombre de requêtes
Q = int(readline())
ans = []

# Traitement des requêtes une à une
for q in range(Q):
    t, *cmd = map(int, readline().split())
    if t:
        # Requête de somme : afficher la somme jusqu'au nœud cmd[0]
        ans.append(str(query_sum(cmd[0])))
    else:
        # Requête d'ajout : ajouter cmd[1] aux nœuds du chemin
        v, w = cmd
        query_add(v, w)

# Écriture des réponses à la sortie standard
write("\n".join(ans))
write("\n")