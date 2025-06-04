from math import sqrt
from typing import List, Tuple

def project(point: complex, begin: complex, end: complex) -> complex:
    """
    Calcule la projection orthogonale d'un point sur une droite définie par deux points.

    Args:
        point (complex): Le point à projeter sous forme de nombre complexe (x + yj).
        begin (complex): Le premier point définissant la droite (x + yj).
        end (complex): Le second point définissant la droite (x + yj).

    Returns:
        complex: Le point projeté sur la droite (sous forme complexe).
    """
    # Calcule le rapport complexe du vecteur point-begin sur le vecteur end-begin
    tmp = (point - begin) / (end - begin)
    # Reconstitue le point projeté sur la droite selon la partie réelle du ratio
    return tmp.real * (end - begin) + begin

if __name__ == "__main__":
    # Lecture des coordonnées du centre du cercle et du rayon
    x, y, r = map(int, input().split())
    c = complex(x, y)  # Représentation du centre du cercle sous forme complexe

    ans: List[Tuple[float, float, float, float]] = []  # Stockera les résultats finaux

    # Lecture du nombre de requêtes à traiter
    q = int(input())

    # Traite chaque requête indépendamment
    for _ in range(q):
        res = []  # Liste temporaire pour stocker les deux points d'intersection
        x, y, z, w = map(int, input().split())
        p1 = complex(x, y)  # Extrémité 1 de la droite
        p2 = complex(z, w)  # Extrémité 2 de la droite

        # Calcule la projection du centre du cercle sur la droite (p1, p2)
        proj = project(c, p1, p2)

        # Les points d'intersection se situent à une distance sqrt(r^2 - |c - proj|^2)
        # de la projection, le long de la direction (p2-p1)/|p2-p1|
        for i in (-1, 1):
            # i alterne pour couvrir les deux points d'intersection
            diff = sqrt(r**2 - abs(c - proj)**2) * (p2 - p1) / abs(p2 - p1)
            res.append(proj + i * diff)

        # Trie les points d'intersection (pour garantir un ordre stable)
        res.sort(key=lambda point: (point.real, point.imag))

        # Ajoute les coordonnées réelles de chaque point à la liste des réponses
        ans.append((res[0].real, res[0].imag, res[1].real, res[1].imag))

    # Affiche les résultats avec 6 décimales pour chaque coordonnée
    for a in ans:
        print("{:.6f} {:.6f} {:.6f} {:.6f}".format(*a))