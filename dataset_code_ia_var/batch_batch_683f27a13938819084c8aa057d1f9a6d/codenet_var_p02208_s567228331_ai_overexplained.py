from collections import deque  # Importation de deque depuis la librairie collections qui permet de manipuler efficacement des files double-entrée

# Lecture de 7 entiers depuis l'entrée standard (généralement le clavier), séparés par des espaces
# La fonction input() lit toute la ligne sous forme de chaîne de caractères
# La méthode split() découpe cette chaîne de caractères là où il y a des espaces, produisant une liste de chaînes de caractères
# La fonction map(int, ...) convertit chaque élément de cette liste de chaînes en entier
# Les variables x, y, z, n, m, s, t reçoivent respectivement les valeurs ainsi lues
x, y, z, n, m, s, t = map(int, input().split())

# Création d'une liste 'g' de listes vides, une pour chaque sommet du graphe
# La taille totale du graphe (donc le nombre de sommets) est la somme de x, y et z
# L'opération [[] for _ in range(x+y+z)] crée une liste contenant x + y + z sous-listes, toutes initialement vides
g = [[] for _ in range(x + y + z)]

# Boucle sur les n arêtes du premier type (selon l'indice i de 0 à n-1)
for i in range(n):
    # Lecture de deux entiers, a et b, qui représentent un couple de sommets reliés par une arête
    a, b = map(int, input().split())
    # Ajout de l'arête dans le graphe sous forme de listes d'adjacence
    # Les indices doivent être ajustés car la numérotation des sommets dans l'entrée commence à 1
    # On soustrait 1 pour que les indices commencent à 0 dans la liste Python
    # a-1 représente donc le sommet dans le premier groupe (taille x)
    # b+x-1 ajuste b pour pointer vers le deuxième groupe (taille y) placé juste après le premier
    g[a - 1].append(b + x - 1)  # Ajoute b comme voisin de a
    g[b + x - 1].append(a - 1)  # Ajoute a comme voisin de b dans l'autre sens pour la symétrie (non oriente)

    # Si on est à la s-ième itération (s-1 parce que Python commence à 0), on se souvient des deux sommets de cette arête
    if i == s - 1:
        p, q = a - 1, b + x - 1  # On note les indices des deux sommets de cette arête spéciale

# Boucle sur les m arêtes du deuxième type (indice j de 0 à m-1)
for j in range(m):
    # Lecture de deux entiers, a et b, représentant un couple de sommets connectés
    a, b = map(int, input().split())
    # Cette fois, les indices sont ajustés différemment pour viser le second et le troisième groupe de sommets
    # a+x-1 positionne le sommet a dans le deuxième groupe (taille y décalée après x)
    # b+x+y-1 positionne le sommet b dans le troisième groupe (taille z décalée après x + y)
    g[a + x - 1].append(b + x + y - 1)  # Ajoute b comme voisin de a
    g[b + x + y - 1].append(a + x - 1)  # Ajoute a comme voisin de b (graphe non orienté)

    # Si on est à la t-ième itération (t-1, base 0), on se souvient de ces indices pour utilisation ultérieure
    if j == t - 1:
        u, v = a + x - 1, b + x + y - 1  # On note les indices de cette arête particulière

# Création d'une liste 'd' qui va servir à stocker la distance minimale depuis les deux sommets de l'arête repérée par s
# On initialise toutes les distances à -2, une valeur dite 'sentinelle' qui signifiera "non encore visitée"
d = [-2] * (x + y + z)

# Les deux sommets associés à l'arête s (p et q) sont les points de départ, on considère leurs distances comme 0 (origine)
d[p], d[q] = 0, 0

# On prépare une file double (deque), initialisée avec les deux points de départ (p et q)
# Cela permettra de faire un parcours en largeur (BFS) simultané depuis ces deux sommets
q = deque([p, q])

# Boucle principale du BFS ; elle continue tant que la file n'est pas vide
while q:
    # Retirer (et obtenir) le sommet placé en premier dans la file (FIFO : First In First Out)
    p = q.popleft()
    # Parcourir chacun des voisins du sommet p (on les trouve dans la liste d'adjacence g[p])
    for node in g[p]:
        # Si ce voisin n'a pas déjà été visité (on le sait car sa distance est -2)
        if d[node] == -2:
            # On place ce voisin à la fin de la file pour traiter ses voisins ultérieurement
            q.append(node)
            # On lui attribue une distance qui est celle de p augmentée de 1 (on vient juste de l'atteindre)
            d[node] = d[p] + 1

# À la fin du parcours, d[u] et d[v] contiennent la distance minimale pour atteindre chacun des deux sommets de l'arête repérée par t, depuis l'un ou l'autre des deux sommets de l'arête repérée par s
# On prend le minimum entre d[u] et d[v], car l'objectif est d'aller d'un des sommets d'origine à l'un des sommets de destination
# On ajoute 1 pour compter le passage final sur l'arête t elle-même (puisque la distance stockée ne compte pas encore ce passage)
print(min(d[u], d[v]) + 1)