# Demande à l'utilisateur d'entrer une ligne de texte via le clavier (stdin)
# Stocke cette ligne dans la variable `line`
line = input()

# La ligne saisie contient deux valeurs séparées par un espace : n et q
# La fonction `split()` sépare la ligne en deux éléments
# Puis `map(int, ...)` convertit chaque élément en entier
# Enfin, `list()` crée une liste avec ces deux entiers assignés respectivement à n et q
n, q = list(map(int, line.split()))

# Crée un dictionnaire vide `rel` pour stocker des relations (non utilisé dans le code)
rel = {}

# Boucle `for` qui va de 0 à n-1 pour initialiser chaque clé de `rel`
# Chaque clé prendra une liste vide pour stocker de potentiels voisins ou relations
for i in range(0, n):
    rel[i] = []

# Création d'une liste `parent` contenant les ancêtres/directeurs de chaque élément
# Initialement, chaque élément est son propre parent, donc parent[i] = i
parent = [i for i in range(0, n)]

# Création d'une liste `rank` initialisée à 0
# `rank[i]` sera utilisé pour suivre la "hauteur" de l'arbre lors des fusions pour le DSU
rank = [0] * n

# Création d'une liste `weight`, contenant 0 au départ pour chaque élément
# `weight[i]` sera utilisé pour stocker un poids relatif pour chaque élément
weight = [0] * n

# Définition de la fonction `find(x)`
# Cette fonction récupère le représentant racine de l'arbre/disjoint set auquel x appartient
# Elle utilise la compression de chemin pour accélérer les requêtes suivantes
def find(x):
    # Si l'élément est son propre parent, on retourne x
    if parent[x] == x:
        return x
    else:
        # Sinon, on continue à chercher le représentant racine récursivement pour parent[x]
        y = find(parent[x])
        # On met à jour le poids de x en additionnant celui de son parent
        weight[x] += weight[parent[x]]
        # On actualise le parent de x en pointant directement à la racine trouvée `y`
        parent[x] = y
        # On retourne la racine finale
        return y

# Définition de la fonction `union(x, y, w)`
# Cette fonction fusionne les ensembles de x et y tout en maintenant l’information de poids
def union(x, y, w):
    # Calcule les représentants racines de x et y
    rx = find(x)
    ry = find(y)
    # Si le rang de rx est inférieur à celui de ry,
    # alors rx devient enfant de ry
    if rank[rx] < rank[ry]:
        parent[rx] = ry
        # Mise à jour du poids de rx
        # w est le poids relatif entre x et y, weight[x] et weight[y] sont relatifs à leurs racines respectives
        weight[rx] = w - weight[x] + weight[y]
    else:
        # Sinon, ry devient enfant de rx
        parent[ry] = rx
        # Mise à jour du poids de ry
        weight[ry] = - w - weight[y] + weight[x]
        # Si les rangs étaient égaux au départ, on augmente le rang de la nouvelle racine
        if rank[rx] == rank[ry]:
            rank[rx] += 1

# Fonction `same(x, y)` qui retourne True si x et y appartiennent au même ensemble
def same(x, y):
    # Compare les représentants racines de x et de y
    return find(x) == find(y)

# Fonction `diff(x, y)` qui retourne la différence de poids entre x et y
def diff(x, y):
    # La différence c'est le poids de x moins celui de y
    return weight[x] - weight[y]

# Boucle principale pour traiter `q` requêtes
for _ in range(0, q):
    # Lit la ligne de l'utilisateur contenant la requête encodée (0/1 suivi des entiers)
    line = input()
    # Transforme chaque élément de la requête en int
    query = list(map(int, line.split()))
    # Si la première valeur est 0, cela indique une requête de fusion (union)
    if query[0] == 0:
        # x : premier élément à fusionner; y : second élément; z : poids entre eux
        x, y, z = query[1:]
        # Appelle la fonction d'union avec ces paramètres
        union(x, y, z)
    # Si la requête commence par 1, il s'agit d'une interrogation sur la différence
    elif query[0] == 1:
        # Récupère les deux indices à comparer
        x, y = query[1:]
        # Si x et y sont dans le même ensemble, on affiche la différence
        if same(x, y):
            print(diff(x, y))
        # Sinon on affiche l'inconnue "?"
        else:
            print("?")