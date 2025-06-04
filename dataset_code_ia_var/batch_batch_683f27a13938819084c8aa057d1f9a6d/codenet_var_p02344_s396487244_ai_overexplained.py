import sys  # Le module sys permet d'accéder à certaines variables et fonctions propres à l'interpréteur Python

# Ici, readline est assignée à une fonction qui permet de lire efficacement une ligne issue de l'entrée standard (stdin)
# `.buffer` permet de lire les entrées au format binaire, utile pour des entrées rapides
readline = sys.stdin.buffer.readline

# On lit la première ligne et on la découpe en deux entiers : n (nombre d’éléments), q (nombre de requêtes)
n, q = map(int, readline().split())

# Définition de la classe WeightedUnionFind, qui gère une structure d’ensembles disjoints avec gestion de poids (ou différence potentielle)
class WeightedUnionFind:
    # Le constructeur de la classe
    def __init__(self, n):
        # Initialisation d'un tableau par où chaque indice représente un élément et la valeur associée désigne son parent.
        # Au début, chaque élément est son propre parent.
        self.par = [i for i in range(n + 1)]  # 0-inclusif, souvent indexé à partir de 1
        # Tableau des rangs, utilisé pour garder la profondeur des sous-arbres pour l’optimisation (union by rank).
        # On cherche à minimiser la profondeur des arbres générés.
        self.rank = [0] * (n + 1)
        # Tableau des poids, permettant de savoir la différence de coût entre l’élément et son parent (chemin jusqu'à la racine)
        self.weight = [0] * (n + 1)
    
    # La méthode find sert à trouver le représentant (racine) de la classe (ensemble) à laquelle appartient x
    def find(self, x):
        # Si x est le parent de lui-même, c’est la racine de l’arbre qui contient x
        if self.par[x] == x:
            return x  # La racine est trouvée, on la retourne
        else:
            # Appel récursif pour continuer à chercher la racine du parent de x
            y = self.find(self.par[x])  # Recherche de la racine du parent de x
            # Mise à jour du poids de x lors de la compression de chemin.
            # On ajoute le poids de son parent à son propre poids pour maintenir corrects les potentiels
            self.weight[x] += self.weight[self.par[x]]
            # Compression de chemin: maintenant, x pointe directement vers la racine
            self.par[x] = y
            return y  # On retourne la racine trouvée
    
    # La méthode union fusionne deux ensembles et ajuste les poids pour maintenir la différence potentielle entre x et y
    def union(self, x, y, w):
        # Trouver les racines des ensembles respectifs des éléments x et y
        rx = self.find(x)
        ry = self.find(y)
        # Si les deux éléments ne sont pas déjà dans le même ensemble, on fusionne
        # On regarde la hauteur (rank) des arbres pour que le moins haut devienne enfant du plus haut
        if self.rank[rx] < self.rank[ry]:
            # Si l’arbre x est moins profond que l’arbre y
            self.par[rx] = ry  # La racine de x pointe vers la racine de y
            # Mise à jour du poids pour garder la différence potentielle correcte
            # w est la différence de coût entre x et y donnée par la requête
            self.weight[rx] = w - self.weight[x] + self.weight[y]
        else:
            # Si l’arbre x est aussi haut ou plus haut que celui de y, on fait de y un enfant de x
            self.par[ry] = rx  # La racine de y pointe vers la racine de x
            # Mise à jour du poids du nouveau parent
            # On soustrait w et ajuste avec les poids pour que la différence entre x et y soit bien w
            self.weight[ry] = -w - self.weight[y] + self.weight[x]
            # Si les deux arbres avaient la même hauteur, le nouvel arbre est plus haut de 1
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1  # On augmente le rang (hauteur) de la nouvelle racine
    
    # La méthode same vérifie si deux éléments appartiennent au même ensemble
    def same(self, x, y):
        # Retourne True si x et y ont la même racine, donc sont dans le même ensemble
        return self.find(x) == self.find(y)
    
    # La méthode diff retourne la différence potentielle (coût) entre x et y, c’est-à-dire leur distance pondérée
    def diff(self, x, y):
        # La différence du potentiel de x à y
        return self.weight[x] - self.weight[y]

# Création d'une instance de la structure pour n éléments
uf = WeightedUnionFind(n)

# Traitement des q requêtes une par une
for i in range(q):
    # On lit une ligne de l'entrée, on retire le retour de ligne de la fin, puis on la décode d'UTF-8 (conversion binaire → str)
    s = readline().rstrip().decode('utf-8')
    # Si la première lettre du string (donc le premier caractère de la requête) est "0"
    if s[0] == "0":
        # Requête de type 0: c'est une opération d'union (fusion), on décompose la ligne en 4 entiers
        com, a, b, w = map(int, s.split())
    else:
        # Sinon, c’est une requête de type 1: on ne prend que 3 entiers (com, a, b)
        com, a, b = map(int, s.split())
    # Traitement selon le type de commande
    if com:
        # Si com vaut 1 (requête "différence de coût")
        if uf.same(a, b):
            # Si a et b sont dans le même ensemble (connectés)
            print(uf.diff(a, b))  # On affiche la différence entre a et b
        else:
            # Sinon, ils ne sont pas connectés, donc on ne peut pas répondre à la différence de coût
            print("?")
    else:
        # Si com vaut 0 (requête d'union avec pondération)
        uf.union(a, b, w)  # On fusionne a et b avec un coût de w