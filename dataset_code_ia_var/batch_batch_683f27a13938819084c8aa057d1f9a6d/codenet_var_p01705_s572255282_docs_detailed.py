import sys

readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    """
    Lit un ensemble de cercles (chacun défini par une coordonnée x et un rayon r), et cherche
    le plus grand diamètre d'un cercle (horizontal) qui peut être inséré entre certains des cercles donnés,
    de manière à ce qu'il ne dépasse pas leur profil convexe supérieur (en deux dimensions).
    Utilise une recherche binaire pour calculer le diamètre maximal possible.
    Retourne True s'il y a une nouvelle instance à traiter, sinon False.
    """
    # Lecture du nombre de cercles pour l'instance courante
    N = int(readline())
    if N == 0:
        return False

    # Lecture des cercles, chacun donné par x (position horizontale), r (rayon)
    C = [list(map(int, readline().split())) for _ in range(N)]

    # Calcul pour le centrage vertical du cercle à insérer
    # e = sqrt(2)/2, distance minimale pour placer un cercle de rayon r au-dessus d’un autre
    e = 2**0.5 / 2

    # Rayon minimal: contrainte par l'agencement des cercles (position et rayon)
    r_min = max(r * e for x, r in C)
    # Rayon maximal possible : le cercle le plus grand parmi ceux donnés
    r_max = max(r for x, r in C)

    # Pré-calcul des hauteurs maximales d’insertion entre chaque paire de cercles consécutifs
    H = []
    for i in range(N - 1):
        x0, r0 = C[i]
        x1, r1 = C[i + 1]
        dx = x1 - x0
        # Calcul de la distance horizontale de la corde (l) et de la hauteur maximale (h)
        l = (r0**2 + dx**2 - r1**2) / (2 * dx)
        h = (r0**2 - l**2)**0.5
        H.append(h)

    def check(h):
        """
        Vérifie s'il est possible de placer un cercle d'une hauteur donnée (h = rayon)
        sous l'enveloppe supérieure des cercles C, en tenant compte des restrictions
        géométriques imposées par la disposition.
        Args:
            h (float): hauteur (rayon) du cercle à placer
        Returns:
            bool: True si possible, False sinon
        """
        k = -1  # Indice du cercle de départ possible pour placer le cercle à hauteur h
        for i in range(N):
            xi, ri = C[i]
            if k == -1:
                # Chercher le premier cercle où un cercle de rayon h peut être positionné
                if h <= ri:
                    k = i
            else:
                # On vérifie si l'insertion entre le cercle précédent et le courant est possible
                if H[i - 1] < h:
                    if k != -1:
                        xp, rp = C[k]
                        xq, rq = C[i - 1]
                        # Calcul des bornes horizontales où un cercle de hauteur h peut toucher les deux cercles
                        x0 = xp - (rp**2 - h**2)**0.5
                        x1 = xq + (rq**2 - h**2)**0.5
                        # Vérifie si l'espace horizontal est suffisant pour un cercle de diamètre 2h
                        if x1 - x0 >= 2 * h:
                            return True
                    # Réinitialiser le point de départ
                    if h <= ri:
                        k = i
                    else:
                        k = -1
        # Dernière vérification après la boucle
        if k == -1:
            return False
        xp, rp = C[k]
        xq, rq = C[N - 1]
        x0 = xp - (rp**2 - h**2)**0.5
        x1 = xq + (rq**2 - h**2)**0.5
        return x1 - x0 >= 2 * h

    # Recherche binaire pour trouver la hauteur (rayon) maximale possible
    left = r_min
    right = r_max + 1
    EPS = 1e-5  # Tolérance de précision pour la recherche binaire

    while right - left > EPS:
        mid = (left + right) / 2
        if check(mid):
            left = mid  # On peut essayer plus grand
        else:
            right = mid  # Trop grand, on réduit

    # Affiche le diamètre maximal possible avec 16 chiffres après la virgule
    write("%.16f\n" % (left * 2))
    return True

# Boucle principale : traiter chaque cas jusqu'à ce que solve() retourne False
while solve():
    pass