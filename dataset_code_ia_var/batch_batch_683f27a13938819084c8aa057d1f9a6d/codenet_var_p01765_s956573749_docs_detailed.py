import sys

# Redéfinition de l'entrée standard pour une lecture efficace ligne par ligne.
def input():
    """Lit une ligne de l'entrée standard, retire les espaces inutiles."""
    return sys.stdin.readline().strip()

def list2d(a, b, c):
    """
    Génère une liste 2D de dimensions a x b, chaque élément initialisé à c.
    :param a: int, nombre de lignes
    :param b: int, nombre de colonnes
    :param c: valeur d'initialisation
    :return: liste 2D
    """
    return [[c] * b for i in range(a)]

def list3d(a, b, c, d):
    """
    Génère une liste 3D de dimensions a x b x c, chaque élément initialisé à d.
    :param a: int, première dimension
    :param b: int, deuxième dimension
    :param c: int, troisième dimension
    :param d: valeur d'initialisation
    :return: liste 3D
    """
    return [[[d] * c for j in range(b)] for i in range(a)]

def list4d(a, b, c, d, e):
    """
    Génère une liste 4D de dimensions a x b x c x d, chaque élément initialisé à e.
    :param a: int, première dimension
    :param b: int, deuxième dimension
    :param c: int, troisième dimension
    :param d: int, quatrième dimension
    :param e: valeur d'initialisation
    :return: liste 4D
    """
    return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]

