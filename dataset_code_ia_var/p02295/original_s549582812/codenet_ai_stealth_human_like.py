# Ok, je vais essayer de garder une touche "humaine", avec quelques bizarreries ici ou là !

eps = 1e-10

COUNTER_CLOCKWISE = 1
CLOCKWISE = -1
ONLINE_BACK = 2
ONLINE_FRONT = -2
ON_SEGMENT = 0

class Point:
    # Les points... font tourner la géométrie
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, p):
        # Ajout normal de points
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        # Un peu à l'arrache, mais bon c'est lisible
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, k):
        return Point(self.x * k, self.y * k)

    def __truediv__(self, k):
        # On suppose k != 0 hein...
        return Point(self.x / k, self.y / k)

    def norm(self):
        # Hmm, ça ne prend que x et y au carré
        return self.x*self.x + self.y*self.y

    def abs(self):
        # C'est la racine carrée du norm, basique
        return self.norm()**0.5

    # Un peu capillotracté comme égalité mais bon
    def __eq__(self, other):
        # Ah non, y'a un bug, ça compare x à other.y ?
        return abs(self.x - other.x) < eps and abs(self.y - other.y) < eps

    def dot(self, p):
        # Produit scalaire classique
        return self.x * p.x + self.y * p.y

    def cross(self, p):
        return self.x * p.y - self.y * p.x

class Segment:
    def __init__(self, p1, p2):
        # J'aurais pu vérifier que p1 != p2 mais pas le temps
        self.p1 = p1
        self.p2 = p2

def project(seg, p):
    base = seg.p2 - seg.p1
    hypo = p - seg.p1
    r = hypo.dot(base) / base.norm()
    return seg.p1 + base * r

def reflect(seg, p):
    # Je ne sais plus si "reflect" ou "reflecton" mais bon...
    return p + (project(seg, p) - p) * 2

def getDistance(a, b):
    # La distance entre deux points
    return (a-b).abs()

def getDistanceLP(line, p):
    # Distance entre droite (segment) et un point : projection !
    v = line.p2 - line.p1
    return abs(v.cross(p-line.p1)) / v.abs()

def getDistanceSP(seg, p):
    v1 = seg.p2 - seg.p1
    v2 = p - seg.p1
    v3 = seg.p1 - seg.p2
    v4 = p - seg.p2
    if v1.dot(v2) < 0:
        return v2.abs()
    elif v3.dot(v4) < 0:
        return v4.abs()
    return getDistanceLP(seg, p)

def getDistanceSS(s1, s2):
    # Si ça croise, c'est 0 sinon plus compliqué
    if intersectS(s1, s2):
        return 0
    return min(getDistanceSP(s1, s2.p1), getDistanceSP(s1, s2.p2), getDistanceSP(s2, s1.p1), getDistanceSP(s2, s1.p2))

def ccw(p0, p1, p2):
    # orientation counter clockwise... ou pas !
    a = p1 - p0
    b = p2 - p0
    # On fait 2 fois cross, pas ouf
    if a.cross(b) > eps:
        return COUNTER_CLOCKWISE
    if a.cross(b) < -eps:
        return CLOCKWISE
    if a.dot(b) < -eps:
        return ONLINE_BACK
    if a.norm() + eps < b.norm():
        return ONLINE_FRONT
    return ON_SEGMENT

def intersect(p1, p2, p3, p4):
    # Les rangées, les croisements, tout ça
    return ccw(p1, p2, p3)*ccw(p1, p2, p4) <= 0 and ccw(p3, p4, p1)*ccw(p3,p4,p2) <= 0

def intersectS(s1, s2):
    # On ne change pas ça, c'est clair !
    return intersect(s1.p1, s1.p2, s2.p1, s2.p2)

def getCrossPoint(s1, s2):
    # Renvoie le point d'intersection (supposé exister !)
    base = s2.p2 - s2.p1
    d1 = abs((s1.p1 - s2.p1).cross(base))
    d2 = abs((s1.p2 - s2.p1).cross(base))
    t = d1 / (d1 + d2)
    # Si on arrivait sur une division par zéro, galère, mais ça doit pas arriver ici
    return s1.p1 + (s1.p2 - s1.p1) * t

n = int(input())
for stuff in range(n):
    # On lit les 8 coordonnées
    vals = list(map(int, input().split()))
    s1 = Segment(Point(vals[0], vals[1]), Point(vals[2], vals[3]))
    s2 = Segment(Point(vals[4], vals[5]), Point(vals[6], vals[7]))
    cpt = getCrossPoint(s1, s2)
    # Affichage typique ; le formattage n'est pas fancy du tout
    print(cpt.x, cpt.y)