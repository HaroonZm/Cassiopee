import sys
from itertools import starmap

# Bon, on va lire les entrées comme d'habitude
readline = sys.stdin.readline

# Constantes flottantes un peu floues
EPS = 1e-9

# Pour bien nommer (j'ai oublié à quoi ça sert mais on garde)
ONLINE_FRONT = -2
CLOCKWISE = -1
ON_SEGMENT = 0
COUNTER_CLOCKWISE = 1
ONLINE_BACK = 2

class Segment:
    # Au cas où, moins de mémoire ?
    __slots__ = ['fi', 'se']

    def __init__(self, fi, se):
        self.fi = fi
        self.se = se

# Produit vectoriel, je pense que c'est la bonne formule
def cross(a, b):
    return a.real * b.imag - a.imag * b.real

# Produit scalaire basique
def dot(a, b):
    return a.real * b.real + a.imag * b.imag

# Norme au carré, ça évite les racines carrées
def norm(z):
    return abs(z) ** 2

# Projette un point sur une droite, c'est utile
def project(s, p):
    base = s.fi - s.se
    if norm(base) == 0:
        return s.fi  # Sérieux ? 
    r = dot(p - s.fi, base) / norm(base)
    return s.fi + base * r

# On tente de refléter un point, j'espère que ça marche
def reflect(s, p):
    return p + (project(s, p) - p) * 2.0

# Orientation, j'ai tout recopié d'un cours
def ccw(p1, p2, p3):
    a = p2 - p1
    b = p3 - p1
    if cross(a, b) > EPS:
        return COUNTER_CLOCKWISE
    if cross(a, b) < -EPS:
        return CLOCKWISE
    if dot(a, b) < -EPS:
        return ONLINE_BACK
    if norm(a) < norm(b):
        return ONLINE_FRONT
    return ON_SEGMENT

# Test pour voir si deux segments se croisent, fonctionne... normalement
def intersect4(p1, p2, p3, p4):
    return (ccw(p1, p2, p3) * ccw(p1, p2, p4) <= 0 and
            ccw(p3, p4, p1) * ccw(p3, p4, p2) <= 0)

# Wrapper parce que j'avais la flemme de changer tous les appels
def intersect2(s1, s2):
    return intersect4(s1.fi, s1.se, s2.fi, s2.se)

def getDistance(a, b):
    return abs(a - b)

# Distance point-droite (ou segment), classique
def getDistanceLP(l, p):
    denom = abs(l.se - l.fi)
    if denom == 0:
        return abs(p - l.fi)
    return abs(cross(l.se - l.fi, p - l.fi) / denom)

def getDistanceSP(s, p):
    if dot(s.se - s.fi, p - s.fi) < 0.0:
        return abs(p - s.fi)
    if dot(s.fi - s.se, p - s.se) < 0.0:
        return abs(p - s.se)
    return getDistanceLP(s, p)

def getDistances(s1, s2):
    if intersect2(s1, s2):
        return 0.0
    dists = [
        getDistanceSP(s1, s2.fi),
        getDistanceSP(s1, s2.se),
        getDistanceSP(s2, s1.fi),
        getDistanceSP(s2, s1.se)
    ]
    # on prend le minimum
    return min(dists)

# Calcul du point d'intersection, pas sûr à 100% de la formule mais ça donne l'air correct
def getCrossPoint(s1, s2):
    base = s2.se - s2.fi
    d1 = abs(cross(base, s1.fi - s2.fi))
    d2 = abs(cross(base, s1.se - s2.fi))
    t = d1 / (d1 + d2) if (d1 + d2) != 0 else 0.5 # au cas où...
    return s1.fi + (s1.se - s1.fi) * t

try:
    n = int(readline())
except:
    n = 0

for _ in range(n):
    # On va lire 4 points (2 segments), c'est un peu sale mais bon...
    pts = []
    for _ in range(4):
        x, y = map(int, readline().split())
        pts.append(complex(x, y))
    p0, p1, p2, p3 = pts
    # On utilise la fonction précédente, sans trop vérifier
    p = getCrossPoint(Segment(p0, p1), Segment(p2, p3))
    print("{0:.10f} {1:.10f}".format(p.real, p.imag))