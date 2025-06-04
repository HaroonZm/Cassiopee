import sys
from math import sqrt, atan2, acos, sin, cos
from sys import stdin
input = stdin.readline

class Point(object):
    """
    Représente un point dans le plan 2D.

    Attributs:
        x (float): La coordonnée x du point.
        y (float): La coordonnée y du point.
        epsilon (float): Précision utilisée pour la comparaison flottante.

    Méthodes:
        __add__: Addition de points (coordonnée par coordonnée).
        __sub__: Soustraction de points (coordonnée par coordonnée).
        __mul__: Multiplication par un scalaire.
        __truediv__: Division par un scalaire.
        __lt__, __eq__: Opérateurs de comparaison.
        norm: Renvoie la norme au carré.
        __abs__: Renvoie la norme euclidienne.
        ccw: Teste l'orientation par rapport à un segment (utilisé pour la géométrie orientée).
        project: Projette ce point sur une droite/segment.
        reflect: Calcule le reflet du point par rapport à une droite/segment.
        distance: Calcule la distance minimale entre le point et un segment.
    """
    epsilon = 1e-10

    def __init__(self, x=0.0, y=0.0):
        if isinstance(x, tuple):
            # Création à partir d'un tuple
            self.x = x[0]
            self.y = x[1]
        else:
            self.x = x
            self.y = y

    def __add__(self, other):
        """Additionne deux points."""
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Soustrait deux points."""
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        """Multiplie les coordonnées du point par un scalaire."""
        return Point(other * self.x, other * self.y)

    def __truediv__(self, other):
        """Divise les coordonnées du point par un scalaire."""
        return Point(self.x / other, self.y / other)

    def __lt__(self, other):
        """Compare deux points lexicographiquement."""
        if self.x == other.x:
            return self.y < other.y
        else:
            return self.x < other.x

    def __eq__(self, other):
        """Teste l'égalité de deux points en utilisant epsilon comme tolérance."""
        from math import fabs
        return fabs(self.x - other.x) < Point.epsilon and fabs(self.y - other.y) < Point.epsilon

    def norm(self):
        """Renvoie la norme au carré."""
        return self.x * self.x + self.y * self.y

    def __abs__(self):
        """Renvoie la norme euclidienne du point."""
        return sqrt(self.norm())

    def ccw(self, p0, p1):
        """
        Détermine la position du point courant par rapport au segment (p0, p1).

        Args:
            p0 (Point): Premier sommet du segment.
            p1 (Point): Second sommet du segment.

        Returns:
            int: Code de position :
                1 : COUNTER_CLOCKWISE (gauche)
               -1 : CLOCKWISE (droite)
                2 : ONLINE_BACK (en arrière)
               -2 : ONLINE_FRONT (en avant)
                0 : ON_SEGMENT (sur le segment)
        """
        a = Vector(p1 - p0)
        b = Vector(self - p0)
        if Vector.cross(a, b) > Point.epsilon:
            return 1  # COUNTER_CLOCKWISE
        elif Vector.cross(a, b) < -Point.epsilon:
            return -1  # CLOCKWISE
        elif Vector.dot(a, b) < -Point.epsilon:
            return 2  # ONLINE_BACK
        elif a.norm() < b.norm():
            return -2  # ONLINE_FRONT
        else:
            return 0  # ON_SEGMENT

    def project(self, s):
        """
        Projette ce point sur la droite/segment défini par s.

        Args:
            s (Segment): Le segment sur lequel projeter le point.

        Returns:
            Point: Le point projeté sur la droite contenant s.
        """
        base = Vector(s.p2 - s.p1)
        a = Vector(self - s.p1)
        r = Vector.dot(a, base)
        r /= base.norm()
        return s.p1 + base * r

    def reflect(self, s):
        """
        Renvoie le symétrique de ce point par rapport à la droite/segment s.

        Args:
            s (Segment): Segment de réflection.

        Returns:
            Point: Le point réfléchi.
        """
        proj = self.project(s)
        return self + (proj - self) * 2

    def distance(self, s):
        """
        Calcule la distance minimale entre ce point et le segment s.

        Args:
            s (Segment): Le segment.

        Returns:
            float: La distance minimale.
        """
        # Si le point projeté est en dehors du segment, prendre la distance au point le plus proche.
        if Vector.dot(s.p2 - s.p1, self - s.p1) < 0.0:
            return abs(self - s.p1)
        if Vector.dot(s.p1 - s.p2, self - s.p2) < 0.0:
            return abs(self - s.p2)
        # Sinon, distance projetée sur le segment
        return abs(Vector.cross(s.p2 - s.p1, self - s.p1) / abs(s.p2 - s.p1))

