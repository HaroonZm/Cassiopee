#!/usr/bin/python3

# Importation des bibliothèques standards Python
import array  # Permet de manipuler des tableaux de types homogènes (non utilisé ici mais importé)
from fractions import Fraction  # Permet la manipulation arithmétique exacte de fractions rationnelles
import functools  # Fournit des outils pour la programmation fonctionnelle (ex: reduce, partial; pas utilisé ici)
import itertools  # Fournit des outils de création de itérateurs avancés
import math  # Fournit l’accès à des fonctions mathématiques telles que sqrt, ceil, etc.
import os  # Permet d’interagir avec l’environnement système, par exemple variables d’environnement
import sys  # Permet d’accéder à certains paramètres et fonctions du système d’exploitation

# Fonction principale, point d'entrée de l'exécution du script
def main():
    # Lecture d’un entier N qui représente le nombre de points définissant un polygone
    N = read_int()
    # Lecture de N points, chacun sous forme d’objet Vec, stockés dans une liste P
    P = [Vec(*read_ints()) for _ in range(N)]
    # Lecture du nombre de requêtes Q
    Q = read_int()
    # Boucle pour traiter Q requêtes
    for _ in range(Q):
        # Pour chaque requête, lire les coordonnées de deux points (x1, y1) et (x2, y2)
        x1, y1, x2, y2 = read_ints()
        # Appeler la fonction solve pour résoudre la requête et afficher le résultat
        print(solve(N, P, Vec(x1, y1), Vec(x2, y2)))

# Fonction qui calcule l'aire à gauche d'une droite orientée qui coupe un polygone
def solve(N, P, A, B):
    # Calcul du vecteur directeur de la droite (b = B - A)
    b = B - A
    # Translation de tous les points du polygone: origine déplacée en A
    P = [p - A for p in P]

    # Initialisation des compteurs pour savoir de quel côté de la droite les points sont
    ccw = 0  # Compte les points à gauche de la droite (sens anti-horaire)
    cw = 0   # Compte les points à droite de la droite (sens horaire)
    for p in P:
        # Produit vectoriel entre le vecteur directeur b et le vecteur point p
        c = b.cross(p)
        # Si c >= 0, p est à gauche ou sur la droite
        if c >= 0:
            ccw += 1
        # Si c <= 0, p est à droite ou sur la droite
        if c <= 0:
            cw += 1

    # Si tous les points sont du même côté (+ ou 0), aire = aire du polygone complet
    if ccw == N:
        return float(poly_area(P))
    # Si tous sont strictement de l'autre côté, aire = 0
    if cw == N:
        return 0

    # Liste pour stocker les points d'intersection ("croisements") entre le polygone et la droite
    cross_points = []

    # Parcourir chaque arête du polygone pour trouver les intersections avec la droite
    for i in range(N):
        # Définir les indices des deux sommets de l'arête courante: p et q (=p+1 modulo N)
        j = (i + 1) % N
        p = P[i]
        q = P[j]
        qp = q - p  # Vecteur directeur de l'arête

        cross_qp_b = qp.cross(b)  # Produit vectoriel entre l'arête et la droite
        if cross_qp_b == 0:
            # Les vecteurs sont colinéaires, donc pas d'intersection propre
            continue
        # Calcul d'un coefficient k pour trouver la position d'intersection sur l'arête
        k = Fraction(b.cross(p), cross_qp_b)
        # On veut une intersection à l'intérieur de l'arête (0 < k <=1)
        if 0 < k <= 1:
            # Calcul du coefficient t pour marquer l'ordre des intersections le long de la droite
            t = Fraction(p.cross(qp), b.cross(qp))
            # Ajouter le point d'intersection sous forme de tuple (t, i, k)
            cross_points.append((t, i, k))

    # Ordonner les points d'intersection selon leur position sur la droite (ordre croissant de t)
    cross_points.sort()
    # Extraire l'indice et le coefficient k de la première intersection
    _, i1, k1 = cross_points[0]
    # Extraire l'indice et le coefficient k de la deuxième intersection
    _, i2, k2 = cross_points[1]

    # Calculer les véritables coordonnées vectorielles des deux points d'intersection
    x1 = P[i1] + k1 * (P[(i1 + 1) % N] - P[i1])
    x2 = P[i2] + k2 * (P[(i2 + 1) % N] - P[i2])
    # Initialiser la liste Q pour stocker le nouveau polygone "coupé par la droite"
    Q = [x2]
    # Boucler à partir du sommet suivant x2 jusqu'à x1, en ajoutant les sommets dans Q
    j = (i2 + 1) % N
    while j != i1:
        Q.append(P[j])
        j = (j + 1) % N
    # Ajouter le dernier sommet x1 pour refermer le contour
    Q.append(P[i1])
    # Enfin, ajouter le point d'intersection x1
    Q.append(x1)

    # Retourner l’aire du polygone Q, convertie en float (car poly_area renvoie une Fraction)
    return float(poly_area(Q))

