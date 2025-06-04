import sys  # Importation du module système pour interagir avec l'entrée/sortie bas niveau

# Création de raccourcis pratiques pour lire l'entrée standard (stdin) sous forme de bytes
read = sys.stdin.buffer.read         # Permet de lire tout le flux d'entrée sous forme binaire d'un coup
readline = sys.stdin.buffer.readline # Permet de lire une ligne à la fois sous forme binaire
readlines = sys.stdin.buffer.readlines # Permet de lire toutes les lignes sous forme d'une liste de lignes binaires

N = int(readline())  # Lire une ligne avec un entier : le nombre de sommets du graphe/arbre, puis le convertir en entier

# Lire le reste de l'entrée, qui contient une séquence d'entiers séparés par des espaces
data = list(map(int, read().split()))
# La liste 'data' contient : [A1, B1, A2, B2, ..., AN-1, BN-1, S1, S2, ..., SN]
# Ai, Bi sont des entiers reliant deux sommets ; Si sont des valeurs attribuées aux sommets

# Séparation des listes A et B à partir de la liste 'data'
# A contient les numéros de départ des N-1 arêtes (positions paires)
# La notation de tranchage [start:stop:step] sélectionne tous les deux éléments à partir du début jusqu'à 2N-2
A = data[:N+N-2:2]
B = data[1:N+N-2:2]  # B contient les numéros d'arrivée des arêtes (positions impaires)

# Définition d'une très grande valeur qui servira d'infini lors des comparaisons minimales
INF = 10 ** 18 + 100

# Récupération des poids S pour chaque sommet, en ajoutant une valeur 'INF' en position 0, car les sommets sont indexés à partir de 1
S = [INF] + data[-N:]  # On ajoute 'INF' car dans le problème le sommet 0 n'existe pas, mais on aligne ainsi les indices des listes à ceux des sommets

# Création d'une liste d'adjacence (graphe non orienté) pour représenter l'arbre ; chaque élément de la liste est une liste des voisins de ce sommet
graph = [[] for _ in range(N+1)]  # On crée N+1 listes vides, car les sommets vont de 1 à N

# Pour chaque arête de l'arbre, on ajoute les voisins réciproques (non orienté)
for a, b in zip(A, B):
    graph[a].append(b)  # Le sommet b est voisin de a
    graph[b].append(a)  # Le sommet a est voisin de b

# Chercher la racine de l'arbre en choisissant le sommet ayant la valeur S minimale
root = S.index(min(S))  # On prend l'indice où S est le plus petit (correspond à un sommet également)

# Initialiser la liste des parents pour tous les sommets (0 signifie "pas de parent", la racine aura pour parent 0)
parent = [0] * (N+1)  # parent[i] donnera le parent du sommet i
# Liste pour enregistrer l'ordre de parcours des sommets (utile pour le traitement post-ordre)
order = []
# On commence le parcours en profondeur (DFS) avec une pile initialisée à la racine
stack = [root]

# Parcours en profondeur de l'arbre pour remplir la liste 'order' et établir les parents de chaque sommet
while stack:  # Tant que la pile n'est pas vide
    x = stack.pop()  # Retirer le sommet au sommet de la pile
    order.append(x)  # Ajouter ce sommet à l'ordre de parcours

    # Parcourir les voisins du sommet courant dans le graphe
    for y in graph[x]:
        # Si le voisin y est le parent de x, on ne revient pas en arrière (pas de boucle)
        if y == parent[x]:
            continue  # On saute ce voisin

        # Pour les autres voisins (enfants), on définit x comme parent de y
        parent[y] = x
        # Ajouter ce voisin à la pile pour traitement ultérieur (DFS)
        stack.append(y)

# Calcul des tailles des sous-arbres pour chaque sommet
subtree_size = [1] * (N+1)  # Initialisation : chaque sommet compte pour lui-même
# On traite les sommets en ordre inverse de l'ordre de parcours (post-ordre), on agrège les tailles des enfants dans leurs parents
for v in reversed(order):
    subtree_size[parent[v]] += subtree_size[v]  # Ajouter la taille du sous-arbre de v au parent de v

# Préparation de la liste des longueurs (inconnues au départ) sur chaque arête
length = [0] * (N+1)  # On va remplir ce tableau par la suite

# Pour chaque arête (A,B), on calcule la valeur length
for v, p in zip(A, B):  # Pour chaque arête reliant v et p
    # On ajuste l'ordre pour toujours avoir v comme enfant et p comme parent
    if parent[p] == v:
        v, p = p, v  # On échange v et p si nécessaire

    # Calcul de la taille du sous-arbre sous v
    s = subtree_size[v]

    # Calcul de la différence 'd' = nombre de sommets hors du sous-arbre de v moins ceux dans le sous-arbre de v
    d = N - s - s  # N - s donne les sommets hors du sous-arbre, donc N - 2*s est la différence

    # Si d vaut 0 (grande arête centrale entre deux sous-arbres égaux), la longueur n'est pas encore déterminée
    # Sinon, on calcule length[v] comme le quotient (S[v] - S[p]) // d
    length[v] = 0 if d == 0 else (S[v] - S[p]) // d

# À ce stade, toutes les arêtes sauf celles entre les centres ont été déterminées
# Pour l'instant, on suppose que la longueur des arêtes centrales vaut 0 et on effectue les calculs

# Calcul des distances de chaque sommet au centre choisi (root)
dist = [0] * (N+1)  # Initialisation : la distance du root à lui-même est 0

# Parcours de l'arbre en utilisant l'ordre DFS (sauf le root, déjà à 0)
for v in order[1:]:
    p = parent[v]               # Parent du sommet v
    dist[v] = dist[p] + length[v]  # Distance = distance au parent + longueur de l'arête

# Calcul de la somme des distances totales depuis la racine
d_root = sum(dist)

# Calcul de la longueur inconnue sur les arêtes centrales (là où length[v]==0)
# On double la différence entre S[root] et la somme des distances calculées, puis on divise par N
x = (S[root] - d_root) * 2 // N

# Préparer la liste des réponses (longueurs finales pour chaque arête)
answer = []
for v, p in zip(A, B):
    # Toujours avoir v comme l'indice enfant, p comme parent
    if parent[p] == v:
        v, p = p, v

    # Si la longueur sur cette arête n'est toujours pas connue (par construction elle ne peut qu'être 0 à ce stade)
    if length[v] == 0:
        length[v] = x  # On affecte cette longueur (x) aux arêtes centrales

    # On ajoute la longueur finale au tableau des réponses
    answer.append(length[v])

# On affiche toutes les longueurs des arêtes, une par ligne
print('\n'.join(map(str, answer)))  # Transformation de chaque élément de la liste en chaîne de caractères, puis affichage séparé par des sauts de ligne