class Vector(Point):
    """
    Représente un vecteur dans le plan 2D.
    Hérite de Point pour une compatibilité maximale.

    Méthodes:
        dot: Produit scalaire entre deux vecteurs.
        cross: Produit vectoriel (déterminant) entre deux vecteurs.
        is_orthogonal: Détermine si deux vecteurs sont orthogonaux.
        is_parallel: Détermine si deux vecteurs sont parallèles.
    """
    def __init__(self, x=0.0, y=0.0):
        if isinstance(x, tuple):
            self.x = x[0]
            self.y = x[1]
        elif isinstance(x, Point):
            self.x = x.x
            self.y = x.y
        else:
            self.x = x
            self.y = y

    def __add__(self, other):
        """Additionne deux vecteurs."""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Soustrait deux vecteurs."""
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        """Multiplie le vecteur par un scalaire."""
        return Vector(other * self.x, other * self.y)

    def __truediv__(self, other):
        """Divise le vecteur par un scalaire."""
        return Vector(self.x / other, self.y / other)

    @classmethod
    def dot(cls, a, b):
        """
        Calcule le produit scalaire entre deux vecteurs.

        Args:
            a (Vector): Premier vecteur.
            b (Vector): Second vecteur.

        Returns:
            float: Produit scalaire.
        """
        return a.x * b.x + a.y * b.y

    @classmethod
    def cross(cls, a, b):
        """
        Calcule le produit vectoriel (déterminant) dans le plan entre deux vecteurs.

        Args:
            a (Vector): Premier vecteur.
            b (Vector): Second vecteur.

        Returns:
            float: Résultat du déterminant, positif si b à gauche de a.
        """
        return a.x * b.y - a.y * b.x

    @classmethod
    def is_orthogonal(cls, a, b):
        """
        Teste si deux vecteurs sont orthogonaux (angle droit).

        Args:
            a (Vector): Premier vecteur.
            b (Vector): Second vecteur.

        Returns:
            bool: True si orthogonaux.
        """
        return abs(Vector.dot(a, b)) < Point.epsilon

    @classmethod
    def is_parallel(cls, a, b):
        """
        Teste si deux vecteurs sont parallèles.

        Args:
            a (Vector): Premier vecteur.
            b (Vector): Second vecteur.

        Returns:
            bool: True si parallèles.
        """
        return abs(Vector.cross(a, b)) < Point.epsilon

class Segment(object):
    """
    Représente un segment de droite (ou une droite si utilisé ainsi) entre deux points.

    Attributs:
        p1 (Point): Extrémité 1.
        p2 (Point): Extrémité 2.

    Méthodes:
        intersect: Teste si deux segments se croisent.
        cross_point: Si intersection existe, retourne le point d'intersection.
        distance: Distance minimale entre deux segments.
        is_orthogonal, is_parallel: Méthodes de classe pour tester l’orthogonalité ou le parallélisme.
    """
    def __init__(self, p1=Point(), p2=Point()):
        if isinstance(p1, Point):
            self.p1 = p1
            self.p2 = p2
        elif isinstance(p1, tuple):
            self.p1 = Point(p1[0], p1[1])
            self.p2 = Point(p2[0], p2[1])

    def intersect(self, s):
        """
        Vérifie si ce segment et le segment s se croisent.

        Args:
            s (Segment): Autre segment.

        Returns:
            bool: True si les segments se croisent.
        """
        ans1 = s.p1.ccw(self.p1, self.p2) * s.p2.ccw(self.p1, self.p2)
        ans2 = self.p1.ccw(s.p1, s.p2) * self.p2.ccw(s.p1, s.p2)
        return ans1 <= 0 and ans2 <= 0

    def cross_point(self, s):
        """
        Calcule le point d'intersection entre ce segment et le segment s, supposé qu'ils se croisent.

        Args:
            s (Segment): Autre segment.

        Returns:
            Point: Le point d'intersection.
        """
        base = s.p2 - s.p1
        d1 = abs(Vector.cross(base, self.p1 - s.p1))
        d2 = abs(Vector.cross(base, self.p2 - s.p1))
        t = d1 / (d1 + d2)
        return self.p1 + (self.p2 - self.p1) * t

    def distance(self, s):
        """
        Calcule la distance minimale entre ce segment et un autre segment.

        Args:
            s (Segment): Autre segment.

        Returns:
            float: La distance minimale.
        """
        if self.intersect(s):
            return 0.0
        d1 = s.p1.distance(self)
        d2 = s.p2.distance(self)
        d3 = self.p1.distance(s)
        d4 = self.p2.distance(s)
        return min(d1, d2, d3, d4)

    @classmethod
    def is_orthogonal(cls, s1, s2):
        """
        Teste si les segments sont orthogonaux.

        Args:
            s1 (Segment): Premier segment.
            s2 (Segment): Second segment.

        Returns:
            bool: True si orthogonaux.
        """
        a = Vector(s1.p2 - s1.p1)
        b = Vector(s2.p2 - s2.p1)
        return Vector.is_orthogonal(a, b)

    @classmethod
    def is_parallel(cls, s1, s2):
        """
        Teste si les segments sont parallèles.

        Args:
            s1 (Segment): Premier segment.
            s2 (Segment): Second segment.

        Returns:
            bool: True si parallèles.
        """
        a = Vector(s1.p2 - s1.p1)
        b = Vector(s2.p2 - s2.p1)
        return Vector.is_parallel(a, b)

class Line(Segment):
    """
    Alias pour Segment mais utile lorsque le concept de droite est utilisé.
    """
    pass

class Cirle(object):
    """
    Représente un cercle dans le plan 2D.

    Attributs:
        c (Point): Centre du cercle.
        r (float): Rayon du cercle.

    Méthodes:
        cross_points: Calcule les points d'intersection avec un segment ou un autre cercle.
    """
    def __init__(self, x, y=Point(), r=1.0):
        if isinstance(x, Point):
            self.c = x
            self.r = y
        elif isinstance(x, tuple):
            self.c = Point(x[0], x[1])
            self.r = r

    def cross_points(self, s):
        """
        Calcule les points d'intersection du cercle avec un segment ou un autre cercle.

        Args:
            s (Segment|Cirle): Segment ou cercle pour intersection.

        Returns:
            tuple: Deux Points représentant les points d'intersection.
        """
        if isinstance(s, Segment):
            pr = self.c.project(s)
            e = (s.p2 - s.p1) / abs(s.p2 - s.p1)
            base = sqrt(self.r * self.r - (pr - self.c).norm())
            return pr + e * base, pr - e * base
        elif isinstance(s, Cirle):
            c2 = s
            d = abs(self.c - c2.c)
            a = acos((self.r * self.r + d * d - c2.r * c2.r) / (2 * self.r * d))
            t = atan2(c2.c.y - self.c.y, c2.c.x - self.c.x)
            temp1 = Point(cos(t + a) * self.r, sin(t + a) * self.r)
            temp2 = Point(cos(t - a) * self.r, sin(t - a) * self.r)
            return self.c + temp1, self.c + temp2

def contains(polygon, p):
    """
    Détermine la position d'un point p par rapport à un polygone donné.

    Args:
        polygon (list of Point): Liste des sommets du polygone (dans l'ordre).
        p (Point): Le point à tester.

    Returns:
        int: 0 si à l'extérieur, 1 si sur le bord, 2 si à l'intérieur.
    """
    n = len(polygon)
    x = False
    for i in range(n):
        a = polygon[i] - p
        b = polygon[(i + 1) % n] - p
        # Si le point est sur un côté du polygone
        if abs(Vector.cross(a, b)) < Point.epsilon and Vector.dot(a, b) < Point.epsilon:
            return 1
        # Inversion si les points sont dans le "bon" ordre pour croiser l'axe y=0.
        if a.y > b.y:
            a, b = b, a
        # Comptage des croisements avec le demi-axe positif pour l'algorithme de la somme d'angles
        if a.y < Point.epsilon and Point.epsilon < b.y and Vector.cross(a, b) > Point.epsilon:
            x = not x
    return 2 if x else 0

def main(args):
    """
    Lit les entrées, construit le polygone et répond à chaque requête
    pour déterminer la position du point par rapport au polygone.

    Args:
        args (list): Arguments de la ligne de commande, non utilisé ici.
    """
    n = int(input())
    polygon = []
    for _ in range(n):
        x, y = map(int, input().split())
        polygon.append(Point(x, y))
    q = int(input())
    for _ in range(q):
        x, y = map(int, input().split())
        result = contains(polygon, Point(x, y))
        print(result)

if __name__ == '__main__':
    main(sys.argv[1:])