# Fonction qui calcule l'aire d'un polygone général par la formule du "shoelace"
def poly_area(P):
    N = len(P)  # Nombre de sommets
    a = 0  # Accumulateur pour l’aire
    # On considère P[0] comme point de référence, on somme les aires des triangles (P[0], P[i], P[i+1])
    for i in range(1, N - 1):
        # Calcul de l'aire signée par produit vectoriel, puis division par 2
        a += Fraction((P[i + 1] - P[i]).cross(P[0] - P[i + 1]), 2)
    # Retourner l’aire totale sous forme de Fraction
    return a

###############################################################################
# FONCTIONS AUXILIAIRES ET CLASSES POUR VECTEURS

# Classe Vec pour les vecteurs 2D
class Vec(object):
    def __init__(self, x, y):
        # Initialisation des coordonnées du vecteur aux valeurs x et y
        self.x = x
        self.y = y
        # Appel du constructeur parent de manière préventive (pas strictement nécessaire ici)
        super().__init__()

    def __add__(self, other):
        # Addition de deux vecteurs: (x, y) + (x', y') = (x + x', y + y')
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        # Soustraction de deux vecteurs: (x, y) - (x', y') = (x - x', y - y')
        return Vec(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        # Multiplication d’un vecteur par un scalaire à droite: (x, y) * s = (x*s, y*s)
        return Vec(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        # Multiplication d’un vecteur par un scalaire à gauche: s * (x, y) = (x*s, y*s)
        return Vec(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        # Division d’un vecteur par un scalaire: (x, y) / s = (x/s, y/s)
        return Vec(self.x / scalar, self.y / scalar)

    def __iadd__(self, other):
        # Addition et affectation directe: v += w
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, other):
        # Soustraction et affectation directe: v -= w
        self.x -= other.x
        self.y -= other.y
        return self

    def __imul__(self, scalar):
        # Multiplication par scalaire et affectation directe: v *= s
        self.x *= scalar
        self.y *= scalar
        return self

    def __idiv__(self, scalar):
        # Division par scalaire et affectation directe: v /= s
        self.x /= scalar
        self.y /= scalar
        return self

    def __neg__(self):
        # Négation d’un vecteur: -v = (-x, -y)
        return Vec(-self.x, -self.y)

    def __eq__(self, other):
        # Test d’égalité de deux vecteurs: v == w
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        # Test de différence entre deux vecteurs: v != w
        return not self.__eq__(other)

    def __hash__(self):
        # Permet à Vec d'être utilisé comme clé dans un dictionnaire ou un ensemble
        # On hash le tuple ('Vec', x, y) pour éviter les collisions avec d’autres types
        return hash(('Vec', self.x, self.y))

    def dot(self, other):
        # Produit scalaire entre deux vecteurs: (x, y) . (x', y') = x*x' + y*y'
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        # Produit vectoriel en 2D: (x, y) x (x', y') = x*y' - y*x'
        # Cela donne un scalaire, utile pour déterminer l’orientation ou l’aire
        return self.x * other.y - self.y * other.x

    def abs2(self):
        # Norme au carré du vecteur: x^2 + y^2
        return self.x * self.x + self.y * self.y

    def __abs__(self):
        # Norme euclidienne (longueur) du vecteur: sqrt(x^2 + y^2)
        return math.sqrt(float(self.abs2()))

    def __repr__(self):
        # Représentation lisible du vecteur pour l’affichage
        return '({}, {})'.format(self.x, self.y)

# Définir un flag de DEBUG depuis une variable d'environnement
DEBUG = 'DEBUG' in os.environ

# Fonction pour lire une ligne depuis l’entrée standard et retirer le retour à la ligne
def inp():
    return sys.stdin.readline().rstrip()

# Fonction pour lire un entier depuis l’entrée standard
def read_int():
    return int(inp())

# Fonction pour lire plusieurs entiers sur une même ligne, séparés par des espaces
def read_ints():
    return [int(e) for e in inp().split()]

# Fonction d'affichage de débogage, n’affiche que si DEBUG est activé 
def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)

# Condition d’exécution principale : si ce script est le programme principal, exécuter main()
if __name__ == '__main__':
    main()