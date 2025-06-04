class UnionFind:
    # Le constructeur de la classe UnionFind initialise un ensemble d'éléments et leurs parents
    def __init__(self, N):
        # N est le nombre d'éléments dans l'ensemble (doit être un entier positif)
        self.N = N
        # La liste 'parent' contient l'index du parent de chaque élément.
        # Initialement, chaque élément est son propre parent, ce qui signifie que chaque élément forme un ensemble singleton.
        self.parent = list(range(N))

    # Cette fonction trouve le représentant (racine) de l'ensemble auquel appartient l'élément x
    def root(self, x):
        # path_to_root stocke les noeuds rencontrés en remontant jusqu'à la racine.
        path_to_root = []
        # Tant que l'élément x n'est pas son propre parent, cela signifie qu'il n'est pas la racine.
        # On continue donc à remonter l'arbre en allant de parent en parent.
        while self.parent[x] != x:
            # Ajoute x à la liste pour se souvenir du chemin parcouru
            path_to_root.append(x)
            # Met à jour x pour qu'il devienne son parent.
            x = self.parent[x]
        # A ce stade, x est la racine de l'ensemble d'origine.
        # On applique la compression de chemin (path compression) :
        # tous les éléments rencontrés dans le chemin voient leur parent devenir directement la racine,
        # ce qui accélère les requêtes futures.
        for node in path_to_root:
            self.parent[node] = x  # Compression du chemin
        # On retourne la racine trouvée
        return x

    # La fonction same détermine si deux éléments x et y appartiennent au même ensemble
    def same(self, x, y):
        # Si les racines des deux éléments sont égales, ils sont dans le même ensemble
        return self.root(x) == self.root(y)

    # La fonction unite fusionne l'ensemble contenant x avec l'ensemble contenant y
    def unite(self, x, y):
        # Trouve la racine de x
        root_x = self.root(x)
        # Trouve la racine de y
        root_y = self.root(y)
        # Relie la racine de x à la racine de y
        # Cela fait que tous les éléments qui avaient root_x comme racine sont maintenant rattachés à root_y
        self.parent[root_x] = root_y

    # La fonction __str__ permet d'afficher l'état actuel des ensembles connectés de la structure UnionFind
    def __str__(self):
        # Un dictionnaire pour stocker les groupes d'éléments par racine
        groups = {}
        # On examine chaque élément de 0 à N-1
        for x in range(self.N):
            # On trouve la racine de l'élément courant
            root = self.root(x)
            # Si ce root existe déjà comme clé du dictionnaire, on y ajoute l'élément x
            if root in groups.keys():
                groups[root].append(x)
            # Sinon, on crée une nouvelle clé et on commence la liste d'ensemble
            else:
                groups[root] = [x]
        # On prépare une chaîne pour construire la représentation textuelle de tous les groupes
        result = ""
        # Pour chaque racine, on affiche la liste des éléments appartenant au même ensemble
        for root in groups.keys():
            result += str(groups[root]) + "\n"
        # On retourne la représentation complète
        return result

# Lecture du nombre d'éléments n et du nombre de requêtes q depuis l'entrée standard
# La fonction input() retourne une chaîne, split() la divise en morceaux, map(int,...) convertit chaque morceau en entier
# n est le nombre d'éléments uniques gérés par UnionFind, q est le nombre de requêtes à traiter
n, q = map(int, input().split())
# Création d'une nouvelle instance de la classe UnionFind avec n éléments
u = UnionFind(n)
# Pour chaque requête (il y en a q au total), on lit les valeurs de la requête et on traite en conséquence
for i in range(q):
    # On lit une requête sous la forme de trois entiers : com, x, y
    # com détermine le type de requête : 0 pour l'union, 1 pour la vérification
    com, x, y = map(int, input().split())
    # Si com vaut 0, il s'agit d'unir les ensembles de x et y
    if com == 0:
        # On unit les ensembles contenant x et y
        u.unite(x, y)
    # Sinon, si com n'est pas 0 (c'est-à-dire 1), on vérifie si x et y sont dans le même ensemble
    else:
        # On vérifie si x et y sont dans le même ensemble
        if u.same(x, y):
            # Si oui, on affiche 1 pour indiquer qu'ils sont connectés
            print(1)
        else:
            # Sinon, on affiche 0 pour indiquer qu'ils ne sont pas connectés
            print(0)