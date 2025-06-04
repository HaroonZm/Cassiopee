class UnionFind:
    def __init__(self, n):
        # Cette méthode __init__ est appelée lors de la création d’une instance de la classe.
        # Elle prend un argument n qui représente le nombre d’éléments distincts que comportera la structure.
        # self.par stocke pour chaque élément son "parent" dans le structure d’ensemble disjoint.
        # Initialement, chaque élément est son propre parent, formant n ensembles singletons.
        self.par = [i for i in range(n)]  # Création d'une liste du même taille que n, initialisée en [0, 1, ..., n-1]
        # self.rank sert d’heuristique pour équilibrer les arbres lors des fusions.
        # Chaque indice correspond au "rang" (profondeur approximative) de l’arbre dont l’élément est la racine.
        # Tous les rangs sont initialisés à 0, car tous les ensembles ont un seul élément géographiquement.
        self.rank = [0 for _ in range(n)]
    
    def find(self, x):
        # Cette méthode permet de trouver la "racine" de l’ensemble auquel x appartient.
        # Ceci est fondamental pour déterminer si deux éléments sont dans le même ensemble.
        # La comparaison self.par[x] == x vérifie si x est le parent de lui-même, 
        # donc s’il est la racine de son ensemble.
        if self.par[x] == x:
            # Si x est déjà la racine, alors on le retourne simplement.
            return x
        else:
            # Sinon, il faut remonter l’arbre pour trouver la racine réelle du groupe inclusif de x.
            # Pendant cette remontée, on applique la compression de chemin (path compression) :
            # on rattache x directement à la racine pour rendre les futurs accès plus rapides.
            self.par[x] = self.find(self.par[x])  # L’appel récursif continue jusqu’à atteindre la racine.
            return self.par[x]  # On retourne la racine trouvée.
    
    def unite(self, x, y):
        # Cette méthode fusionne les ensembles contenant x et y.
        # D’abord, il faut localiser les racines réelles des ensembles de x et y :
        x = self.find(x)
        y = self.find(y)
        # Si les deux racines sont identiques, cela signifie que x et y sont déjà dans le même ensemble :
        if x == y:
            # Rien à faire, ils sont déjà connectés.
            return
        # Sinon, il faut fusionner les deux ensembles.
        # On compare les rangs pour déterminer quel arbre ajouter sous l’autre (pour équilibrer la hauteur).
        if self.rank[x] < self.rank[y]:
            # On attache l’arbre de x sous l’arbre de y parce que le rang de x est strictement inférieur :
            self.par[x] = y
        else:
            # Sinon, on attache l’arbre de y sous celui de x (y compris si les rangs sont égaux).
            self.par[y] = x
            # Si les deux arbres avaient la même hauteur, on a augmenté celle de x de 1.
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
    
    def same(self, x, y):
        # Cette méthode retourne True si x et y appartiennent au même ensemble, False sinon.
        # Cela se fait en comparant les racines respectives des deux éléments.
        return self.find(x) == self.find(y)  # L’égalité des racines implique l’appartenance au même groupe.


def main():
    # Fonction principale exécutée par le programme.
    # On commence par lire deux entiers depuis l’entrée standard (typiquement le clavier).
    # N représente le nombre d’éléments que va gérer UnionFind,
    # Q le nombre de requêtes ou opérations à traiter.
    N, Q = map(int, input().split())  # Découpe l’entrée "N Q" en deux entiers.
    
    # On crée une instance de UnionFind pour gérer les N éléments.
    uni = UnionFind(N)
    # Cette boucle va s’exécuter Q fois, chaque itération traitant une requête/un ordre.
    for i in range(Q):
        # On lit chaque requête, qui est composée de 3 entiers : t, u et v.
        t, u, v = map(int, input().split())  # t indique le type d’opération, u et v sont des indices.
        if t == 0:
            # Si t vaut 0, on fusionne les ensembles contenant u et v.
            uni.unite(u, v)
        else:
            # Si t est différent de 0 (donc égal à 1), cela signifie qu’il faut tester 
            # si les éléments u et v sont dans le même ensemble.
            if uni.same(u, v):
                # Si c’est le cas, on affiche 1 (pour "oui").
                print(1)
            else:
                # Sinon, on affiche 0 pour "non".
                print(0)

# Ce qui suit exécute la fonction main si ce script est lancé.
main()