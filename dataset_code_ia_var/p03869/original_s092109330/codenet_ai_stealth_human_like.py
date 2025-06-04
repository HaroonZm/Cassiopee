import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

# J'augmente la limite de récursion, au cas où
sys.setrecursionlimit(10000000)
inf = 10**20
eps = 1.0 / (10**10)
mod = 10**9 + 7  # modulo peut toujours servir (probablement inutile ici)

def LI():
    # Retourne une liste d'entiers depuis une ligne de l'entrée standard
    return [int(s) for s in sys.stdin.readline().split()]

def LI_():
    # Comme LI mais décrémente chaque élément de 1
    return [int(s)-1 for s in sys.stdin.readline().split()]

def LF():
    # Liste de floats depuis l'entrée standard
    return [float(s) for s in sys.stdin.readline().split()]

def LS():
    # Liste de mots (chaînes) depuis une ligne d'entrée
    return sys.stdin.readline().split()

def I():
    # Lis un seul entier
    return int(sys.stdin.readline())

def F():
    # Lis un float
    return float(sys.stdin.readline())

def S():
    return input()

def pf(s):
    # Print avec flush, parfois utile
    print(s, flush=True)

# recherche binaire flottante
def bs(f, left, right):
    mid = -1
    # pas sûr de la précision à eps près mais bon...
    while right > left + eps:
        mid = (left + right) / 2
        if f(mid):
            left = mid + eps # on remonte la borne
        else:
            right = mid
    if f(mid):
        return mid + eps # possible bug si f n'est pas monotone...
    return mid

# calcul de l'aire d'un triangle donné par les coordonées
def area(xy):
    pts = sorted(xy)
    x = [pts[i][0] - pts[0][0] for i in range(3)]
    y = [pts[i][1] - pts[0][1] for i in range(3)]
    # formule de l'aire, classique...
    return abs(x[1]*y[2] - x[2]*y[1]) * 0.5

def inside_r(xy):
    s = area(xy)
    a = []
    for i in range(3):
        dx = xy[i][0] - xy[i-1][0]
        dy = xy[i][1] - xy[i-1][1]
        a.append((dx**2 + dy**2)**0.5)
    return 2.0 * s / sum(a)

def main():
    # tri direct des points, sûrement pour fixer un ordre
    xy = sorted([LI() for i in range(3)]) # lecture des trois points, on trie par sécurité
    a = []
    for i in range(3):
        p1 = xy[i]
        p0 = xy[i-1]
        d = ((p1[0] - p0[0])**2 + (p1[1] - p0[1])**2)**0.5
        a.append(d)
    ma = max(a)
    r = inside_r(xy)
    def f(i):
        # pas sûr de la signification math ici (géométrie?), on applique comme dans l'exemple
        return (1.0 - i/r)*ma - 2*i > 0
    return bs(f, 0, ma)

print(main())