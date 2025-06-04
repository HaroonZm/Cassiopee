# Importation du module permutations depuis le module standard itertools.
# 'permutations' permet de générer toutes les façons d'ordonner une séquence.
from itertools import permutations

# Prise de deux entiers en entrée séparés par un espace : N (taille) et M (nombre de coups).
# input() récupère une ligne, split() sépare en morceaux, map(int,...) convertit en entiers.
N, M = map(int, input().split())

# Lecture de M entiers. Pour chaque entrée, on lit un entier, on enlève 1 car on veut un indice basé sur 0.
# On stocke chaque valeur ajustée dans la liste k.
k = [int(input()) - 1 for i in range(M)]

# Génération d'une liste g contenant toutes les valeurs de 0 à N-1. 
# Ceci sert de représentation initiale (par exemple, g=[0,1,2,3] si N=4).
g = [i for i in range(N)]

# On va "simuler" les opérations indiquées par chaque valeur de la liste k sur la liste g.
# Pour chaque position i de la liste (de 0 à N-1):
for i in range(N):
    # Pour chaque index j dans la liste k (qui sont les positions où l'on applique un échange):
    for j in k:
        # Si la valeur actuelle g[i] est exactement à l'indice 'j':
        if g[i] == j:
            # On échange g[i] avec g[i+1] en effet : donc on l'incrémente de 1.
            g[i] = j + 1
        # Si la valeur courante g[i] est juste après (égale à j+1):
        elif g[i] == j + 1:
            # On l'échange avec g[i-1], donc décrémente de 1.
            g[i] = j

# Initialisation d'une variable 's' à 10.
# Cette variable gardera la valeur minimale trouvée ultérieurement.
s = 10

# Pour chaque permutation possible de la liste des indices k :
for K in permutations(k):
    # On recommence avec une nouvelle liste G similaire à [0, 1, ..., N-1]
    G = [i for i in range(N)]
    # Pour chaque indice de la liste
    for i in range(N):
        # Pour chaque opération (indice j) dans l'ordre donné par la permutation K :
        for j in K:
            # Même logique d'échange qu'avant
            if G[i] == j:
                G[i] = j + 1
            elif G[i] == j + 1:
                G[i] = j
    # On vérifie si ce résultat G correspond à g obtenu au début.
    # Si ce n'est pas le cas, on ignore cette permutation.
    if G != g:
        continue

    # On crée une liste l de taille N remplie de zéros : cela sert à compter des niveaux ou des coups attribués.
    l = [0] * N
    # Pour chacune des M opérations dans l'ordre de la permutation courante:
    for i in range(M):
        a = K[i]      # Prend la position d'échange actuelle
        # On cherche le maximum déjà attribué à ces deux positions.
        b = max(l[a], l[a + 1])
        # On attribue b+1 à chacune des positions échangées
        l[a] = b + 1
        l[a + 1] = b + 1
    # On compare la valeur maximale attribuée à s et on conserve le minimum
    s = min(s, max(l))

# Enfin, on affiche la plus petite valeur trouvée pour s.
print(s)