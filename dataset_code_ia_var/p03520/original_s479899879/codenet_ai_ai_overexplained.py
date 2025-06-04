import sys  # Importe le module système, utilisé pour modifier des paramètres du système comme la limite de récursion

# Augmente la limite de récursion maximale autorisée pour éviter les erreurs de récursion sur de grands graphes/arborescences
sys.setrecursionlimit(10**8)

# Lit un entier N depuis l'entrée standard, c'est le nombre de nœuds dans le graphe/arbre
N = int(input())

# Crée une liste de listes 'G', où chaque sous-liste représente les arêtes connectées à un nœud particulier :
# - G[i] sera la liste des (voisin, numéro_de_l_arête) pour le sommet i
G = [[] for i in range(N)]

# Initialise une liste vide 'E' qui servira à stocker des informations sur les arêtes pour un traitement ultérieur
E = []

# Initialise un tableau 'ans' de taille N-1 rempli de zéros, qui contiendra les résultats finaux pour chaque arête
ans = [0] * (N - 1)

# Pour chaque arête (il y a N-1 arêtes dans un arbre à N nœuds)
for i in range(N - 1):
    # Lit deux entiers a et b, les extrémités de l'arête (numérotées à partir de 1)
    a, b = map(int, input().split())
    # Ajoute (b-1, i) à la liste des voisins de a-1 (convertit en indice 0-based)
    G[a - 1].append((b - 1, i))
    # Ajoute (a-1, i) à la liste des voisins de b-1 (graphe non orienté)
    G[b - 1].append((a - 1, i))

# Lit une liste d'entiers séparés par des espaces et la convertit en liste d'entiers 's'
# Par exemple, si l'entrée est "5 3 7", alors s = [5, 3, 7]
s = [int(i) for i in input().split()]

# Initialise une liste 'n' de taille N avec des zéros, pour stocker la taille des sous-arbres de chaque nœud après DFS
n = [0] * N

# Initialise une liste 'visited' de taille N remplie de False pour savoir si un nœud a été visité ou non lors de DFS
visited = [False] * N

# Définit une fonction pour calculer la taille du sous-arbre enraciné en x,
# et pour marquer les arêtes traversées pendant la DFS
def size(x):
    # Initialise la taille du sous-arbre courant à 1 (compte le nœud x lui-même)
    res = 1
    # Marque le nœud x comme visité pour éviter de revisiter dans la DFS
    visited[x] = True
    # Parcourt toutes les arêtes connectées à x
    for i, e in G[x]:
        # Si le voisin i de x a déjà été visité, continue sans rien faire
        if visited[i]:
            continue
        # Ajoute à res la taille du sous-arbre enraciné en i (appel récursif)
        res += size(i)
        # Ajoute aux arêtes E l'information sur l'arête 'e' allant de x à i
        E.append((e, x, i))
    # Après avoir visité tous les enfants, assigne la taille de ce sous-arbre à n[x]
    n[x] = res
    # Retourne la taille finale de ce sous-arbre
    return res

# Lance la fonction size à partir du nœud 0 (supposé racine)
size(0)

# Définit une variable 'flag' initialisée à 0, qui va servir à repérer le cas particulier (voir plus bas)
flag = 0

# Trie la liste des arêtes E par le numéro de l'arête, pour garantir l'ordre
E.sort()

# Parcourt chaque arête (index de 0 à N-2)
for i in range(N - 1):
    # Décompose le tuple en (numéro_de_l_arête, sommet_a, sommet_b)
    e, a, b = E[i]
    # Si la taille du sous-arbre b vaut pile la moitié de l'arbre (cas d'arête dominante, coupe l'arbre en deux parts égales)
    if 2 * n[b] == N:
        # Stocke ce numéro d'arête+1 dans 'flag' (sert d'indicateur)
        flag = e + 1
        # Passe à l'arête suivante
        continue
    # Sinon, calcule la valeur pour ans[e] liée à la différence s[a] - s[b]
    # (Opération entière, assurez-vous qu'il n'y aura pas de division par zéro)
    ans[e] = abs((s[a] - s[b]) // (2 * n[b] - N))

# Si 'flag' n'est pas nul, on dispose d'une arête qui coupe l'arbre équitablement,
# il faut traiter ce cas particulier pour rétablir l'équilibre de la solution :
if flag:
    # Prend la valeur de s[0] (racine)
    A = s[0]
    # Pour chaque arête, on retire la contribution du sous-arbre correspondant à l'arête
    for i in range(N - 1):
        # E[i][2] est le sommet b du tuple (e, a, b)
        A -= n[E[i][2]] * ans[i]
    # En déduit la valeur manquante pour cette arête spéciale (flag-1 = indice réel)
    ans[flag - 1] = A // n[E[flag - 1][2]]

# Pour chaque arête, affiche le résultat calculé
for i in range(N - 1):
    print(ans[i])  # Affiche le résultat à la ligne (fonctionne sur toutes les plateformes Python)