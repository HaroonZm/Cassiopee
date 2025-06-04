class SegmentTree:
    """
    SegmentTree permet d'accomplir des opérations de range-add
    (ajout d'une valeur à tous les éléments d'un intervalle)
    ainsi que des requêtes de récupération d'un élément à un index donné,
    le tout avec une complexité logarithmique.
    """

    def __init__(self, n):
        """
        Initialise un arbre de segment pour "n" éléments.
        L'arbre utilise une représentation sous forme de tableau pour optimiser l'accès.

        Args:
            n (int): Nombre d'éléments initiaux.
        """
        # Longueur minimale de l'arbre, puissance de 2 >= n
        self.seg_len = 1
        while self.seg_len < n:
            self.seg_len <<= 1
        # Les noeuds de l'arbre, taille 2*seg_len pour représenter l'arbre complet
        self.node = [0 for _ in range(self.seg_len * 2)]

    def add(self, l, r, x):
        """
        Ajoute la valeur 'x' à chaque élément dans l'intervalle [l, r) (inclus à gauche, exclu à droite),
        en appliquant la mise à jour de façon paresseuse (lazy propagation simple sans propagation descendante).

        Args:
            l (int): Indice de début (inclus).
            r (int): Indice de fin (exclu).
            x (int): Valeur à ajouter sur l'intervalle.
        """
        # Convertir les indices de l'espace utilisateur à l'espace du noeud feuille
        l += self.seg_len
        r += self.seg_len
        while l < r:
            # Si l'est impair, il correspond à un segment seul à couvrir
            if l & 1 == 1:
                self.node[l] += x
                l += 1
            # Si r est impair, (r-1) correspond à un segment seul à couvrir
            if r & 1 == 1:
                self.node[r - 1] += x
                r -= 1
            # Remonter dans l'arbre pour la prochaine couche
            l >>= 1
            r >>= 1

    def get(self, idx):
        """
        Récupère la valeur courante à l'indice "idx", en accumulant toutes les mises à jour
        qui concernent ce point (remontée du chemin de la feuille à la racine).

        Args:
            idx (int): Indice de l'élément à récupérer.

        Returns:
            int: Valeur obtenue à l'indice concerné.
        """
        # Commencer à la feuille correspondant à idx
        idx += self.seg_len
        ret = self.node[idx]
        # Remonter vers la racine, additionner toutes les valeurs sur le chemin
        while idx > 1:
            idx >>= 1
            ret += self.node[idx]
        return ret


# Lecture des entrées et gestion des requêtes
n, q = map(int, input().split())
seg_tree = SegmentTree(n)

for _ in range(q):
    query = [int(x) for x in input().split()]
    if len(query) == 4:
        # Requête de type ajout sur intervalle: 1 l r x   (on suppose que le premier nombre est le type)
        _, l, r, x = query
        # Ajuster les indices à partir de 0 (les entrées sont 1-indexées)
        l -= 1
        r -= 1
        # Ajouter x à l'intervalle [l, r] donc [l, r+1) car r est inclusif dans l'entrée mais add est exclusif
        seg_tree.add(l, r + 1, x)
    if len(query) == 2:
        # Requête de récupération: 2 i
        _, i = query
        i -= 1  # Ajuster l'indice à 0-based
        print(seg_tree.get(i))