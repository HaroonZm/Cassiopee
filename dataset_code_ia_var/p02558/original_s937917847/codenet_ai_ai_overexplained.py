import sys  # Importe le module sys qui permet d'accéder à certaines variables et fonctions propres à l'interpréteur Python

# Redéfinit la fonction input pour qu'elle lise directement les lignes depuis l'entrée standard (stdin) en mode binaire (pour plus de rapidité qu'input())
input = sys.stdin.buffer.readline  # .buffer.readline lit les bytes, plus efficace que input() classique pour de nombreux cas en compétitions

class UnionFindTree:
    """
    Cette classe implémente la structure de donnée Union-Find (aussi appelée Disjoint-Set Forest ou arbre d'union-find), utilisée pour
    gérer dynamiquement la partition de n éléments en ensembles disjoints. Elle supporte efficacement deux opérations principales :
    - Trouver le représentant (racine) d'un ensemble contenant un élément (find)
    - Fusionner deux ensembles (unite)

    Complexité:
        - Initialisation: O(n)
        - find, unite, is_same: O(alpha(n)), où alpha est la fonction d'inverse d'Ackermann, qui croît très lentement
    """

    def __init__(self, n: int) -> None:
        """
        Constructeur de la structure de donnée Union-Find.

        n: nombre d'éléments de base (chaque élément démarre dans son propre ensemble)
        """
        # self.par[i] contient le parent immédiat de l'élément i dans l'arborescence de l'ensemble. Au début, chaque élément est son propre parent.
        self.par = list(range(n))  # Par convention, au départ, par[i] = i, donc chaque élément est sa propre racine.
        # self.rank[i] stocke une estimation (non nécessairement exacte) de la profondeur de l'ensemble dont i est la racine.
        # Ceci permet de fusionner de façon plus efficace lors de unite()
        self.rank = [0] * n  # Au début, tous les ensembles sont d'une seule feuille, donc rang = 0 pour chaque ensemble

    def find(self, x: int) -> int:
        """
        Trouve le représentant (racine) de l'ensemble contenant x.
        Applique la compression de chemin pour rendre les futurs appels plus rapides.
        """
        # Si le parent de x est x lui-même, x est la racine de son ensemble
        if self.par[x] == x:
            return x  # On retourne la racine immédiatement
        else:
            # Sinon, on applique la recherche récursive : le parent de x devient la racine de son ensemble
            self.par[x] = self.find(self.par[x])  # On mémorise la racine trouvée jusqu'à remonter complètement à la racine
            return self.par[x]  # On retourne la racine mise à jour

    def unite(self, x: int, y: int) -> None:
        """
        Fusionne les ensembles contenant x et y. Si x et y sont déjà dans le même ensemble, l'opération ne fait rien.
        Utilise l'union par rang pour limiter la profondeur des arbres et accélérer les futurs find().
        """
        # On trouve la racine de l'ensemble de x
        x = self.find(x)
        # On trouve la racine de l'ensemble de y
        y = self.find(y)
        # Si les deux racines sont identiques, c'est déjà le même ensemble : aucune fusion nécessaire
        if x == y:
            return
        # Sinon, on fusionne les deux ensembles
        # On attache toujours le plus petit arbre au plus haut rang (pour limiter la hauteur totale)
        if self.rank[x] < self.rank[y]:
            # l'arbre de x est plus petit, donc on rattache x à y
            self.par[x] = y
        else:
            # L'arbre de y est plus petit ou les deux ont la même hauteur, donc on rattache y à x
            self.par[y] = x
            # Si les deux arbres avaient exactement la même hauteur, la hauteur de la racine x augmente de 1
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1  # On incrémente le rang de la nouvelle racine

    def is_same(self, x: int, y: int) -> bool:
        """
        Détermine si x et y appartiennent au même ensemble ou non.
        Retourne True s'ils sont dans le même ensemble, False sinon.
        """
        # Ils sont dans le même ensemble si leurs racines sont égales
        return self.find(x) == self.find(y)

def main() -> None:
    """
    Point d'entrée du programme.
    Lit les données du problème, exécute les instructions union/find, et affiche les résultats attendus.
    """
    # On lit la première ligne (nombre d'éléments N et nombre de requêtes Q)
    N, Q = map(int, input().split())
    # On crée une instance de l'union-find avec N éléments
    uft = UnionFindTree(N)
    # On lit et traite chacune des Q requêtes
    for _ in range(Q):
        # On lit trois entiers : t, u, v
        t, u, v = map(int, input().split())
        # Si t vaut 0, on doit fusionner l'ensemble contenant u et celui contenant v
        if t == 0:
            uft.unite(u, v)
        else:
            # Sinon (t == 1), on doit vérifier si u et v sont dans le même ensemble, et afficher 1 (oui) ou 0 (non)
            print(int(uft.is_same(u, v)))  # On convertit le booléen (True/False) en entier (1/0) pour l'afficher

# Ceci garantit que la fonction main() ne sera exécutée que si ce script est exécuté comme programme principal
if __name__ == "__main__":
    main()