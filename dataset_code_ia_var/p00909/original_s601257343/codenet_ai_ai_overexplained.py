# Auteur : cr4zjh0bp
# Créé le : Vendredi 20 Mars 2020 22:48:43 UTC

# On importe le module sys pour avoir accès à des objets et fonctions liés au système d'exécution du programme Python.
import sys

# On définit un alias 'stdin' qui fait référence à sys.stdin. Cela représente le flux d'entrée standard du programme (typiquement, clavier ou pipe).
stdin = sys.stdin

# On définit une très grande valeur entière en réalisant un décalage binaire. Cela sera éventuellement utilisé comme "infini".
inf = 1 << 60  # 1 décalé vers la gauche de 60 bits, ce qui fait un nombre extrêmement grand.

# On définit un nombre premier grand, appelé couramment "modulo", utilisé pour des calculs de reste de divisions dans beaucoup de problèmes d’algorithmique.
mod = 1000000007  # 10^9 + 7

# On crée des fonctions ou lambdas pour faciliter et condenser la lecture des entrées, avec différents formats :
# Récupérer un int à partir d'une ligne d'entrée
ni = lambda: int(ns())
# Lire y entiers sous forme de liste (1 entier par ligne)
nin = lambda y: [ni() for _ in range(y)]
# Lire une seule ligne constituée de plusieurs entiers, et les mettre dans une liste
na = lambda: list(map(int, stdin.readline().split()))
# Lire y lignes, où chaque ligne est une liste d'entiers (plusieurs entiers par ligne)
nan = lambda y: [na() for _ in range(y)]
# Lire un float sur une ligne
nf = lambda: float(ns())
# Lire y flottants (1 par ligne)
nfn = lambda y: [nf() for _ in range(y)]
# Lire une ligne composée de plusieurs flottants
nfa = lambda: list(map(float, stdin.readline().split()))
# Lire y lignes, où chaque ligne est une liste de flottants
nfan = lambda y: [nfa() for _ in range(y)]
# Lire une ligne sous forme de chaîne (sans le retour à la ligne)
ns = lambda: stdin.readline().rstrip()
# Lire y chaînes (1 par ligne)
nsn = lambda y: [ns() for _ in range(y)]
# Lire y lignes, transformer chaque ligne en liste de caractères
ncl = lambda y: [list(ns()) for _ in range(y)]
# Lire une ligne découpée en liste de chaînes (par défaut, split() sépare sur les espaces)
nas = lambda: stdin.readline().split()

