import sys

# Redéfinition de input pour lecture rapide depuis stdin, sans saut de ligne terminal
input = lambda: sys.stdin.readline().rstrip()

class LazySegmentTree():
    """
    Lazy Segment Tree (Arbre de segment paresseux) permettant de réaliser des requêtes 
    et des modifications sur des intervalles, avec application paresseuse d'opérations.

    Attributs :
        n (int) : Taille (supportant la puissance de deux ≥ nombre de feuilles).
        X (list) : Noeuds de segment contenant les résultats agrégés.
        A (list) : Noeuds de lazy propagation contenant les valeurs à appliquer.
        size (list) : Nombre de feuilles sous chaque noeud interne (pour operations par taille de segment).
        unitX : Élément neutre pour la monïde f.
        unitA : Élément neutre pour la monïde h.
        f (callable) : Fonction d'agrégation binaire (X, X) → X.
        g (callable) : Fonction de push (X, A, size) → X.
        h (callable) : Fonction d'application sur les valeurs lazy (A, A) → A.
    """

    def __init__(self, init, unitX, unitA, f, g, h):
        """
        Initialise l'arbre de segment paresseux selon les fonctions et unités spécifiées.
        Crée les tableaux internes nécessaires à l'arbre et à la propagation paresseuse.

        Args:
            init (int ou list) : Taille de l'arbre ou tableau initial des feuilles.
            unitX : Élément neutre pour la monïde sur les segments.
            unitA : Élément neutre pour la monïde d'opération paresseuse.
            f (callable) : Fonction d'agrégation binaire (X, X) → X.
            g (callable) : Fonction d'application Lazy (X, A, size) → X.
            h (callable) : Fonction d'application sur lazy tags (A, A) → A.
        """
        self.f = f  # Agrégation de deux valeurs de segment
        self.g = g  # Application d'une opération paresseuse sur un segment
        self.h = h  # Combinaison de deux opérations paresseuses
        self.unitX = unitX
        self.unitA = unitA

        # Initialisation selon que init soit un entier (taille) ou un tableau initial
        if type(init) == int:
            self.n = init
            self.X = [unitX] * (self.n * 2)
            self.size = [1] * (self.n * 2)  # Par défaut, chaque feuille couvre 1 élément
        else:
            self.n = len(init)
            # Remplissage : feuilles = valeurs, autres = neutre
            self.X = [unitX] * self.n + init + [unitX] * (self.n - len(init))
            self.size = [0] * self.n + [1] * len(init) + [0] * (self.n - len(init))
            # Construction ascendante des agrégats depuis les feuilles
            for i in range(self.n - 1, 0, -1):
                self.X[i] = self.f(self.X[i*2], self.X[i*2|1])

        # Calcul du nombre d'éléments sous chaque noeud interne
        for i in range(self.n - 1, 0, -1):
            self.size[i] = self.size[i*2] + self.size[i*2|1]

        # Initialisation du tableau des opérations lazy avec unitA
        self.A = [unitA] * (self.n * 2)

    def update(self, i, x):
        """
        Met à jour la valeur de la feuille d'index i avec la nouvelle valeur x, 
        puis met à jour les agrégats de ses ancêtres.

        Args:
            i (int) : Index (0-based) de la feuille à mettre à jour.
            x : Nouvelle valeur à placer.
        """
        i += self.n
        self.X[i] = x
        i >>= 1
        while i:
            self.X[i] = self.f(self.X[i * 2], self.X[i * 2 | 1])
            i >>= 1

    def calc(self, i):
        """
        Calcule la vraie valeur du noeud i en appliquant l'opération lazy locale au besoin.

        Args:
            i (int) : Index du noeud
        Returns:
            Valeur agrégée avec l'opération lazy appliquée.
        """
        return self.g(self.X[i], self.A[i], self.size[i])

    def calc_above(self, i):
        """
        Met à jour tous les ancêtres du noeud donné à l'aide de 'f' et 'calc'.

        Args:
            i (int) : Index du noeud
        """
        i >>= 1
        while i:
            self.X[i] = self.f(self.calc(i * 2), self.calc(i * 2 | 1))
            i >>= 1

    def propagate(self, i):
        """
        Propagation de l'opération lazy de i vers ses enfants,
        c'est-à-dire application paresseuse de l'opération et relai du tag.

        Args:
            i (int) : Noeud à propager vers ses enfants
        """
        # Appliquer le tag lazy au noeud lui-même
        self.X[i] = self.g(self.X[i], self.A[i], self.size[i])
        # Propager le tag lazy aux enfants gauche/droite
        self.A[i * 2] = self.h(self.A[i * 2], self.A[i])
        self.A[i * 2 | 1] = self.h(self.A[i * 2 | 1], self.A[i])
        # Réinitialiser le tag lazy de ce noeud
        self.A[i] = self.unitA

    def propagate_above(self, i):
        """
        Propage la lazy tag depuis la racine jusqu'au noeud i (non inclus),
        pour garantir que toute opération paresseuse impactant i est matérialisée.

        Args:
            i (int) : Index du noeud auquel on veut appliquer toutes les lazy tags
        """
        H = i.bit_length()
        for h in range(H, 0, -1):
            self.propagate(i >> h)

    def propagate_all(self):
        """
        Propage les lazy operations pour tous les noeuds internes (pour debugging/validation globale).
        """
        for i in range(1, self.n):
            self.propagate(i)

    def getrange(self, l, r):
        """
        Calcule la valeur agrégée sur l'intervalle [l, r) avec propagation paresseuse assurée.

        Args:
            l (int) : Borne gauche (incluse), 0-based.
            r (int) : Borne droite (exclue), 0-based.
        Returns:
            Agrégat de l'intervalle [l, r)
        """
        l += self.n
        r += self.n
        l0, r0 = l // (l & -l), r // (r & -r) - 1
        self.propagate_above(l0)
        self.propagate_above(r0)

        al = self.unitX  # Accumulateur côté gauche
        ar = self.unitX  # Accumulateur côté droit
        while l < r:
            if l & 1:
                al = self.f(al, self.calc(l))
                l += 1
            if r & 1:
                r -= 1
                ar = self.f(self.calc(r), ar)
            l >>= 1
            r >>= 1
        return self.f(al, ar)

    def getvalue(self, i):
        """
        Donne la valeur du i-ième élément (après propagation si besoin).

        Args:
            i (int) : Index de l'élément (0-based)
        Returns:
            Valeur de la feuille après application de toute lazy tag la concernant
        """
        i += self.n
        self.propagate_above(i)
        return self.calc(i)

    def operate_range(self, l, r, a):
        """
        Applique paresseusement l'opération 'a' sur l'intervalle [l, r).

        Args:
            l (int) : Borne gauche (incluse), 0-based.
            r (int) : Borne droite (exclue), 0-based.
            a : Opération à appliquer
        """
        l += self.n
        r += self.n
        l0, r0 = l // (l & -l), r // (r & -r) - 1
        self.propagate_above(l0)
        self.propagate_above(r0)
        while l < r:
            if l & 1:
                self.A[l] = self.h(self.A[l], a)
                l += 1
            if r & 1:
                r -= 1
                self.A[r] = self.h(self.A[r], a)
            l >>= 1
            r >>= 1

        self.calc_above(l0)
        self.calc_above(r0)

    def max_right(self, l, z):
        """
        Cherche le plus à droite r ≥ l tel que la propriété z(f(A[l],...,A[r-1])) soit vraie,
        mais qui échoue à r.

        Args:
            l (int) : Point de départ (inclus), 0-based.
            z (callable) : Fonction booléenne de coupure.
        Returns:
            Index r (0-based) maximal vérifiant la propriété.
        """
        if l >= self.n:
            return self.n
        l += self.n
        s = self.unitX
        while True:
            while l % 2 == 0:
                l >>= 1
            if not z(self.f(s, self.calc(l))):
                while l < self.n:
                    l *= 2
                    if z(self.f(s, self.calc(l))):
                        s = self.f(s, self.calc(l))
                        l += 1
                return l - self.n
            s = self.f(s, self.calc(l))
            l += 1
            if l & -l == l:
                break
        return self.n

    def min_left(self, r, z):
        """
        Cherche le plus à gauche l < r tel que la propriété z(f(A[l],...,A[r-1])) soit vraie
        mais échoue en avançant plus à gauche.

        Args:
            r (int) : Fin d'intervalle (exclue), 0-based.
            z (callable) : Fonction booléenne de coupure.
        Returns:
            Index l (0-based) minimal vérifiant la propriété.
        """
        if r <= 0:
            return 0
        r += self.n
        s = self.unitX
        while True:
            r -= 1
            while r > 1 and r % 2:
                r >>= 1
            if not z(self.f(self.calc(r), s)):
                while r < self.n:
                    r = r * 2 + 1
                    if z(self.f(self.calc(r), s)):
                        s = self.f(self.calc(r), s)
                        r -= 1
                return r + 1 - self.n
            s = self.f(self.calc(r), s)
            if r & -r == r:
                break
        return 0

    def debug(self):
        """
        Affiche la valeur concrète des feuilles (après propagation, pour debug).
        """
        X = self.X
        print("X =", [self.calc(i) for i in range(self.n, self.n * 2)])


