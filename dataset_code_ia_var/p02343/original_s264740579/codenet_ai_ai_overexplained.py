# Définition d'une classe appelée UnionFind, qui permet de gérer des ensembles disjoints (Union-Find ou DSU)
class UnionFind:
    # Constructeur de la classe, appelé lors de la création d'un objet UnionFind
    def __init__(self, n):
        # Stocke le nombre total d'éléments gérés par la structure, typiquement de 1 à n inclus
        self.n = n
        # Crée une liste 'par' de taille n + 1 (pour les indices de 1 à n inclus)
        # Chaque élément dans 'par' représente le parent de l'élément à cet indice
        # Initialement, chaque valeur est -1, cela signifie que chaque élément est sa propre racine
        self.par = [-1] * (n + 1)
        # Crée une liste 'size' qui garde la taille de chaque arbre (ensemble)
        # Chaque composant ne contient au début qu'un seul élément, donc on remplit avec des 1
        self.size = [1] * (n + 1)

    # Méthode pour trouver la racine (représentant) de l'ensemble contenant l'élément idx
    # Implémente la compression de chemin pour accélérer les requêtes futures
    def root(self, idx):
        # Si l'élément idx n'a pas de parent (son parent vaut -1)
        # alors idx est la racine de son ensemble, on le retourne directement
        if self.par[idx] == -1:
            return idx

        # Si l'élément n'est pas une racine, on appelle root récursivement sur son parent
        # Afin de compresser le chemin, on assigne le parent de idx à la racine trouvée,
        # ce qui réduit la longueur des chemins à l'avenir lors des requêtes root
        self.par[idx] = self.root(self.par[idx])
        # On retourne alors la racine de idx
        return self.par[idx]

    # Méthode pour fusionner (unir) les ensembles qui contiennent idx1 et idx2
    def unite(self, idx1, idx2):
        # Trouve la racine de idx1, c'est important car seuls les représentants doivent être fusionnés
        idx1_par = self.root(idx1)
        # Trouve la racine de idx2
        idx2_par = self.root(idx2)

        # Si les deux éléments appartiennent déjà au même ensemble (même racine), il n'y a rien à faire
        if idx1_par == idx2_par:
            return

        # Pour garder les arbres le plus plats possible, on attache le plus petit arbre au plus grand
        # Ici, on choisit d'attacher l'arbre dont la racine a la plus petite taille
        if self.size[idx1_par] >= self.size[idx2_par]:
            # On ajoute la taille de l'arbre de idx2_par à celui de idx1_par
            self.size[idx1_par] += self.size[idx2_par]
            # On fait pointer la racine de idx2_par vers idx1_par, unifiant ainsi les deux ensembles
            self.par[idx2_par] = idx1_par
        else:
            # Cas symétrique : on attache l'arbre idx1_par à l'arbre idx2_par
            self.size[idx2_par] += self.size[idx1_par]
            self.par[idx1_par] = idx2_par

    # Méthode pour vérifier si deux éléments sont dans le même ensemble
    def same(self, idx1, idx2):
        # Si les deux éléments ont la même racine, alors ils sont dans le même ensemble
        return self.root(idx1) == self.root(idx2)

# Lecture de deux entiers (n nombre d'éléments, q nombre de requêtes) à partir de l'entrée standard
# map(int, input().split()) lit une ligne, sépare sur les espaces, convertit chaque morceau en int
n, q = map(int, input().split())

# Création d'une instance de UnionFind pour gérer n éléments
uf = UnionFind(n)

# Boucle pour traiter chacune des q requêtes en entrée
for i in range(q):
    # Lecture de 3 entiers : com, x, y
    # com détermine le type de requête (0 pour unir, 1 pour vérifier la connexion)
    com, x, y = map(int, input().split())
    # Si com vaut 0, on souhaite unir les ensembles de x et y
    if com == 0:  # unite
        uf.unite(x, y)
    else:  # same, c'est-à-dire, vérifier si x et y sont connectés (dans le même ensemble)
        # Si x et y sont dans le même ensemble (méthode same renvoie True)
        if uf.same(x, y):
            # On imprime 1 pour indiquer qu'ils sont connectés
            print(1)
        else:
            # Sinon, on imprime 0 pour indiquer qu'ils ne sont pas connectés
            print(0)