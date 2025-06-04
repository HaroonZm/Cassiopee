from collections import deque
import sys
from typing import List, Optional

# Augmente la limite de récursion pour gérer de grands arbres lors du DFS
sys.setrecursionlimit(200000)

# Lecture du nombre de sommets du graphe/arbre
N = int(input())

# G : Liste d'adjacence représentant l'arbre
G: List[List[int]] = [[0]] * N
for i in range(N):
    # Pour chaque sommet, lire ses enfants
    k, *c = map(lambda x: int(x), input().split())
    G[i] = c

# H : pour chaque sommet, stocke son "fils lourd"
H = [0] * N

# prv : pour chaque sommet, stocke son parent
prv: List[Optional[int]] = [None] * N

def dfs(v: int) -> int:
    """
    Effectue un DFS pour calculer la taille des sous-arbres et déterminer le fils lourd de chaque sommet.

    Args:
        v (int): Sommet actuel à traiter.

    Returns:
        int: La taille du sous-arbre enraciné en v.
    """
    s = 1  # La taille du sous-arbre courant
    heavy = None  # Le fils lourd du sommet
    m = 0  # Taille maximale du sous-arbre d'un enfant
    for w in G[v]:
        prv[w] = v  # Définit le parent de l'enfant w
        c = dfs(w)  # Calcule la taille du sous-arbre de w
        if m < c:
            heavy = w  # Met à jour le fils lourd si nécessaire
            m = c
        s += c  # Ajoute la taille du sous-arbre de w à celle de v
    H[v] = heavy  # Stocke le fils lourd de v
    return s

# Lance le DFS depuis la racine (supposée être 0)
dfs(0)

# SS : Listes de chaînes lourdes (heavy paths)
SS: List[List[int]] = []

# D : Profondeur de la tête de chaque chaîne lourde
D: List[int] = []

# L : Numéro de la chaîne lourde de chaque sommet
L = [0] * N

# I : Index du sommet dans sa chaîne lourde
I = [0] * N  # noqa: E741

# Construction des chaînes lourdes à l'aide d'une file pour BFS
que = deque([(0, 0)])  # (sommet, profondeur)
while que:
    v, d = que.popleft()
    S: List[int] = []  # Une nouvelle chaîne lourde
    k = len(SS)  # Numéro de la prochaine chaîne lourde
    while v is not None:
        I[v] = len(S)
        S.append(v)
        L[v] = k
        h = H[v]
        # Ajoute tous les enfants non-lourds à la file
        for w in G[v]:
            if h == w:
                continue
            que.append((w, d + 1))
        v = h  # Passe au sommet suivant dans la chaîne lourde
    SS.append(S)
    D.append(d)

# C : Taille de chaque chaîne lourde
C = list(map(len, SS))

# DS0, DS1 : Structures pour les arbres de Fenwick (BIT) pour chaque chaîne lourde
# DS0 est utilisé pour gérer les préfixes pondérés
DS0 = [[0] * (c + 1) for c in C]
# DS1 pour les préfixes simples
DS1 = [[0] * (c + 1) for c in C]

def add(K: int, data: List[int], k: int, x: int) -> None:
    """
    Ajoute une valeur x à l'index k (1-based) dans un arbre de Fenwick contenant K éléments.

    Args:
        K (int): Taille de la structure.
        data (List[int]): Tableau de l'arbre de Fenwick.
        k (int): Index (1-based) où ajouter x.
        x (int): Valeur à ajouter.
    """
    while k <= K:
        data[k] += x
        k += k & -k

def get(K: int, data: List[int], k: int) -> int:
    """
    Calcule la somme préfixe des éléments jusqu'à l'index k (1-based) dans un arbre de Fenwick.

    Args:
        K (int): Taille de la structure.
        data (List[int]): Tableau de l'arbre de Fenwick.
        k (int): Index (1-based) jusqu'où la somme est prise.

    Returns:
        int: La somme préfixe.
    """
    s = 0
    while k:
        s += data[k]
        k -= k & -k
    return s

def query_add(v: int, x: int) -> None:
    """
    Ajoute une valeur x à tous les sommets du chemin allant de la racine au sommet v,
    en utilisant la décomposition en chaînes lourdes et les arbres de Fenwick par chaîne.

    Args:
        v (int): Sommet auquel s'applique l'opération.
        x (int): Valeur à ajouter.
    """
    while v is not None:
        l = L[v]  # Numéro de la chaîne lourde
        i = I[v]  # Position dans la chaîne lourde
        add(C[l], DS1[l], i + 1, -x)
        add(C[l], DS1[l], 1, x)
        add(C[l], DS0[l], i + 1, x * (i + 1))
        v = prv[SS[l][0]]  # Passe à la tête de la chaîne précédente

def query_sum(v: int) -> int:
    """
    Calcule la somme des valeurs sur le chemin allant de la racine au sommet v,
    en utilisant la décomposition en chaînes lourdes et les arbres de Fenwick par chaîne.

    Args:
        v (int): Sommet auquel s'applique la requête.

    Returns:
        int: La somme demandée.
    """
    s = - get(C[0], DS1[L[0]], 1) - get(C[0], DS0[L[0]], 1)
    while v is not None:
        l = L[v]  # Numéro de la chaîne lourde
        i = I[v]  # Position dans la chaîne lourde
        # Utilisation de deux arbres de Fenwick pour obtenir la somme pondérée
        s += get(C[l], DS1[l], i + 1) * (i + 1) + get(C[l], DS0[l], i + 1)
        v = prv[SS[l][0]]  # Passe à la tête de la chaîne précédente
    return s

# Lecture et traitement des Q requêtes
Q = int(input())
ans = []
for q in range(Q):
    t, *cmd = map(lambda x: int(x), input().split())
    if t:
        # Requête de somme sur le chemin jusqu'à cmd[0]
        ans.append(str(query_sum(cmd[0])))
    else:
        # Requête d'ajout de cmd[1] sur le chemin jusqu'à cmd[0]
        v, w = cmd
        query_add(v, w)
# Affichage des réponses des requêtes de somme
print("\n".join(ans))