from math import sin, cos, atan2

def sgn(x, eps=1e-10):
    """
    Determine le signe d'un nombre flottant x en tenant compte d'une tolérance eps.

    Args:
        x (float): Le nombre à évaluer.
        eps (float, optionnel): La tolérance autour de zéro (défaut: 1e-10).

    Returns:
        int: -1 si x est négatif, 1 si x est positif, 0 si x est proche de zéro (entre -eps et eps).
    """
    if x < -eps:
        return -1
    if -eps <= x <= eps:
        return 0
    if eps < x:
        return 1

class Vector():
    """
    Classe représentant un vecteur 2D avec coordonnées réelles.
    Fournit diverses opérations vectorielles utiles en géométrie.
    """
    def __init__(self, x=0.0, y=0.0):
        """
        Initialise un vecteur avec les coordonnées x et y.

        Args:
            x (float, optionnel): Abscisse du vecteur (défaut: 0.0).
            y (float, optionnel): Ordonnée du vecteur (défaut: 0.0).
        """
        self.x = x
        self.y = y

    def arg(self):
        """
        Calcule l'argument (angle avec l'axe des x) du vecteur.

        Returns:
            float: L'angle en radians.
        """
        return atan2(self.y, self.x)

    def norm(self):
        """
        Calcule la norme euclidienne (longueur) du vecteur.

        Returns:
            float: La norme du vecteur.
        """
        return (self.x**2 + self.y**2)**0.5

    def rotate(self, t):
        """
        Retourne un nouveau vecteur résultant de la rotation de ce vecteur d'un angle t.

        Args:
            t (float): L'angle de rotation en radians.

        Returns:
            Vector: Le vecteur résultant après rotation.
        """
        nx = self.x * cos(t) - self.y * sin(t)
        ny = self.x * sin(t) + self.y * cos(t)
        return Vector(nx, ny)

    def counter(self):
        """
        Retourne le vecteur opposé (direction inverse).

        Returns:
            Vector: Le vecteur opposé.
        """
        nx = -self.x
        ny = -self.y
        return Vector(nx, ny)

    def times(self, k):
        """
        Multiplie ce vecteur par un scalaire.

        Args:
            k (float): Le scalaire.

        Returns:
            Vector: Le vecteur redimensionné.
        """
        nx = self.x * k
        ny = self.y * k
        return Vector(nx, ny)

    def unit(self):
        """
        Retourne le vecteur unitaire (de norme 1) dans la même direction.

        Returns:
            Vector: Le vecteur unitaire.
        """
        norm = self.norm()
        nx = self.x / norm
        ny = self.y / norm
        return Vector(nx, ny)

    def normal(self):
        """
        Retourne un vecteur unitaire normal (orthogonal) à ce vecteur vers la gauche.

        Returns:
            Vector: Le vecteur normal unitaire.
        """
        norm = self.norm()
        nx = -self.y / norm
        ny = self.x / norm
        return Vector(nx, ny)

    def add(self, other):
        """
        Additionne ce vecteur avec un autre.

        Args:
            other (Vector): Le vecteur à additionner.

        Returns:
            Vector: La somme des deux vecteurs.
        """
        nx = self.x + other.x
        ny = self.y + other.y
        return Vector(nx, ny)

    def sub(self, other):
        """
        Soustrait un autre vecteur de ce vecteur.

        Args:
            other (Vector): Le vecteur à soustraire.

        Returns:
            Vector: La différence des deux vecteurs.
        """
        nx = self.x - other.x
        ny = self.y - other.y
        return Vector(nx, ny)

    def dot(self, other):
        """
        Calcule le produit scalaire avec un autre vecteur.

        Args:
            other (Vector): Le vecteur avec lequel effectuer le produit scalaire.

        Returns:
            float: Le produit scalaire des deux vecteurs.
        """
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        """
        Calcule le produit vectoriel (z) avec un autre vecteur.

        Args:
            other (Vector): Le vecteur avec lequel effectuer le produit vectoriel.

        Returns:
            float: La composante z du produit vectoriel.
        """
        return self.x * other.y - self.y * other.x

    def __str__(self):
        """
        Retourne une représentation chaîne de caractères pour l'affichage du vecteur,
        avec 9 décimales de précision pour chaque coordonnée.

        Returns:
            str: Représentation du vecteur.
        """
        return '{:.9f}'.format(self.x) + ' ' + '{:.9f}'.format(self.y)

class Line():
    """
    Classe représentant une droite par deux points (vecteurs) dans le plan.
    Permet de réaliser des projections ou des réflexions par rapport à la droite.
    """
    def __init__(self, bgn=Vector(), end=Vector()):
        """
        Initialise la droite à partir de deux points (vecteurs).

        Args:
            bgn (Vector, optionnel): Premier point de la droite (défaut: origine).
            end (Vector, optionnel): Second point de la droite (défaut: origine).
        """
        self.bgn = bgn
        self.end = end

    def build(self, a, b, c):
        """
        Construit la droite à partir des coefficients (a, b, c) de l'équation ax + by + c = 0.
        Définit deux points de la droite en fonction des coefficients.

        Args:
            a (float): Coefficient de x.
            b (float): Coefficient de y.
            c (float): Terme constant.
        """
        assert sgn(a) != 0 or sgn(b) != 0
        if sgn(b) == 0:
            # Si b==0, droite verticale: x = -c/a
            self.bgn = Vector(-c / a, 0.0)
            self.end = Vector(-c / a, 1.0)
        else:
            # Si b ≠ 0, choisir deux points distincts sur la droite
            self.v = Vector(0, -c / b)
            self.u = Vector(1.0, -(a + c) / b)

    def vec(self):
        """
        Renvoie le vecteur directeur de la droite (end - bgn).

        Returns:
            Vector: Le vecteur directeur de la droite.
        """
        return self.end.sub(self.bgn)

    def projection(self, point):
        """
        Calcule la projection orthogonale d'un point sur la droite.

        Args:
            point (Vector): Le point à projeter.

        Returns:
            Vector: Le point projeté sur la droite.
        """
        v = self.vec()              # Vecteur directeur de la droite
        u = point.sub(self.bgn)     # Vecteur du début de la droite vers le point
        k = v.dot(u) / v.norm()     # Distance projetée sur la droite
        h = v.unit().times(k)       # Vecteur projeté selon la direction
        return self.bgn.add(h)      # Point projeté

    def refrection(self, point):
        """
        Calcule le point réfléchi par rapport à la droite (symétrique du point de l'autre côté de la droite).

        Args:
            point (Vector): Le point dont on veut la réflexion.

        Returns:
            Vector: Le point réfléchi par rapport à la droite.
        """
        proj = self.projection(point)                   # Projection orthogonale
        return proj.sub(point).times(2).add(point)      # Symétrique

# Lecture des coordonnées des deux extrémités de la droite
xp1, yp1, xp2, yp2 = map(int, input().split())

# Nombre de requêtes (points à réfléchir)
q = int(input())

# Création des vecteurs représentant les deux extrémités de la droite
p1 = Vector(xp1, yp1)
p2 = Vector(xp2, yp2)
l = Line(p1, p2)  # Initialisation de la droite avec ces deux points

# Pour chaque requête, lecture du point puis calcul et affichage de la réflexion
for _ in range(q):
    x, y = map(int, input().split())
    p = Vector(x, y)
    ref = l.refrection(p)
    print(ref)