import math

def manhattan_max_path(d: float) -> float:
    """
    Calcule la distance maximale possible en suivant uniquement les routes
    (c'est-à-dire les axes avec coordonnées entières) entre deux points dont
    la distance euclidienne est exactement d.

    En effet, dans le type de grille de Manhattan décrit, les maisons sont sur
    les axes x = entier ou y = entier. Toute position sur la route a soit x ou y entier.

    Soit (x1, y1) et (x2, y2) deux maisons avec :
      ((x2 - x1)^2 + (y2 - y1)^2) = d^2
      avec (x1 ou y1) entier et (x2 ou y2) entier.

    On veut maximiser la distance entre eux en parcourant les routes, c'est
   -à-dire la distance de Manhattan:
      |x2 - x1| + |y2 - y1|

    La contrainte clé est que chaque maison est "sur la route":
        soit x est entier, soit y est entier.

    Donc deux cas possibles :
    1. Les deux maisons ont leur x entier (donc y quelconque) ou y entier (et x quelconque)
       -> distance Manhattan = distance euclidienne = d (cas minimal)

    2. Sinon, pour maximiser la distance sur l'axe, on place une maison sur x entier,
       l'autre sur y entier, avec la distance euclidienne d.

    Le plus grand Manhattan correspond alors à :
    - x1 entier et y2 entier, avec (x2 - x1)^2 + (y2 - y1)^2 = d^2
    - |x2 - x1| + |y2 - y1| maximal

    Soit a = |x2 - x1| et b = |y2 - y1|. On a a² + b² = d², avec a > 0, b > 0.

    Pour maximiser a + b sous la contrainte a² + b² = d², on sait que :
       a + b <= d * sqrt(2)
    avec égalité lorsque a = b = d / sqrt(2)

    Conclusion :
      La distance Manhattan maximale possible = d * sqrt(2)

    Cette valeur peut toujours être atteinte en positionnant une maison avec x entier
    ≠ 0, y = 0 et l'autre avec x = 0, y entier ≠ 0 tel que a² + b² = d².

    :param d: la distance euclidienne entre les maisons
    :return: la plus grande distance possible le long des routes
    """
    return d * math.sqrt(2)

if __name__ == "__main__":
    # Lecture de l'entrée
    d = float(input())
    # Calcul de la réponse
    res = manhattan_max_path(d)
    # Affichage de la réponse avec la précision demandée
    print(f"{res:.12f}")