# Exemple de fonctions d'agrégation/d'opération paresseuse pour gestion d'inversions dans un array binaire
mm = 262143  # Masque binaire sur 18 bits

def f(x, y):
    """
    Fonction d'agrégation : fusionne deux segments codant (inv, zéros, uns)

    Args:
        x (int) : Encodage sur 54 bits, inv<<36|zéros<<18|uns
        y (int) : Encodage identique
    Returns:
        int : Encodage fusionné du segment résultant
    """
    x0, x1, x2 = x >> 36, (x >> 18) & mm, x & mm
    y0, y1, y2 = y >> 36, (y >> 18) & mm, y & mm
    # inv = inv_l + inv_r + (uns_l * zeros_r)
    return ((x0 + y0 + x2 * y1) << 36) + ((x1 + y1) << 18) + (x2 + y2)

def g(x, a, s):
    """
    Application paresseuse : si a==1, flip du segment binaire (inversions recalculées)

    Args:
        x (int) : Encodage du segment
        a (int) : Flip à appliquer (0 ou 1)
        s (int) : Taille du segment (inutile ici)
    Returns:
        int : Nouveau codage du segment (flip appliqué si a==1)
    """
    x0, x1, x2 = x >> 36, (x >> 18) & mm, x & mm
    # Flipper toutes les valeurs : swap uns/zeros, inversion = zeros*uns - inversion
    return ((x1 * x2 - x0) << 36) + (x2 << 18) + x1 if a else x

def h(a, b):
    """
    Combinaison d'opérations lazy : XOR sur le flip

    Args:
        a (int) : op précédente
        b (int) : nouvelle op
    Returns:
        int : op combinée
    """
    return a ^ b

unitX = 0  # Encodage du segment neutre (inv=0, zeros=0, uns=0)
unitA = 0  # Pas d'opération lazy par défaut


# Lecture des paramètres d'entrée : taille et nombre de requêtes
N, Q = map(int, input().split())
# Encodage des valeurs initiales : 0 → 1<<18, 1 → 1 (c.a.d. (inv=0, zeros/uns=0/1))
A = [(1 << 18) if int(a) == 0 else 1 for a in input().split()]
st = LazySegmentTree(A, unitX, unitA, f, g, h)

# Traitement des requêtes
for _ in range(Q):
    t, l, r = map(int, input().split())
    if t == 1:
        # Flip (inverser tous les bits de l'intervalle)
        st.operate_range(l - 1, r, 1)
    else:
        # Affiche le nombre d'inversions dans [l-1, r)
        print(st.getrange(l - 1, r) >> 36)