def ceil(x, y=1):
    """
    Calcule le plafond (ceil) du quotient x/y.
    :param x: int
    :param y: int, par défaut 1
    :return: int, plus petit entier >= x/y
    """
    return int(-(-x // y))

def INT():
    """
    Lit une ligne et la convertit en entier.
    :return: int
    """
    return int(input())

def MAP():
    """
    Lit une ligne et en extrait des entiers.
    :return: tuple d'int
    """
    return map(int, input().split())

def LIST(N=None):
    """
    Retourne une liste d'entiers lue depuis l'entrée standard.
    :param N: int ou None, nombre de valeurs à lire. Si None, lit toute la ligne.
    :return: list d'int
    """
    return list(MAP()) if N is None else [INT() for i in range(N)]

def Yes():
    """Affiche 'Yes'."""
    print('Yes')

def No():
    """Affiche 'No'."""
    print('No')

def YES():
    """Affiche 'YES'."""
    print('YES')

def NO():
    """Affiche 'NO'."""
    print('NO')

# Augmentation du niveau de récursion maximal
sys.setrecursionlimit(10 ** 9)

# Constantes pratiques
INF = 10 ** 18
MOD = 10 ** 9 + 7

class Geometry:
    """
    Classe utilitaire pour calculs géométriques en 2D.
    Fournit diverses méthodes pour opérations vectorielles, calculs de distances,
    projections, intersections, etc.
    """

    EPS = 10 ** -9  # Tolérance des comparaisons flottantes

    def add(self, a, b):
        """
        Additionne deux points/vecteurs.
        :param a: tuple (x1, y1)
        :param b: tuple (x2, y2)
        :return: tuple (x1+x2, y1+y2)
        """
        x1, y1 = a
        x2, y2 = b
        return (x1 + x2, y1 + y2)

    def sub(self, a, b):
        """
        Soustrait deux points/vecteurs.
        :param a: tuple (x1, y1)
        :param b: tuple (x2, y2)
        :return: tuple (x1-x2, y1-y2)
        """
        x1, y1 = a
        x2, y2 = b
        return (x1 - x2, y1 - y2)

    def mul(self, a, b):
        """
        Multiplie un vecteur par un scalaire ou un autre vecteur (produit de Hadamard).
        :param a: tuple (x1, y1)
        :param b: float, int ou tuple (x2, y2)
        :return: tuple
        """
        x1, y1 = a
        if not isinstance(b, tuple):
            return (x1 * b, y1 * b)
        x2, y2 = b
        return (x1 * x2, y1 * y2)

    def div(self, a, b):
        """
        Divise un vecteur par un scalaire ou par composantes.
        :param a: tuple (x1, y1)
        :param b: float, int ou tuple (x2, y2)
        :return: tuple
        """
        x1, y1 = a
        if not isinstance(b, tuple):
            return (x1 / b, y1 / b)
        x2, y2 = b
        return (x1 / x2, y1 / y2)

    def abs(self, a):
        """
        Retourne la norme (longueur) d'un vecteur.
        :param a: tuple (x, y)
        :return: float
        """
        from math import hypot
        x1, y1 = a
        return hypot(x1, y1)

    def norm(self, a):
        """
        Retourne la norme au carré d'un vecteur (utile pour les comparaisons).
        :param a: tuple (x, y)
        :return: float
        """
        x, y = a
        return x ** 2 + y ** 2

    def dot(self, a, b):
        """
        Calcule le produit scalaire de deux vecteurs.
        :param a: tuple (x1, y1)
        :param b: tuple (x2, y2)
        :return: float
        """
        x1, y1 = a
        x2, y2 = b
        return x1 * x2 + y1 * y2

    def cross(self, a, b):
        """
        Calcule le produit vectoriel 2D (déterminant) entre deux vecteurs.
        :param a: tuple (x1, y1)
        :param b: tuple (x2, y2)
        :return: float
        """
        x1, y1 = a
        x2, y2 = b
        return x1 * y2 - y1 * x2

    def project(self, seg, p):
        """
        Calcule la projection orthogonale du point p sur la droite formée par le segment seg.
        :param seg: tuple de deux points ((x1, y1), (x2, y2))
        :param p: tuple (x, y)
        :return: tuple, coordonnées projetées sur seg
        """
        p1, p2 = seg
        base = self.sub(p2, p1)
        r = self.dot(self.sub(p, p1), base) / self.norm(base)
        return self.add(p1, self.mul(base, r))

    def reflect(self, seg, p):
        """
        Calcule le symétrique de p par rapport à la droite formée par le segment seg.
        :param seg: tuple de deux points ((x1, y1), (x2, y2))
        :param p: tuple (x, y)
        :return: tuple, symétrique de p
        """
        return self.add(p, self.mul(self.sub(self.project(seg, p), p), 2))

    def ccw(self, p0, p1, p2):
        """
        Détermine l'orientation des points p0, p1, p2.
        :param p0: tuple (x0, y0)
        :param p1: tuple (x1, y1)
        :param p2: tuple (x2, y2)
        :return: int, 1: anti-horaire, -1: horaire, 2/-2/0: alignés dans différents ordres
        """
        a = self.sub(p1, p0)
        b = self.sub(p2, p0)
        if self.cross(a, b) > self.EPS:
            return 1  # Anti-horaire
        if self.cross(a, b) < -self.EPS:
            return -1  # Horaire
        if self.dot(a, b) < -self.EPS:
            return 2  # p2--p0--p1
        if self.norm(a) < self.norm(b):
            return -2  # p0--p1--p2
        return 0  # p0--p2--p1

    def intersect(self, seg1, seg2):
        """
        Vérifie si deux segments 2D se coupent.
        :param seg1: tuple de deux points ((x1, y1), (x2, y2))
        :param seg2: tuple de deux points ((x3, y3), (x4, y4))
        :return: bool
        """
        p1, p2 = seg1
        p3, p4 = seg2
        return (
            self.ccw(p1, p2, p3) * self.ccw(p1, p2, p4) <= 0 and
            self.ccw(p3, p4, p1) * self.ccw(p3, p4, p2) <= 0
        )

    def get_distance_LP(self, line, p):
        """
        Calcule la distance entre une droite et un point.
        :param line: tuple de deux points ((x1, y1), (x2, y2))
        :param p: tuple (x, y)
        :return: float, distance minimale entre la droite et le point
        """
        p1, p2 = line
        return abs(self.cross(self.sub(p2, p1), self.sub(p, p1)) / self.abs(self.sub(p2, p1)))

    def get_distance_SP(self, seg, p):
        """
        Calcule la distance minimale entre un segment et un point.
        :param seg: tuple de deux points ((x1, y1), (x2, y2))
        :param p: tuple (x, y)
        :return: float
        """
        p1, p2 = seg
        if self.dot(self.sub(p2, p1), self.sub(p, p1)) < 0:
            return self.abs(self.sub(p, p1))
        if self.dot(self.sub(p1, p2), self.sub(p, p2)) < 0:
            return self.abs(self.sub(p, p2))
        return self.get_distance_LP(seg, p)

    def get_distance_SS(self, seg1, seg2):
        """
        Calcule la distance minimale entre deux segments.
        :param seg1: tuple de deux points
        :param seg2: tuple de deux points
        :return: float
        """
        p1, p2 = seg1
        p3, p4 = seg2
        if self.intersect(seg1, seg2):
            return 0
        return min(
            self.get_distance_SP(seg1, p3),
            self.get_distance_SP(seg1, p4),
            self.get_distance_SP(seg2, p1),
            self.get_distance_SP(seg2, p2),
        )

    def get_cross_pointSS(self, seg1, seg2):
        """
        Calcule le point d'intersection entre deux segments non parallèles et sécants.
        :param seg1: tuple de deux points
        :param seg2: tuple de deux points
        :return: tuple
        """
        p1, p2 = seg1
        p3, p4 = seg2
        base = self.sub(p4, p3)
        dist1 = abs(self.cross(base, self.sub(p1, p3)))
        dist2 = abs(self.cross(base, self.sub(p2, p3)))
        t = dist1 / (dist1 + dist2)
        return self.add(p1, self.mul(self.sub(p2, p1), t))

    def get_cross_pointCL(self, c, line):
        """
        Calcule les points d'intersection d'un cercle et d'une droite.
        :param c: tuple (x, y, r), centre et rayon du cercle
        :param line: tuple de deux points
        :return: liste de deux tuples, points d'intersection
        """
        from math import sqrt
        x, y, r = c
        p1, p2 = line
        pr = self.project(line, (x, y))
        e = self.div(self.sub(p2, p1), self.abs(self.sub(p2, p1)))
        base = sqrt(r * r - self.norm(self.sub(pr, (x, y))))
        return [self.add(pr, self.mul(e, base)), self.sub(pr, self.mul(e, base))]

    def arg(self, p):
        """
        Retourne l'argument (l'angle) du vecteur point p.
        :param p: tuple (x, y)
        :return: float, angle en radians
        """
        from math import atan2
        x, y = p
        return atan2(y, x)

    def polar(self, a, r):
        """
        Retourne le vecteur de module a et d'argument r.
        :param a: float, norme
        :param r: float, angle en radians
        :return: tuple
        """
        from math import sin, cos
        return (cos(r) * a, sin(r) * a)

    def get_cross_pointCC(self, c1, c2):
        """
        Calcule les points d'intersection entre deux cercles.
        :param c1: tuple (x1, y1, r1)
        :param c2: tuple (x2, y2, r2)
        :return: liste de tuples, points d'intersection
        """
        from math import acos
        x1, y1, r1 = c1
        x2, y2, r2 = c2
        d = self.abs(self.sub((x1, y1), (x2, y2)))
        a = acos((r1 * r1 + d * d - r2 * r2) / (2 * r1 * d))
        t = self.arg(self.sub((x2, y2), (x1, y1)))
        return [
            self.add((x1, y1), self.polar(r1, t + a)),
            self.add((x1, y1), self.polar(r1, t - a))
        ]

# Instanciation de la classe Geometry
gm = Geometry()

# Lecture des entrées et préparation des segments
N1 = INT()
# Construction d'un polygone ouvert sur le segment bas (y=0)
XY1 = [(0, 0)]
for i in range(N1):
    x, y = MAP()
    XY1.append((x, y))
XY1.append((1000, 0))  # Point final

N2 = INT()
# Construction d'un polygone ouvert sur le segment haut (y=1000)
XY2 = [(0, 1000)]
for i in range(N2):
    x, y = MAP()
    XY2.append((x, y))
XY2.append((1000, 1000))  # Point final

# Transformation des listes de points en listes de segments (paires de points consécutifs)
seg1 = []
for i in range(N1 + 1):
    x1, y1 = XY1[i]
    x2, y2 = XY1[i + 1]
    seg1.append(((x1, y1), (x2, y2)))

seg2 = []
for i in range(N2 + 1):
    x1, y1 = XY2[i]
    x2, y2 = XY2[i + 1]
    seg2.append(((x1, y1), (x2, y2)))

# Recherche de la distance minimale entre tous les segments des deux polylignes
mn = INF
for i in range(N1 + 1):
    for j in range(N2 + 1):
        mn = min(mn, gm.get_distance_SS(seg1[i], seg2[j]))

# Affiche la distance minimale
print(mn)