# Définition d'une classe : structure Union-Find (avec poids/différences relatives, "Weighted Union-Find")
class WUnionFind:
    # Méthode d'initialisation de la classe, appelée lors de la création d'un nouvel objet.
    def __init__(self, n, sum_unity=0):
        # n : nombre d’éléments totaux
        # sum_unity : valeur initiale du poids (par défaut 0)
        self.n = n  # on stocke le nombre d’éléments
        # self.par est une liste où chaque case i contient le parent de i dans la forêt, initialement chaque élément est son propre parent
        self.par = [i for i in range(n)]
        # self.rank sert à optimiser la fusion (union) en choisissant la racine la "plus profonde"
        self.rank = [0 for _ in range(n)]
        # self.diff_weight sauvegarde la différence de poids entre le noeud i et son parent direct
        self.diff_weight = [sum_unity for _ in range(n)]
        # self._size sert à connaître la taille de chaque composante/tree, initialement chaque ensemble a 1 élément
        self._size = [1 for _ in range(n)]
        # self._edges compte le nombre d’arêtes/unions réalisées (pour calculer par exemple le nombre de composantes)
        self._edges = 0

    # Méthode pour trouver la racine ("root") de l’élément x, avec compression de chemin pour accélérer les futures recherches
    def find(self, x):
        # Si x est son propre parent, on a trouvé la racine
        if self.par[x] == x:
            return x
        else:
            # Sinon, on cherche récursivement le parent de x
            r = self.find(self.par[x])
            # On met à jour la différence de poids lors du passage vers le haut, pour que le poids absolu de chaque nœud soit correct
            self.diff_weight[x] += self.diff_weight[self.par[x]]
            # Compression de chemin : désormais, le parent direct de x sera la racine trouvée
            self.par[x] = r
            return r
    
    # Méthode pour fusionner les ensembles contenant x et y, en fixant la différence de poids entre eux à w
    def unite(self, x, y, w):
        # On ajuste w de façon à tenir compte des poids relatifs de x et y
        w += self.weight(x)
        w -= self.weight(y)
        # On trouve les racines de x et de y après ajustement
        x = self.find(x)
        y = self.find(y)
        # Si les racines sont déjà les mêmes, ils sont déjà connectés, donc rien à faire
        if x == y:
            return
        # On vérifie les rangs pour garder un arbre équilibré (moins profond)
        if self.rank[x] < self.rank[y]:
            # On attache x comme enfant de y
            self.par[x] = y
            self.diff_weight[x] = -w
            self._size[y] += self._size[x]  # on augmente la taille du composant de y
            self._edges += 1  # on a ajouté une arête
        else:
            # On attache y comme enfant de x
            self.par[y] = x
            self.diff_weight[y] = w
            # Si les deux arbres ont le même rang, on augmente le rang de la nouvelle racine
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self._size[x] += self._size[y]  # on augmente la taille d'arbre de x
            self._edges += 1  # nouvelle arête ajoutée

    # Méthode pour obtenir le poids relatif depuis un nœud x jusqu’à sa racine
    def weight(self, x):
        # On s'assure que le chemin est compressé et les poids mis à jour
        self.find(x)
        # Maintenant, le poids de x vis-à-vis de la racine est dans diff_weight[x]
        return self.diff_weight[x]

    # Retourne la différence de poids entre les nœuds y et x : c'est-à-dire poids(y) - poids(x)
    def diff(self, x, y):
        return self.weight(y) - self.weight(x)
    
    # Retourne la taille (nombre de noeuds) du composant/racine auquel appartient x
    def size(self, x):
        x = self.find(x)  # on remonte à la racine
        return self._size[x]

    # Retourne le nombre d'arbres (composantes connexes) restants dans la forêt d’ensembles disjoints
    def trees(self):
        return self.n - self._edges

    # Indique si x et y appartiennent au même ensemble (i.e., ont la même racine)
    def same(self, x, y):
        return self.find(x) == self.find(y)

# On démarre une boucle infinie permettant de traiter plusieurs cas d'entrée successivement
while True:
    # On lit deux entiers n et m de la même ligne : n = nombre de sommets, m = nombre de requêtes
    n, m = na()
    # Si à la fois n == 0 et m == 0, cela signifie que l’entrée est terminée, donc on sort de la boucle
    if n == 0 and m == 0:
        break
    # On crée un nouvel objet de la classe WUnionFind pour gérer n éléments sans poids initial
    wuf = WUnionFind(n)
    # On boucle pour traiter chacune des m opérations
    for i in range(m):
        # On lit la requête sous forme de liste de chaînes (chaque mot de la ligne)
        que = nas()
        # Si le premier mot est "!", il s'agit d'une requête pour ajouter une relation de poids entre deux éléments
        if que[0] == '!':
            # On lit a, b, w et on les convertit en entiers : a et b sont des indices (1-based dans l'entrée)
            a, b, w = list(map(int, que[1:]))
            a -= 1  # On convertit a en index 0-based pour Python
            b -= 1  # Idem pour b
            # On appelle la fonction unite pour lier a et b avec une différence de poids w
            wuf.unite(a, b, w)
        # Si le premier mot est "?", il s'agit d'une requête pour obtenir la différence de poids entre deux éléments
        elif que[0] == '?':
            # On lit a et b, deux indices à comparer, et on les convertit en indices 0-based
            a, b = list(map(int, que[1:]))
            a -= 1
            b -= 1
            # On vérifie d'abord si a et b sont connectés (même arbre)
            if wuf.same(a, b):
                # S’ils sont reliés, on affiche la différence de poids s’en allant de a à b
                print(wuf.diff(a, b))
            else:
                # Sinon, ils ne sont pas reliés, la différence est donc "UNKNOWN"
                print("UNKNOWN")