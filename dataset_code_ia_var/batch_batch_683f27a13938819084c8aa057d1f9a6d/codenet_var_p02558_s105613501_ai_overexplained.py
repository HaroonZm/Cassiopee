import sys  # On importe le module sys, qui contient des fonctions et objets permettant d’interagir avec l’interpréteur Python.

# On définit trois variables pour lire les données depuis l'entrée standard.
read = sys.stdin.buffer.read      # 'read' permettra de lire toute l'entrée standard en une seule fois sous forme de bytes.
readline = sys.stdin.buffer.readline  # 'readline' permettra de lire une seule ligne de l'entrée standard à chaque appel, sous forme de bytes.
readlines = sys.stdin.buffer.readlines  # 'readlines' permettra de lire toutes les lignes de l'entrée standard comme une liste de bytes.

# Définition de la classe DisjointSetUnion, également appelée Union-Find.
class DisjointSetUnion:
    def __init__(self, n):
        # Cette méthode spéciale '__init__' est le constructeur de l'objet. Elle est appelée lors de la création d'une instance de la classe.
        self.n = n  # On stocke le nombre d'éléments (taille de l'ensemble) dans l'attribut 'n'.
        # 'par' (pour parent) est une liste représentant le parent de chaque élément.
        # Si par[x] == -1, cela signifie que x est la racine de son ensemble.
        self.par = [-1] * n  # On initialise chaque élément comme sa propre racine au début en mettant tous les parents à -1.
        # 'rank' est une liste qui aide à optimiser l'union des ensembles.
        # Cela permet de garder l'arbre de représentation aussi plat que possible en unissant les ensembles de "petit" rang sous ceux de "grand" rang.
        self.rank = [0] * n  # Au départ, le rang (la "hauteur" de l'ensemble) de chaque ensemble est 0.

    def root(self, x):
        # Cette méthode retourne la racine de l'ensemble auquel appartient l'élément 'x'.
        # Si x est la racine, on le retourne directement.
        if self.par[x] == -1:
            return x  # x est la racine de son ensemble.
        else:
            # Sinon, on applique la compression de chemin (path compression).
            # Cela signifie qu'on raccourcit le chemin de x vers la racine en mettant directement le parent de x à la racine de son ensemble.
            self.par[x] = self.root(self.par[x])  # Appel récursif pour trouver la racine puis mettre à jour par[x].
            return self.par[x]  # On retourne le nouveau parent, qui est la racine.

    def same(self, x, y):
        # Cette méthode vérifie si deux éléments 'x' et 'y' sont dans le même ensemble.
        # Elle le fait en comparant leurs racines.
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        # Cette méthode fusionne les ensembles contenant les éléments 'x' et 'y'.
        # On commence par trouver la racine de x et la racine de y (au cas où x et y ne sont pas eux-mêmes racines).
        x = self.root(x)
        y = self.root(y)
        # Si les racines sont les mêmes, cela signifie que x et y sont déjà dans le même ensemble, donc il n'y a rien à faire.
        if x == y:
            return
        # Pour garder l'arbre aussi plat que possible, on unit l'ensemble de plus petit rang sous l'ensemble de plus grand rang.
        if self.rank[x] < self.rank[y]:
            # On échange les rôles si le rang de x est inférieur à celui de y.
            x, y = y, x
        # Si les deux ensembles ont le même rang, on doit augmenter le rang du nouvel ensemble fusionné.
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1  # On augmente le rang.
        # On met à jour le parent de l'ensemble dont la racine est y pour qu'il pointe vers la racine x.
        self.par[y] = x
        return  # La méthode ne retourne rien.

# Cette condition spéciale vérifie si ce fichier est exécuté directement en tant que script principal.
if __name__ == '__main__':
    # On lit la première ligne de l'entrée standard (stdin) pour obtenir deux entiers n et q.
    # n est le nombre d'éléments du DSU, q est le nombre de requêtes.
    n, q = map(int, readline().split())
    # On crée une instance de DisjointSetUnion avec n éléments.
    dsu = DisjointSetUnion(n)

    # On exécute une boucle q fois, une pour chaque requête.
    for i in range(q):
        # À chaque itération, on lit la prochaine ligne de l'entrée standard,
        # on la découpe en chaines de caractères, on les convertit en entiers,
        # et on les assigne à t, u, et v.
        t, u, v = map(int, readline().split())
        # Si t vaut 1, il s'agit d'une opération de vérification (same), sinon d'une union.
        if t:
            # On affiche 1 si u et v sont dans le même ensemble, sinon 0.
            print(int(dsu.same(u, v)))
        else:
            # On fusionne les ensembles contenant u et v.
            dsu.unite(u, v)