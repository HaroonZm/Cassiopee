import collections  # On importe le module 'collections' pour utiliser deque, une file efficace pour la manipulation d'éléments en FIFO.

# On lit un entier depuis l'entrée standard, qui représente le nombre de sommets (noeuds) dans le graphe.
n = int(input().rstrip())  # On utilise .rstrip() pour enlever les éventuels espaces ou sauts de ligne à la fin de l'entrée.

# On crée une liste de listes (appelée 'g') pour stocker la liste d'adjacence du graphe.
# Cela permettra de représenter chaque sommet et les sommets auxquels il est connecté.
# g[i] contiendra une liste de tous les voisins du sommet i.
g = [[] for i in range(n)]

# On crée une liste 'deg' pour stocker le degré (nombre de connexions) de chaque sommet.
# Initialement, on met toutes les valeurs à 0.
deg = [0 for i in range(n)]

# On lit les arêtes (connexions entre sommets) du graphe.
# Il y a exactement n arêtes à lire.
for i in range(n):
    # On lit une ligne, on la découpe en deux nombres, puis on soustrait 1 à chacun (car l'indice commence à 0).
    u, v = map(lambda x: x-1, map(int, input().rstrip().split(' ')))
    # On ajoute chaque sommet à la liste d'adjacence de l'autre, car le graphe est non orienté.
    g[u].append(v)
    g[v].append(u)
    # On incrémente le degré de chaque sommet impliqué dans cette arête.
    deg[u] += 1
    deg[v] += 1

# On crée une deque (double-ended queue) qui servira à contenir les feuilles du graphe à traiter.
q = collections.deque()

# Pour chaque sommet, on vérifie si son degré est 1 (c'est donc une feuille ; un noeud avec une seule connexion).
# On ajoute alors cet indice à la deque 'q'.
for i in range(n):
    if deg[i] == 1:
        q.append(i)

# On crée une liste booléenne 'isPushed' de taille n, initialisée avec des False.
# Cette liste va servir à marquer quels sommets ont été "poussés" (i.e. retirés en tant que feuille).
isPushed = [False for i in range(n)]

# On utilise une boucle while pour effectuer une forme d'élagage de feuilles dans le graphe.
# Tant qu'il y a des éléments (noeuds feuilles) dans la deque q, on continue l'élagage.
while len(q) > 0:
    # On retire le sommet v situé en tête de la file (le plus ancienlement ajouté).
    v = q.popleft()
    # On marque v comme ayant été "poussé".
    isPushed[v] = True
    # Pour chaque voisin nv (noeud voisin) de v :
    for nv in g[v]:
        # On diminue le degré de ce voisin, car v a été retiré.
        deg[nv] -= 1
        # Si ce voisin devient une feuille (degré == 1) après avoir diminué, on l'ajoute à la deque pour traitement futur.
        if deg[nv] == 1:
            q.append(nv)

# On lit un entier depuis l'entrée standard qui représente le nombre de requêtes à traiter.
q = int(input().rstrip())

# Pour chaque requête :
for _ in range(q):
    # On lit deux entiers a et b, qui représentent les indices des sommets pour lesquels il faut répondre à la requête.
    # On soustrait 1 pour obtenir des indices basés sur 0 (convention Python).
    a, b = map(lambda x: x-1, map(int, input().rstrip().split(' ')))
    # On teste si l'un des deux sommets a été "poussé" (c'est-à-dire envoyé dans le processus d'élagage des feuilles).
    # Cela vérifie si a ou b ont été coupés petit à petit du centre (fait partie d'une branche élaguée).
    if isPushed[a] or isPushed[b]:
        # Si l'un des deux sommets est une feuille (ou est devenu feuille après l'élagage), on affiche 1.
        print(1)
    else:
        # Sinon, les deux sont au coeur du graphe, on affiche 2.
        print(2)